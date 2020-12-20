<template>
  <a-carousel autoplay>
    <div><h3>社團宣傳輪播 1</h3></div>
    <div><h3>社團宣傳輪播 2</h3></div>
    <div><h3>社團宣傳輪播 3</h3></div>
    <div><h3>社團宣傳輪播 4</h3></div>
  </a-carousel>
</template>

<script>
export default {
  name: 'Ad'
}
</script>

<style scoped>
/* For demo */
.ant-carousel >>> .slick-slide {
  text-align: center;
  height: 540px;
  line-height: 160px;
  background: #364d79;
  overflow: hidden;
}

.ant-carousel >>> .slick-slide h3 {
  color: #fff;
}
</style>
