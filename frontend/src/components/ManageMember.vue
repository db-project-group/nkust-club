<template>
  <div>
    <a-divider>
      <h3>社員名單</h3>
    </a-divider>
    <a-button class="editable-add-btn" @click="handleAdd">
      新增社員
    </a-button>
   <a-table :columns="columns" :data-source="club.members" bordered>
    <template
      v-for="col in ['department','id','name', 'job']"
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
          <a-popconfirm title="Sure to cancel?" @confirm="() => cancel(record.key)">
            <a>Cancel</a>
          </a-popconfirm>
        </span>
        <span v-else>
          <a :disabled="editingKey !== ''" @click="() => edit(record.key)">Edit</a>
          <a-divider type="vertical" />
          <a href="javascript:;">Delete</a>
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
    dataIndex: 'department',
    width: '15%',
    scopedSlots: { customRender: 'department' },
  },
  {
    title: '學號',
    dataIndex: 'id',
    width: '15%',
    scopedSlots: { customRender: 'id' },
  },
  {
    title: '姓名',
    dataIndex: 'name',
    width: '25%',
    scopedSlots: { customRender: 'name' },
  },
  {
    title: '職位',
    dataIndex: 'job.name',
    width: '15%',
    scopedSlots: { customRender: 'job' },
  },
  {
    title: 'operation',
    dataIndex: 'operation',
    scopedSlots: { customRender: 'operation' },
  },
];

export default {
  name: 'Member',
  data () {
    // this.cacheData = data.map(item => ({ ...item }));
    return {
      club: {},
      columns,
      editingKey: '',
    };
  },
  mounted () {
    console.log()
    this.getClub()
  },
  methods: {
    getClub () {
      this.axios.get(
        `/club/${this.$route.params.id}`
      ).then((response) => {
        console.log(response.data)
        let club = response.data.club
        this.club = club
      })
    },
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
      const { count, dataSource } = this;
      const newData = {
        key: count,
        grades: `4csie ${i}`,
        number: 1,
        name: `Edrward ${i}`,
        office: `社員 ${i}`,
      }
      this.dataSource = [...dataSource, newData];
      this.count = count + 1;
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
