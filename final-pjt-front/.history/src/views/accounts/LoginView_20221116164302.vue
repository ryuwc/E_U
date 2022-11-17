<template>
  <div>
    <h4>로그인</h4>
    <form @submit.prevent="login">
      <label for="username">아이디</label>
      <input type="text" id="username" v-model="username" />
      <br />
      <label for="password">비밀번호</label>
      <input type="password" id="password" v-model="password" />
      <br />
      <input type="submit" />
    </form>
  </div>
</template>

<script>
export default {
  name: 'FinalPjtFrontLoginView',

  data() {
    return {
      
    };
  },

  mounted() {
    
  },

  methods: {
    
  },
};
</script>

<style scoped>

</style>