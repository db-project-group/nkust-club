<template>
  <div>
    <a-card title="Default size card" style="width: 300px">
      <a slot="extra" href="#">more</a>
      <p>card content</p>
      <p>card content</p>
      <p>card content</p>
    </a-card>
    <br />
    <a-card size="small" title="Small size card" style="width: 300px">
      <a slot="extra" href="#">more</a>
      <p>card content</p>
      <p>card content</p>
      <p>card content</p>
    </a-card>
  </div>
</template>

<script>
export default {
  name: 'Home',
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
