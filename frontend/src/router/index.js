import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Header from '@/components/Header'
import Sidebar from '@/components/Sidebar'
import Ad from '@/components/Ad'
import Home from '@/components/Home'
import BreadCrumb from '@/components/BreadCrumb'
import ManageMember from '@/components/ManageMember'
import ManageAnnounce from '@/components/ManageAnnounce'
import Announce from '@/components/Announce'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      components: {
        default: Index,
        header: Header,
        breadcrumb: BreadCrumb
      },
      children: [
        {
          path: '',
          component: Ad
        }
      ]
    },
    {
      path: '/home',
      name: 'home',
      components: {
        default: Home,
        header: Header,
        breadcrumb: BreadCrumb
      }
    },
    {
      path: '/manage/:id',
      name: 'manage',
      components: {
        default: ManageMember,
        header: Header,
        sidebar: Sidebar
      }
    },
    {
      path: '/manage/:id/member',
      name: 'manageMember',
      components: {
        default: ManageMember,
        header: Header,
        sidebar: Sidebar
      }
    },
    {
      path: '/manage/:id/announce',
      name: 'manageAnnounce',
      components: {
        default: ManageAnnounce,
        header: Header,
        sidebar: Sidebar
      }
    },
    {
      path: '/announce/:id',
      name: 'announce',
      components: {
        default: Announce,
        header: Header,
        breadcrumb: BreadCrumb
      }
    }
  ],
  mode: 'history'
})
