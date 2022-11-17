<script setup></script>

<template>
  <!-- Page Container -->
  <div id="page-container" class="flex flex-col w-full min-h-screen mx-auto bg-gray-100">
    <!-- Page Content -->
    <main id="page-content" class="flex flex-col flex-auto max-w-full">
      <div class="flex items-center justify-center w-full p-4 py-0 mx-auto min-h-fit max-w-10xl lg:px-8 bg-gray-200/50">
        <!-- Sign Up Section -->
        <div class="w-full max-w-5xl lg:py-16">
          <!-- Sign Up Box -->
          <div class="flex flex-col overflow-hidden shadow-sm md:flex-row rounded-xl">
            <!-- Sign Up Form -->
            <section class="px-6 py-10 bg-white md:px-10 lg:p-16 md:w-1/2">
              <form class="space-y-6" @submit.prevent="s">
                <div class="space-y-1">
                  <input class="block w-full px-3 py-2 leading-6 placeholder-gray-400 border border-gray-200 rounded focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50" type="text" id="name" name="name" placeholder="아이디를 입력해주세요"
                  v-model="username"
                  >
                </div>
                <div class="space-y-1">
                  <input class="block w-full px-3 py-2 leading-6 placeholder-gray-400 border border-gray-200 rounded focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50" type="text" placeholder="닉네임을 입력해주세요"
                  v-model="nickname"
                  >
                </div>
                <div class="space-y-1">
                  <input class="block w-full px-3 py-2 leading-6 placeholder-gray-400 border border-gray-200 rounded focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50" type="password" id="password" name="password" placeholder="비밀번호를 입력해주세요"
                  v-model="password1"
                  >
                </div>
                <div class="space-y-1">
                  <input class="block w-full px-3 py-2 leading-6 placeholder-gray-400 border border-gray-200 rounded focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50" type="password" id="password_confirm" name="password_confirm" placeholder="비밀번호를 다시 입력해주세요"
                  v-model="password2"
                  >
                </div>
                <div class="flex items-center">
                  <input type="checkbox" id="remember_me" name="remember_me" class="w-4 h-4 text-blue-500 border border-gray-300 rounded focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50">
                  <span class="ml-2 text-sm font-medium">개인정보 제공에 동의합니다</span>
                </div>
                <div>
                  <button type="submit" class="inline-flex items-center justify-center w-full px-4 py-3 space-x-2 font-semibold leading-6 text-white border rounded border-cyan-500 bg-cyan-500 focus:outline-none hover:text-white hover:bg-cyan-600 hover:border-cyan-600 focus:ring focus:ring-blue-500 focus:ring-opacity-50 active:bg-blue-700 active:border-blue-700"
                  @click="signUp"
                  >
                    Create Account
                  </button>
                  <div class="mt-4">
                    <a href="#" class="inline-block text-sm font-medium text-blue-600 hover:text-blue-400">Return to Sign In</a>
                  </div>
                </div>
              </form>
            </section>
            <!-- END Sign Up Form -->
            
            <!-- END Sign Up Extra -->
            <div class="relative flex items-center px-6 py-10 bg-opacity-100 bg-cover md:px-10 lg:p-16 md:w-1/2" style="background-image: url('https://images.unsplash.com/photo-1485846234645-a62644f84728?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1459&q=80');">
              <div class="absolute inset-0 bg-opacity-50"></div>
              <div class="relative text-center sm:text-left">
                <p class="mb-0 text-2xl font-semibold leading-relaxed text-white">
                  ssafy에서 다양한 영화 컨텐츠를
                </p>
                <p class="mt-0 mb-2 text-2xl font-semibold leading-relaxed text-white">
                  함께 확인해봐요!
                </p>
                <p class="text-sm font-medium text-white/75">
                  류원창, 이지은
                </p>
              </div>
            </div>
            <!-- END Sign Up Extra -->
          </div>
          <!-- END Sign Up Box -->
        </div>
        <!-- END Sign Up Section -->
      </div>
    </main>
    <!-- END Page Content -->
  </div>
  <!-- END Page Container -->
</template>

<div style="display: none;">
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
    <label for="nickname">닉네임</label>
    <input type="text" id="nickname" v-model="nickname" />
    <br />
    <input type="submit" />
  </form>
</div>


<script>
import axios from "axios";

export default {
  name: "SignUpView",

  data() {
    return {
      username: "",
      nickname: "",
      password1: "",
      password2: "",
    };
  },
  methods: {
    signUp() {
      // console.log("sign up");
      let user = {
        username: this.username,
        nickname: this.nickname,
        password1: this.password1,
        password2: this.password2,
      };
      if (!this.nickname) {
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
          // console.log(res.data);
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
