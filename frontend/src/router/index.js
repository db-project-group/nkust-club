import Vue from 'vue'
import Router from 'vue-router'
import Header from '@/components/Header'
import Sidebar from '@/components/Sidebar'
import Index from '@/components/Index'
import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      components: {
        default: Home,
        header: Header
      }
    },
    {
      path: '/home',
      name: 'Home',
      components: {
        default: Home,
        header: Header,
        sidebar: Sidebar
      }
    }
  ]
})
