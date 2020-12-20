<template>
  <div :style="{ background: 'rgba(0,0,0,0.5)'}">
    <a-divider><div :style="{ padding: '10px', textAlign: 'center' }">
<h1 style="font-size:2vw">社團公告</h1>
</div></a-divider>
<div :style="{ padding: '10px' , background: 'rgba(0,0,0,0.5)', textAlign: 'center' }">
 <h1 style="font-size:1vw">建立公告</h1>
  <!-- </div></a-divider> -->
  <p>
    <a-divider style="width: 1500px ;background: #000" /></p>
<div :id="fixed-center" :style="{ padding: '24px', background: 'rgba(65,65,65,0.1)', textAlign: 'center' }">
    <a-card title="" :bordered="false" style="width: 1500px ; height: 350px ;background: rgba(70,70,70,0.1);textAlign: center">
      <a-form :form="form" :label-col="{ span: 1 }" :wrapper-col="{ span: 23 }" @submit="handleSubmit">
      <div :style="{ padding: '10px', textAlign: 'center' }">
      <a-form-item label="標題" style="{ padding: '10px', textAlign: 'center' }" >
      <a-input
        v-decorator="['note', { rules: [{ required: true, message: '請輸入公告的標題!' }] }]"
      />
      </a-form-item></div>
      </a-form>
      <a-textarea placeholder="請輸入內容......" :rows="10" />
      <p/>
      <a-button type="primary" @click="check" text-align=center style="rgba(0,0,0,0.5)">
      發佈
      </a-button>
    </a-card>
  </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'Page10',
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
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
