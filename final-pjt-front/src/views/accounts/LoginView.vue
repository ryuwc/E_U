<script setup></script>

<template>
  <!-- Page Container -->
  <div
    style="background-color: rgba(0, 0, 0, 0.1);"
    id="page-container"
    class="flex flex-col w-full h-screen mx-auto"
  >
  <div id="for_nav"></div>
    <!-- Page Content -->
    <main id="page-content" class="flex flex-col flex-auto max-w-full mt-40">
      <div
        class="flex items-center justify-center w-full p-4 py-0 mx-auto min-h-fit max-w-10xl lg:px-8"
      >
        <!-- Sign Up Section -->
        <div class="w-full max-w-5xl lg:py-16">
          <!-- Sign Up Box -->
          <div
            class="flex flex-col overflow-hidden shadow-sm md:flex-row rounded-xl"
          >
            <!-- Sign Up Form -->
            <section class="px-6 py-10 bg-white md:px-10 lg:p-16 md:w-1/2">
              <form
                class="space-y-6"
                @submit.prevent="
                  login({ username: username, password: password, uporin: false })
                "
              >
                <div class="space-y-1">
                  <input
                    class="block w-full px-3 py-2 leading-6 placeholder-gray-400 bg-white border rounded shadow-sm focus:outline-none focus:border-sky-500 focus:ring-sky-500 sm:text-sm focus:ring-1"
                    type="text"
                    id="name"
                    name="name"
                    placeholder="아이디를 입력해주세요"
                    v-model="username"
                  />
                  <p class="text-xs italic text-red-500">{{ msg }}</p>
                </div>
                <div class="space-y-1">
                  <input
                    class="block w-full px-3 py-2 leading-6 placeholder-gray-400 border rounded shadow-sm focus:outline-none focus:border-sky-500 focus:ring-sky-500 sm:text-sm focus:ring-1"
                    type="password"
                    id="password_confirm"
                    name="password"
                    placeholder="비밀번호 입력해주세요"
                    v-model="password"
                  />
                </div>
                <div class="flex items-center">
                  <input
                    type="checkbox"
                    id="remember_me"
                    name="remember_me"
                    class="w-4 h-4 text-blue-500 border border-gray-300 rounded focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
                  />
                  <span style="color: rgba(0, 0, 0, 0.4);" class="ml-2 text-sm font-semibold">Remember Me</span>
                </div>
                <div>
                  <button
                    type="submit"
                    class="inline-flex items-center justify-center w-full px-4 py-3 space-x-2 font-semibold leading-6 text-white border rounded border-cyan-500 bg-cyan-500 focus:outline-none hover:text-white hover:bg-cyan-600 hover:border-cyan-600 focus:ring focus:ring-blue-500 focus:ring-opacity-50 active:bg-blue-700 active:border-blue-700"
                  >
                    Sign In
                  </button>
                  <div class="mt-4">
                    <router-link to="/signup"
                      ><a
                        href="#"
                        class="inline-block text-sm font-medium text-blue-600 hover:text-blue-400"
                        >Return to Sign In</a
                      ></router-link
                    >
                  </div>
                </div>
              </form>
            </section>
            <!-- END Sign Up Form -->

            <!-- END Sign Up Extra -->
            <div
              class="relative flex items-center px-6 py-10 bg-opacity-100 bg-cover md:px-10 lg:p-16 md:w-1/2"
              style="
                background-image: url('https://images.unsplash.com/photo-1612635466104-e3aab50680b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80');
              "
            >
              <div class="absolute inset-0 bg-opacity-50"></div>
              <div class="relative text-center sm:text-left">
                <p
                  class="mb-0 text-2xl font-semibold leading-relaxed text-white h-44"
                ></p>
                <p class="text-sm font-medium text-white/75"></p>
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
import { mapActions, mapGetters } from "vuex";

const accountsStore = "accountsStore";

export default {
  name: "LoginView",

  data() {
    return {
      username: "",
      password: "",
      msg: "",
    };
  },
  methods: {
    ...mapActions(accountsStore, ["login"]),
    
  },
  computed: {
    ...mapGetters(accountsStore, ["usernames"]),
    checkInUserName() {
      if (this.username && !this.usernames.includes(this.username)) {
        return this.msg = "존재하지 않는 아이디입니다."
      } else {
        return this.msg = ""
      }
    },
  },
  created() {
    if (this.$store.getters[accountsStore + "/isLogin"]) {
      this.$router.push("/");
    }
  },
};
</script>

<style scoped>
template {
  background-color: #86888a;
}

#for_nav{
  position: absolute;
    top: 0;
    height: 100px;
    width: 100%;
    /* background-color: rgba(0, 0, 0, 0.2); */
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0));
}
</style>
