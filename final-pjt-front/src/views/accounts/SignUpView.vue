<script setup></script>

<template>
  <!-- Page Container -->
  <div id="page-container" class="flex flex-col w-full min-h-screen mx-auto" style="background-color: rgba(0, 0, 0, 0.1);">
    <div id="for_nav"></div>
    <!-- Page Content -->
    <main id="page-content" class="flex flex-col flex-auto max-w-full mt-28">
      <div class="flex items-center justify-center w-full p-4 py-0 mx-auto min-h-fit max-w-10xl lg:px-8">
        <!-- Sign Up Section -->
        <div class="w-full max-w-5xl lg:py-16">
          <!-- Sign Up Box -->
          <div class="flex flex-col overflow-hidden shadow-sm md:flex-row rounded-xl">
            <!-- Sign Up Form -->
            <section class="px-6 py-10 bg-white md:px-10 lg:p-16 md:w-1/2">
              <form class="space-y-6" @submit.prevent="signUp({username: username, nickname: nickname, password1: password1, password2: password2 })">
                <div class="space-y-1">
                  <input class="block w-full px-3 py-2 leading-6 placeholder-gray-400 border rounded shadow-lg focus:outline-none focus:border-sky-500 focus:ring-sky-500 sm:text-sm focus:ring-1" type="text" id="name" name="name" placeholder="아이디를 입력해주세요"
                  v-model="username"
                  >
                  <p class="text-xs italic text-red-500">{{ msg }}</p>
                </div>
                <div class="space-y-1">
                  <input class="block w-full px-3 py-2 leading-6 placeholder-gray-400 border rounded shadow-lg focus:outline-none focus:border-sky-500 focus:ring-sky-500 sm:text-sm focus:ring-1" type="text" placeholder="닉네임을 입력해주세요"
                  v-model="nickname"
                  >
                </div>
                <div class="space-y-1">
                  <input class="block w-full px-3 py-2 leading-6 placeholder-gray-400 border rounded shadow-lg focus:outline-none focus:border-sky-500 focus:ring-sky-500 sm:text-sm focus:ring-1" type="password" id="password" name="password" placeholder="비밀번호를 입력해주세요"
                  v-model="password1"
                  >
                  <p class="text-xs italic text-red-500">{{ msgpassword1 }}</p>
                </div>
                <div class="space-y-1">
                  <input class="block w-full px-3 py-2 leading-6 placeholder-gray-400 border rounded shadow-lg focus:outline-none focus:border-sky-500 focus:ring-sky-500 sm:text-sm focus:ring-1" type="password" id="password_confirm" name="password_confirm" placeholder="비밀번호를 다시 입력해주세요"
                  v-model="password2"
                  >
                  <p class="text-xs italic text-red-500">{{ msgpassword2 }}</p>
                </div>
                <div class="flex items-center">
                  <input type="checkbox" id="remember_me" name="remember_me" class="w-4 h-4 text-blue-500 border border-gray-300 rounded focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50">
                  <span class="ml-2 text-sm font-medium" style="color: black;">개인정보 제공에 동의합니다</span>
                </div>
                <div>
                  <button type="submit" class="inline-flex items-center justify-center w-full px-4 py-3 space-x-2 font-semibold leading-6 text-white border rounded border-cyan-500 bg-cyan-500 focus:outline-none hover:text-white hover:bg-cyan-600 hover:border-cyan-600 focus:ring focus:ring-blue-500 focus:ring-opacity-50 active:bg-blue-700 active:border-blue-700">
                    Create Account
                  </button>
                  <div class="mt-4">
                    <router-link to="/login"><a href="#" class="inline-block text-sm font-medium text-blue-600 hover:text-blue-400">Return to Sign In</a></router-link>
                  </div>
                </div>
              </form>
            </section>
            <!-- END Sign Up Form -->
            
            <!-- END Sign Up Extra -->
            <div class="relative flex items-center px-6 py-10 bg-opacity-100 bg-cover md:px-10 lg:p-16 md:w-1/2" style="background-image: url('https://images.unsplash.com/photo-1485846234645-a62644f84728?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1459&q=80');">
              <div class="absolute inset-0 bg-opacity-50"></div>
              <div class="relative sm:text-left">
                <p class="mb-0 text-2xl font-semibold leading-relaxed text-white">
                  ssafy에서 다양한 영화 컨텐츠를
                </p>
                <p class="mt-0 mb-2 text-2xl font-semibold leading-relaxed text-white">
                  함께 확인해봐요!
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

<script>
import { mapActions, mapGetters } from 'vuex';

const accountsStore = 'accountsStore'

export default {
  name: "SignUpView",

  data() {
    return {
      username: "",
      nickname: "",
      password1: "",
      password2: "",
      msg: "",
      msgpassword1: "",
      msgpassword2: "",
    };
  },
  methods: {
    ...mapActions(accountsStore, ['signUp']),
  
  },
  computed: {
    ...mapGetters(accountsStore, ['usernames']),
    checkUserNames() {
      // return console.log(this.usernames);
      if (this.usernames.includes(this.username)) {
        return this.msg = "이미 존재하는 아이디입니다."
      } else {
        return this.msg = ""
      }
    },
    checkPasswordLength() {
      if (this.password1 && this.password1.length < 8) {
        return this.msgpassword1 = "비밀번호는 8자 이상이어야 합니다."
      } else{
        return this.msgpassword1 = ""
      }
    },
    checkPasswordMatch() {
      if (this.password2 && this.password1 !== this.password2) {
        return this.msgpassword2 = "비밀번호가 일치하지 않습니다."
      } else {
        return this.msgpassword2 = ""
      }
    }
  },
  created() {
    if (this.$store.getters[accountsStore + "/isLogin"]) {
      this.$router.push("/");
    }
  },

};
</script>

<style scoped>
#for_nav{
  position: absolute;
    top: 0;
    height: 100px;
    width: 100%;
    /* background-color: rgba(0, 0, 0, 0.2); */
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0));
}
</style>
