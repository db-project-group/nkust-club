<template>
  <a-layout-sider width="200" :style="{ background: '#fff'}">
    <a-menu
      mode="inline"
      :default-selected-keys="['2']"
      :default-open-keys="['sub2']"
      style="height: 100%"
    >
      <a-menu-item key="1">
        <router-link to="/home">
          社團清單
        </router-link>
      </a-menu-item>
      <a-sub-menu key="sub2">
        <span slot="title">社團管理</span>
        <a-menu-item key="2">
          <router-link :to="{ name: 'manageMember', params: { id: $route.params.id } }">
            社員名單
          </router-link>
        </a-menu-item>
        <a-menu-item key="3">
          <router-link :to="{ name: 'manageAnnounce', params: { id: $route.params.id } }">
            社團公告
          </router-link>
        </a-menu-item>
      </a-sub-menu>
    </a-menu>
  </a-layout-sider>
</template>

<script>
export default {
  name: 'Sidebar'
}
</script>
