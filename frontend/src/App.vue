<template>
  <div id="app">
    <a-layout id="components-layout-demo-top-side">
      <router-view class="header" name="header"/>
      <a-layout :style="{ height: 'calc(95vh)', marginTop: '64px' }">
        <router-view class="sidebar" name="sidebar"/>
        <a-layout-content :style="{ padding: '0 50px' }">
          <a-breadcrumb style="margin: 16px 0">
            <a-breadcrumb-item>Home</a-breadcrumb-item>
            <a-breadcrumb-item>List</a-breadcrumb-item>
            <a-breadcrumb-item>App</a-breadcrumb-item>
          </a-breadcrumb>
          <a-layout style="padding: 24px 0; background: #fff">
            <a-layout-content :style="{ padding: '0 24px', minHeight: '280px' }">
              <router-view/>
            </a-layout-content>
          </a-layout>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

</style>
