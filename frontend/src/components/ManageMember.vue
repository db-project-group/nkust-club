<template>
  <div>
    <a-divider>
      <h3>社員名單</h3>
    </a-divider>
    <a-button class="editable-add-btn" @click="handleAdd">
      新增社員
    </a-button>
   <a-table :columns="columns" :data-source="data" bordered>
    <template
      v-for="col in ['grades','number','name', 'office']"
      :slot="col"
      slot-scope="text, record, index"
    >
      <div :key="col">
        <a-input
          v-if="record.editable"
          style="margin: -5px 0"
          :value="text"
          @change="e => handleChange(e.target.value, record.key, col)"
        />
        <template v-else>
          {{ text }}
        </template>
      </div>
    </template>
    <template slot="operation" slot-scope="text, record, index">
      <div class="editable-row-operations">
        <span v-if="record.editable">
          <a @click="() => save(record.key)">Save</a>
          <a-divider type="vertical" />
          <a-popconfirm title="Sure to cancel?" @confirm="() => cancel(record.key)">
            <a>Cancel</a>
          </a-popconfirm>
        </span>
        <span v-else>
          <a :disabled="editingKey !== ''" @click="() => edit(record.key)">Edit</a>
          <a-divider type="vertical" />
          <a @click="() => onDelete(record.key)">Delete</a>
        </span>
      </div>
    </template>
  </a-table>
  </div>
</template>

<script>
/* eslint-disable */
const columns = [
  {
    title: '班級',
    dataIndex: 'grades',
    width: '15%',
    scopedSlots: { customRender: 'grades' },
  },
  {
    title: '學號',
    dataIndex: 'number',
    width: '15%',
    scopedSlots: { customRender: 'number' },
  },
  {
    title: '姓名',
    dataIndex: 'name',
    width: '25%',
    scopedSlots: { customRender: 'name' },
  },
  {
    title: '職位',
    dataIndex: 'office',
    width: '15%',
    scopedSlots: { customRender: 'office' },
  },
  {
    title: 'operation',
    dataIndex: 'operation',
    scopedSlots: { customRender: 'operation' },
  },
];

const data = [];
for (let i = 11; i < 29; i++) {
  data.push({
    key: i.toString(),
    grades: `四資工三甲`,
    number: `C1071511${i}`,
    name: `Edrward ${i}`,
    office: `社員`,
  });
}
export default {
  name: 'Member',
  data () {
    return {
      
    }
  },
  mounted () {
    // $("#menu-toggle").click(function(e) {
    //   e.preventDefault();
    //   $("#wrapper").toggleClass("toggled");
    // });
  },
  data() {
    this.cacheData = data.map(item => ({ ...item }));
    return {
      data,
      columns,
      editingKey: '',
      count:29,
    };
  },
  methods: {
    handleChange(value, key, column) {
      const newData = [...this.data];
      const target = newData.filter(item => key === item.key)[0];
      if (target) {
        target[column] = value;
        this.data = newData;
      }
    },
    edit(key) {
      const newData = [...this.data];
      const target = newData.filter(item => key === item.key)[0];
      this.editingKey = key;
      if (target) {
        target.editable = true;
        this.data = newData;
      }
    },
    save(key) {
      const newData = [...this.data];
      const newCacheData = [...this.cacheData];
      const target = newData.filter(item => key === item.key)[0];
      const targetCache = newCacheData.filter(item => key === item.key)[0];
      if (target && targetCache) {
        delete target.editable;
        this.data = newData;
        Object.assign(targetCache, target);
        this.cacheData = newCacheData;
      }
      this.editingKey = '';
    },
    cancel(key) {
      const newData = [...this.data];
      const target = newData.filter(item => key === item.key)[0];
      this.editingKey = '';
      if (target) {
        Object.assign(target, this.cacheData.filter(item => key === item.key)[0]);
        delete target.editable;
        this.data = newData;
      }
    },
    handleAdd() {
      const { count, data } = this;
      const newData = {
        key: count.toString(),
        grades: `四資工三甲`,
        number: `C1071511${count}`,
        name: `Edrward ${count}`,
        office: `社員`,
      }
      this.data = [...data, newData];
      this.count = count + 1;
    },
    onDelete(key) {
      const data = [...this.data];
      this.data = data.filter(item => item.key !== key);
    },
  },
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  font-weight: bold;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
