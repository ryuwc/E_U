<template>
  <div id="app">
    <nav>
      <router-link to="/signup">Sign Up</router-link> |
      <router-link v-if="!isLogin" to="/login">Login</router-link> |
      <button v-if="!isLogin" @click="logOut">로그아웃</button> |
      <router-link v-if="!isLogin" to="/edit">정보수정</router-link> |
    </nav>
    <p v-if="nickname">안녕하세요, {{ nickname }}님</p>
    <router-view/>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';


export default {

  name: 'App',

  data() {
    return {
    };
  },
  methods: {
    ...mapActions('accountsStore', ['logOut']),
  },
  computed: {
    ...mapGetters('accountsStore', ['isLogin']),
    ...mapGetters('accountsStore', ['nickname']),
  },
  created() {
    
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
