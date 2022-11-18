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
