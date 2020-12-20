<template>
  <div>
    <a-divider>
      <h3>社團公告</h3>
    </a-divider>
    <a-table :columns="columns" :data-source="data">
      <a slot="name" slot-scope="text">{{ text }}</a>
    </a-table>
  </div>
</template>
<script>
/* eslint-disable */
const columns = [
  {
    title: '公告',
    dataIndex: 'announcement',
    key: 'announcement',
    width: 300,
  },
  {
    title: '時間',
    dataIndex: 'time',
    key: 'time',
    width: 100,
  },

];

const data = [
  {
    announcement: '今天天氣真好',
    time: '2020-13-13',
  },
  {
   announcement: '今天天氣不好',
    time: '2020-13-14',
  },
];

export default {
  name: 'Announce',
  data() {
    return {
      data,
      columns,
    };
  },
};
</script>

<style scoped>
h3 {
  font-weight: bold;
}
</style>
