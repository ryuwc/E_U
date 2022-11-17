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
              <form class="space-y-6" @submit.prevent="login({username: username, password: password})">
                <div class="space-y-1">
                  <input class="block w-full px-3 py-2 leading-6 placeholder-gray-400 bg-white border rounded rounded-md shadow-sm focus:outline-none focus:border-sky-500 focus:ring-sky-500 sm:text-sm focus:ring-1" type="text" id="name" name="name" placeholder="아이디를 입력해주세요"
                  v-model="username"
                  >
                </div>
                <div class="space-y-1">
                  <input class="block w-full px-3 py-2 leading-6 placeholder-gray-400 border rounded focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50" type="password" id="password_confirm" name="password" placeholder="비밀번호 입력해주세요"
                  v-model="password"
                  >
                </div>
                <div class="flex items-center">
                  <input type="checkbox" id="remember_me" name="remember_me" class="w-4 h-4 text-blue-500 border border-gray-300 rounded focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50">
                  <span class="ml-2 text-sm font-semibold">Remember Me</span>
                </div>
                <div>
                  <button type="submit" class="inline-flex items-center justify-center w-full px-4 py-3 space-x-2 font-semibold leading-6 text-white border rounded border-cyan-500 bg-cyan-500 focus:outline-none hover:text-white hover:bg-cyan-600 hover:border-cyan-600 focus:ring focus:ring-blue-500 focus:ring-opacity-50 active:bg-blue-700 active:border-blue-700">
                    Create Account
                  </button>
                  <div class="mt-4">
                    <router-link to="/signup"><a href="#" class="inline-block text-sm font-medium text-blue-600 hover:text-blue-400">Return to Sign In</a></router-link>
                  </div>
                </div>
              </form>
            </section>
            <!-- END Sign Up Form -->
            
            <!-- END Sign Up Extra -->
            <div class="relative flex items-center px-6 py-10 bg-opacity-100 bg-cover md:px-10 lg:p-16 md:w-1/2" 
            style="background-image: url('https://images.unsplash.com/photo-1612635466104-e3aab50680b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80');">
              <div class="absolute inset-0 bg-opacity-50"></div>
              <div class="relative text-center sm:text-left">
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

  <!-- <div>
    <h4>로그인</h4>
    <form @submit.prevent="login({username: username, password: password})">
      <label for="username">아이디</label>
      <input type="text" id="username" v-model="username" />
      <br />
      <label for="password">비밀번호</label>
      <input type="password" id="password" v-model="password" />
      <br />
      <input type="submit" />
    </form>
  </div> -->

<script>
import { mapActions } from 'vuex';

const accountsStore = 'accountsStore'

export default {
  name: 'LoginView',

  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    ...mapActions(accountsStore, ['login']),
    
  },
};
</script>

<style scoped>

</style>