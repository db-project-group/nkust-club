import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

/* eslint-disable no-new */
Vue.use(Vuex)

const store = new Vuex.Store({
    plugins: [createPersistedState()],
    state: {
        user: '',
        isLoading: false,
        num: ['1']
    },
    mutations: {
        loading (state, str) {
            let list = []
            list.push(str)
            state.num = [...state.num, ...list]
            console.log('ok')
        }
    },
    gets: {
        readuser(state){
            return state.user
        }
    }
})

export default store