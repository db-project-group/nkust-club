<template>
  <a-layout-header class="header" :style="{ position: 'fixed', zIndex: 1, width: '100%' }">
    <router-link to="/" class="logo">
      <p :style="{ margin: '-14px 0 0 5px'}">高科大社團管理系統</p>
    </router-link>
    <a-menu
      theme="dark"
      mode="horizontal"
      :style="{ lineHeight: '64px', float: 'right' }"
    >
      <a-menu-item key="1">
        <a-badge dot><a-avatar style="backgroundColor: #00000000" icon="bell" /></a-badge>
      </a-menu-item>
      <a-menu-item key="2">
        <a-avatar style="backgroundColor: #00000000" icon="user" />
        <!-- <a-popconfirm
          title="Are you sure logout?"
          ok-text="Yes"
          cancel-text="No"
          @confirm="confirm"
          @cancel="cancel"
        >
          <a href="#"><a-avatar style="backgroundColor:#00000000" icon="user" /></a>
        </a-popconfirm> -->
      </a-menu-item>
    </a-menu>
  </a-layout-header>
</template>

<script>
export default {
  name: 'Header',
  methods: {
    confirm (e) {
      console.log(e)
      this.$message.success('Click on Yes')
    },
    cancel (e) {
      console.log(e)
      this.$message.error('Click on No')
    }
  }
}
</script>

<style>
#components-layout-demo-top-side .logo {
  width: 140px;
  height: 35px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px 28px 16px 0;
  float: left;
  color: rgba(255, 255, 255, 0.8);
}
</style>
