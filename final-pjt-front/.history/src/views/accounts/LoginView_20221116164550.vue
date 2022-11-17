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
import axios from 'axios';
import { log } from 'console';

export default {
  name: 'FinalPjtFrontLoginView',

  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login() {
      const user = {
        username: this.username,
        password: this.password,
      };
      axios({
        method: 'post',
        url: "http://127.0.0.1:8000/accounts/login/",
        data: { ...user },
      })
      .then(res => {
        console.log(res);
      })
    }
  },
};
</script>

<style scoped>

</style>