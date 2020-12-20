<template>
  <div>
    <a-divider>
        <h2>高科大社團管理系統</h2>
    </a-divider>
    <a-row type="flex" justify="center" align="top" :style="{ 'margin-bottom': '50px' }">
      <a-col :span="3">
        <router-link to="/home" class="google-signin-button" text-align=center>
          <a-icon type="google" :style="{ 'margin-right': '10px' }" /> 使用 Google 登入
        </router-link>
      </a-col>
    </a-row>
    <a-row type="flex" justify="center" align="middle">
      <a-col :span="12">
        <router-view/>
      </a-col>
    </a-row>
    <!-- <button v-google-login-button="clientId" class="google-signin-button" text-align=center>
      Continue with Google
    </button> -->
    <!-- <div :style="{ textAlign: 'center' }">
    </div> -->
  </div>
</template>

<script>
/* eslint-disable */
// import GoogleLoginButton from 'vue-google-login-button-directive'
export default {
  name: 'Index',
  data () {
    return {

    }
  },
  mounted () {
    // $("#menu-toggle").click(function(e) {
    //   e.preventDefault();
    //   $("#wrapper").toggleClass("toggled");
    // });
  }
  // directives: {
  //     GoogleLoginButton
  //   },
  //   data: () => ({
  //     clientId: 'Your_Google_Client-Id'
  //   }),
  //   methods: {
  //     OnGoogleAuthSuccess(idToken) {
  //       // Receive the idToken and make your magic with the backend
  //     },
  //     OnGoogleAuthFail(error) {
  //       console.log(error)
  //     }
  //   }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: bold;
  font-size: 42px;
}
/* ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
} */
.google-signin-button {
    color: white;
    background-color: rgb(8, 18, 59);
    height: 50px;
    font-size: 16px;
    border-radius: 10px;
    padding: 20px 20px 25px 20px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }
</style>
