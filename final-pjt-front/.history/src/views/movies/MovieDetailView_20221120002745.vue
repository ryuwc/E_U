<template>
  <div>
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
    <MovieDetailInfo/>
  </div>
</template>

<script>
import MovieDetailInfo from '@/components/MovieDetailInfo.vue';

export default {
  name: 'MovieDetailView',

  data() {
    return {
      
    };
  },
  components: {
    MovieDetailInfo,
  },

  mounted() {
    
  },

  methods: {
    
  },
};
</script>

<style scoped>
nav {
  z-index: 8;
}
</style>