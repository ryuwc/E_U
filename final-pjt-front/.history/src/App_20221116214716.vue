<template>
  <div id="app">
    <nav>
      <router-link to="/signup">Sign Up</router-link> |
      <router-link to="/login">Login</router-link> |
      <button @click="logOut">로그아웃</button>
    </nav>
    <meta name="csrf-token" id="token" content="{{ csrf_token() }}" />
    <router-view />
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "App",

  data() {
    return {};
  },
  methods: {
    logOut() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/logout/",
      }).then((res) => {
        console.log(res);
      });
    },
  },
  created() {
    axios({
      method: "get",
      url: `${API_URL}/accounts/profile/${username}`,
      csrf_token: window.Laravel.csrfToken,
    })
      .then((res) => {
        console.log(JSON.stringify(res));
        console.log(res);
        // commit("SET_USER", res.data);
      })
      .catch((err) => {
        console.log(err);
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
