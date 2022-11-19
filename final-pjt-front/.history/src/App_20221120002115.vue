<template>
  <div id="app">
    <nav>
      <router-link  to="/home">| Home |</router-link>
      <router-link v-if="!isLogin" to="/signup">| Sign Up |</router-link>
      <router-link v-if="!isLogin" to="/login">Login |</router-link>
      <button v-if="isLogin" @click="logOut">로그아웃 |</button>
      <router-link v-if="isLogin" to="/edit">정보수정</router-link> |
      
      <!-- 정보 수정은 프로필 페이지에서만 가능하게 -->
      <!-- <router-link v-if="isLogin" to="/edit">정보수정 |</router-link> -->
      
      <router-link v-if="isLogin" to="/profile">Profile |</router-link>
      <router-link to="/practice">연습</router-link> |
    </nav>
    <router-view/>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

const moviesStore = 'moviesStore'

export default {

  name: 'App',

  data() {
    return {
    };
  },
  methods: {
    ...mapActions('accountsStore', ['logOut']),
    ...mapActions(moviesStore, ['getMovies']),
    ...mapActions(moviesStore, ['getNowMovies']),
    
  },
  computed: {
    ...mapGetters('accountsStore', ['isLogin']),
    ...mapGetters('accountsStore', ['nickname']),
  },
  created() {
    this.getMovies(),
    this.getNowMovies()
  }
};
</script>

<style>

nav {
  padding: 30px;
  z-index: 2;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
