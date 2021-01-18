import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

import auth from './modules/auth.js'

/* eslint-disable */
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth
  },
  plugins: [createPersistedState({
    storage: window.localStorage,
    reducer(val) {
      return {
        auth: val.auth
      }
    }
  })]
})

export default store
