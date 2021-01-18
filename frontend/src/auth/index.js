import router from '@/router'

/* eslint-disable */

export default {
  user: {
    isAuthorized: false
  },
  login(context, data, isAuthorized, redirect) {
    context.axios.post(
        '/auth',
        data
      ).then((response) => {
        console.log(response.data)

        localStorage.setItem('jwt', response.data.access_token)
        localStorage.setItem('email', response.data.email)
        localStorage.setItem('name', response.data.name)
        localStorage.setItem('student_id', response.data.student_id)
        this.isAuthorized = isAuthorized

        if (redirect) {
          router.push(redirect)
        }
      })
  },
  logout () {
    localStorage.removeItem('jwt')
    this.user.isAuthorized = false
  },
  checkAuth () {
    let jwt = localStorage.getItem('jwt')
    if (jwt) {
      this.user.isAuthorized = true
    } else {
      this.user.isAuthorized = false
    }
  }
}

// export default {
//   namespace: true,
//   state: {
//     jwt: null,
//     email: null,
//     name: null,
//     student_id: null,
//     isLogin: false
//   },
//   mutations: {
//     SET_AUTH(state, options) {
//       state.jwt = options.jwt
//       state.email = options.email
//       state.name = options.name
//       state.student_id = options.student_id
//       state.isLogin = options.isLogin
//     }
//   },
//   actions: {
//     setAuth(context, options) {
//       context.commit('SET_AUTH', {
//         jwt: options.jwt,
//         email: options.email,
//         name: options.name,
//         student_id: options.student_id,
//         isLogin: options.isLogin
//       })
//     }
//   }
// }
