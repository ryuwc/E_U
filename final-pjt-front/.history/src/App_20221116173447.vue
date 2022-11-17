<template>
  <div id="app">
    <nav>
      <router-link to="/signup">Sign Up</router-link> |
      <router-link to="/login">Login</router-link> |
      <button @click="logOut">로그아웃</button>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios';
import accountsStore from './store/modules/accountsStore';


export default {
  name: 'App',

  data() {
    return {
    };
  },
  methods: {
    logOut() {
      axios({
        method: 'post',
        url: "http://127.0.0.1:8000/accounts/logout/",
      })
      .then(res => {
        console.log(res);
      })
    }
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
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
