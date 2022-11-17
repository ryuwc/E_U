<script setup></script>

<template>
  <!-- Page Container -->
  <div id="page-container" class="flex flex-col w-full min-h-screen mx-auto bg-gray-100">
    <!-- Page Content -->
    <main id="page-content" class="flex flex-col flex-auto max-w-full">
      <div class="flex items-center justify-center w-full min-h-screen p-4 mx-auto max-w-10xl lg:p-8 bg-gray-200/50">
        <!-- Sign Up Section -->
        <div class="w-full max-w-5xl lg:py-16">
          <!-- Sign Up Box -->
          <div class="flex flex-col overflow-hidden shadow-sm md:flex-row rounded-xl">
            <!-- Sign Up Form -->
            <section class="px-6 py-10 bg-white md:px-10 lg:p-16 md:w-1/2">
              <header class="mb-8 text-center md:text-left sm:mt-0">
                <h1 class="mb-1 text-2xl font-bold">
                  회원가입
                </h1>
              </header>
              <form class="space-y-6">
                <div class="space-y-1">
                  <label for="name" class="text-sm font-medium">Name</label>
                  <input class="block w-full px-3 py-2 leading-6 placeholder-gray-400 border border-gray-200 rounded focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50" type="text" id="name" name="name" placeholder="Enter your first name">
                </div>
                <div class="space-y-1">
                  <label for="email" class="text-sm font-medium">Email</label>
                  <input class="block w-full px-3 py-2 leading-6 placeholder-gray-400 border border-gray-200 rounded focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50" type="email" id="email" name="email" placeholder="Enter your email">
                </div>
                <div class="space-y-1">
                  <label for="password" class="text-sm font-medium">Password</label>
                  <input class="block w-full px-3 py-2 leading-6 placeholder-gray-400 border border-gray-200 rounded focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50" type="password" id="password" name="password" placeholder="Choose a strong password">
                </div>
                <div class="space-y-1">
                  <label for="password_confirm" class="text-sm font-medium">Confirm Password</label>
                  <input class="block w-full px-3 py-2 leading-6 placeholder-gray-400 border border-gray-200 rounded focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50" type="password" id="password_confirm" name="password_confirm" placeholder="Confirm your chosen password">
                </div>
                <div class="flex items-center">
                  <input type="checkbox" id="remember_me" name="remember_me" class="w-4 h-4 text-blue-500 border border-gray-300 rounded focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50">
                  <span class="ml-2 text-sm font-medium">I accept <a href="#" class="font-medium text-gray-600 underline hover:text-gray-500">terms &amp; conditions</a></span>
                </div>
                <div>
                  <button type="submit" class="inline-flex items-center justify-center w-full px-4 py-3 space-x-2 font-semibold leading-6 text-white bg-blue-700 border border-blue-700 rounded focus:outline-none hover:text-white hover:bg-blue-800 hover:border-blue-800 focus:ring focus:ring-blue-500 focus:ring-opacity-50 active:bg-blue-700 active:border-blue-700">
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
            <div class="relative flex items-center px-6 py-10 bg-blue-900 bg-cover md:px-10 lg:p-16 md:w-1/2 bg-opacity-80" style="background-image: url('https://source.unsplash.com/pEgsWN0kwbQ/600x800');">
              <div class="absolute inset-0 bg-blue-900 bg-opacity-50"></div>
              <div class="relative text-center sm:text-left">
                <p class="mb-2 font-semibold leading-relaxed text-white">
                  Amazing UI library with tons of available designs. It helped us build our project really fast!
                </p>
                <p class="text-sm font-medium text-white/75">
                  John Doe, Web Developer
                </p>
              </div>
            </div>
            <!-- END Sign Up Extra -->
          </div>
          <!-- END Sign Up Box -->
  
          <!-- Footer -->
          <div class="mt-5 text-sm text-center text-gray-600">
            <a class="font-medium text-blue-600 hover:text-blue-400" href="https://tailkit.com" target="_blank">Tailkit</a> by <a class="font-medium text-blue-600 hover:text-blue-400" href="https://pixelcave.com" target="_blank">pixelcave</a>
          </div>
          <!-- END Footer -->
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
