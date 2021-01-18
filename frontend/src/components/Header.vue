<template>
  <a-layout-header class="header" :style="{ position: 'fixed', zIndex: 1, width: '100%' }">
    <router-link to="/" class="logo">
      <p :style="{ margin: '-14px 0 0 5px'}">高科大社團管理系統</p>
    </router-link>
    <!-- <a-menu
      theme="dark"
      mode="horizontal"
      :style="{ lineHeight: '64px', float: 'right' }"
    >
      <a-menu-item key="1" v-if="isAuthorized">
        <a-popconfirm
          title="Are you sure logout?"
          ok-text="登出"
          cancel-text="取消"
          @confirm="confirm"
          @cancel="cancel"
        >
          <a-avatar style="backgroundColor: #00000000" icon="user" />
        </a-popconfirm>
      </a-menu-item>
    </a-menu> -->
  </a-layout-header>
</template>

<script>
import auth from '@/auth'

/* eslint-disable */
export default {
  name: 'Header',
  data () {
    return {
      // isAuthorized: false
    }
  },
  computed: {
    // isAuthorized: function () {
    //   return auth.user.isAuthorized
    // }
  },
  // watch: {
  //   isAuthorized
  // },
  // updated(){
  //   this.drawMap()
  // },
  // mounted () {
  //   console.log(auth)
  //   this.isAuthorized = auth.user.isAuthorized
  // },
  methods: {
    isAuthorized: function () {
      return auth.user.isAuthorized
    },
    confirm (e) {
      // console.log(e)
      this.$message.success('登出成功')
      auth.logout()
      auth.logout
    },
    cancel (e) {
      // console.log(e)
      this.$message.error('取消登出')
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
