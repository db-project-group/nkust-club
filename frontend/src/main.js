// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// import store from './store'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
import GAuth from 'vue-google-oauth2'
import axios from 'axios'
import VueAxios from 'vue-axios'

/* eslint-disable no-new */
Vue.config.productionTip = false

Vue.use(Antd)

Vue.use(VueAxios, axios)

const gauthOptions = {
  clientId: '687495968491-6k4toog7o8ajqvie4mj28pjnbkgnishm.apps.googleusercontent.com',
  scope: 'profile email',
  prompt: 'select_account'
}

Vue.use(GAuth, gauthOptions)

window.app = new Vue({
  el: '#app',
  router,
  // store,
  components: { App },
  template: '<App/>'
})
