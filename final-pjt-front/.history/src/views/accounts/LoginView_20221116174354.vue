<template>
  <div>
    <h4>로그인</h4>
    <form @submit.prevent="login(user)">
      <label for="username">아이디</label>
      <input type="text" id="username" v-model="username" />
      <br />
      <label for="password">비밀번호</label>
      <input type="password" id="password" v-model="password" />
      <br />
      {{ user }}
      <input type="submit" />
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

const accountsStore = 'accountsStore'

export default {
  name: 'FinalPjtFrontLoginView',

  data() {
    return {
      username: '',
      password: '',
      user: {
        username: this.username,
        password: this.password,
      }
    };
  },
  methods: {
    ...mapActions(accountsStore, ['login']),
    
  },
};
</script>

<style scoped>

</style>