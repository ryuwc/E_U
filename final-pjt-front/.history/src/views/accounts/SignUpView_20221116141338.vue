<template>
  <div>
    <h4>회원가입</h4>
    <form>
      <label for="username">아이디</label>
      <input
        type="text"
        id="username"
      />
      <label for="email">이메일</label>
      <input
        type="email"
        id="email"
      />
      <label for="password1">비밀번호 1</label>
      <input
        type="password"
        id="password1"
      />
      <label for="password2">비밀번호 2</label>
      <input
        type="password"
        id="password2"
      />
    </form>
  </div>
</template>

<script>
export default {
  name: "SignUpView",

  data() {
    return {};
  },

  mounted() {},

  methods: {},
};
</script>

<style scoped></style>
