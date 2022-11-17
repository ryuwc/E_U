<template>
  <div id="app">
    <nav>
      <router-link to="/signup">Sign Up</router-link> |
      <router-link to="/login">Login</router-link> |
      <button @click="logOut">로그아웃</button>
    </nav>
    <input type="hidden" name="_token" :value="csrf">
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',

  data() {
    return {
      csrf: document.head.querySelector('meta[name="csrf-token"]') ? document.head.querySelector('meta[name="csrf-token"]').content : '',
    };
  },
  methods: {
    logOut() {
      axios({
        method: 'DELETE',
        url: "http://127.0.0.1:8000/accounts/logout/",

      })
      .then(res => {
        console.log(res);
      })
    }
  },
  created() {
    if (! this.csrf) {
            console.warn('The CSRF token is missing. Ensure that the HTML header includes the following: <meta name="csrf-token" content="{{ csrf_token() }}">');
        }
    console.log(this.csrf);
  }
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
