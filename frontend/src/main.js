// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// import store from './store'
import auth from './auth'

import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
import GAuth from 'vue-google-oauth2'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false

const instance = axios.create({
  baseURL: 'http://localhost:5000/api/v1/',
  headers: { 'Content-Type': 'application/json' },
  timeout: 2000
})

instance.interceptors.request.use(
  config => {
    if (localStorage.getItem('jwt')) {
      config.headers.Authorization = `Bearer ${localStorage.getItem('jwt')}`
    }
    return config
  },
  error => {
    return Promise.reject(error)
  })

instance.interceptors.response.use(
  response => {
    return response
  },
  error => {
    if (error.response) {
      console.log('axios:' + error.response.status)
      switch (error.response.status) {
        case 401:
        case 422:
          auth.logout()
          router.replace({ path: 'index' })
      }
    }
    return Promise.reject(error.response.data)
  })

auth.checkAuth()

router.beforeEach((to, from, next) => {
  if (to.path === '/') {
    if (localStorage.getItem('jwt')) {
      next('/home')
    } else {
      next()
    }
  } else {
    if (localStorage.getItem('jwt')) {
      next()
    } else {
      next('/')
    }
  }
  // if (localStorage.getItem('jwt') || ) {
  //   console.log("111")
  //   next()
  // } else {
  //   console.log("222")
  //   next('/')
  // }
})

const gauthOptions = {
  clientId: '612719863118-7j2h2p13ggleivj2a3sgbp6jrsnfchmi.apps.googleusercontent.com',
  scope: 'profile email',
  prompt: 'select_account'
}

Vue.use(GAuth, gauthOptions)
Vue.use(VueAxios, instance)
Vue.use(Antd)

/* eslint-disable no-new */
window.app = new Vue({
  el: '#app',
  router,
  // store,
  components: { App },
  template: '<App/>'
})
