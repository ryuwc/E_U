<template>
  <div>
    <h4>회원가입</h4>
    <form @submit.prevent="signUp">
      <label for="username">아이디</label>
      <input type="text" id="username" v-model="username" />
      <br />
      <label for="password1">비밀번호 1</label>
      <input type="password" id="password1" v-model="password1" />
      <br />
      <label for="password2">비밀번호 2</label>
      <input type="password" id="password2" v-model="password2" />
      <br />
      <input type="submit" />
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignUpView",

  data() {
    return {
      username: "",
      email: "",
      password1: "",
      password2: "",
    };
  },
  methods: {
    signUp() {
      // console.log("sign up");
      let user = {
        username: this.username,
        email: this.email,
        password1: this.password1,
        password2: this.password2,
      };
      if (!this.email) {
        user = {
          username: this.username,
          password1: this.password1,
          password2: this.password2,
        };
      }
      console.log(user);
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/signup/",
        data: { ...user },
      })
        .then((res) => {
          console.log(res.data);
          this.$store.state.token = res.data.key;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped></style>
