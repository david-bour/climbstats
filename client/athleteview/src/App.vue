<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld :arr="arr" msg="Climbers" />
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
// import uniqueId from "lodash.uniqueid";
import axios from "axios";

export default {
  name: "App",
  components: {
    HelloWorld,
  },
  data() {
    return {
      arr: null,
    };
  },
  mounted() {
    axios
      .get("http://localhost:8000/athletes")
      .then((response) => {
        this.arr = response.data.result;
      });
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
