<template>
  <div>
    <a-divider>
      <h3>社團公告</h3>
    </a-divider>
    <a-button class="editable-add-btn" @click="handleAdd">
      新增公告
    </a-button>
   <a-table :columns="columns" :data-source="data" bordered>
    <template
      v-for="col in ['announcement','member','time']"
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
          <a @click="() => save(record.key)">Save </a>
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
    title: '標題',
    dataIndex: 'title',
    width: '15%',
    scopedSlots: { customRender: 'title' },
  },
  {
    title: '內容',
    dataIndex: 'announcement',
    width: '15%',
    scopedSlots: { customRender: 'announcement' },
  },
  {
    title: '張貼者',
    dataIndex: 'member',
    width: '15%',
    scopedSlots: { customRender: 'member' },
  },
  {
    title: '時間',
    dataIndex: 'time',
    width: '25%',
    scopedSlots: { customRender: 'time' },
  },
  {
    title: 'operation',
    dataIndex: 'operation',
    scopedSlots: { customRender: 'operation' },
  },
];

const data = [];
for (let i = 0; i < 20; i++) {
  data.push({
    key: i.toString(),
    title: `社課公告`,
    announcement: `今天晚上有上課!`,
    member: `我是社長吧`,
    time: `2020/12/20 02:25`
  });
}
export default {
  name: 'ManageAnnounce',
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
      console.log(this);
      const { count, dataSource } = this;
      const newData = {
        key: count,
        title: `社課公告`,
        announcement: `今天晚上有上課!`,
        member: `我是社長吧`,
        time: `2020/12/20 02:25`
      }
      // this = [...dataSource, newData];
      // this.count = count + 1;
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
