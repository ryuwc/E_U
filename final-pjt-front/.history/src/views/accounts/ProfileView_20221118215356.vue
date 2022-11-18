<script setup></script>

<template>
  <div class="relative overflow-hidden bg-white">
    <!-- Header -->
    <header
      id="page-header"
      style="height: 40px;"
      class="relative flex items-center flex-none py-5 bg-white shadow-sm bg-opacity-40"
    >
      <div
        class="container flex flex-col px-4 mx-auto space-y-6 text-center xl:max-w-7xl lg:px-10 md:flex-row md:items-center md:justify-between md:space-y-0 md:space-x-8"
      >
        <!-- Brand -->
        <div class="flex items-center justify-center flex-none">
          <a
            href="#"
            class="inline-flex items-center space-x-2 text-lg font-bold tracking-wide text-blue-900 hover:text-blue-700"
          >
            <svg
              class="inline-block w-5 h-5 text-blue-500 hi-solid hi-fire"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z"
                clip-rule="evenodd"
              ></path>
            </svg>
            <span>App</span>
          </a>
        </div>
        <!-- END Brand -->

        <div
          class="flex flex-col space-y-6 text-center grow md:flex-row md:items-center md:justify-between md:space-y-0 md:space-x-8"
        >
          <!-- Navigation -->
          <nav class="space-x-3 md:space-x-6">
            <a
              href="#"
              class="text-sm font-semibold text-blue-900 hover:text-blue-700"
            >
              <span>Dashboard</span>
            </a>
            <a
              href="#"
              class="text-sm font-semibold text-blue-900 hover:text-blue-700"
            >
              <span>Features</span>
            </a>
            <a
              href="#"
              class="text-sm font-semibold text-blue-900 hover:text-blue-700"
            >
              <span>Blog</span>
            </a>
          </nav>
          <!-- END Navigation -->

          <!-- Actions -->
          <div class="flex flex-wrap items-center justify-end order-2 mr-0 md:order-3 md:mr-4" id="nav-content"
          v-if="!isLogin"
          >
            <div class="flex items-center w-full auth md:w-full">
               <button class="p-2 mr-4 text-gray-800 bg-transparent border-gray-300 border-none rounded hover:bg-gray-200 hover:text-gray-700">Sign in</button>
               <button class="p-2 text-gray-200 bg-blue-600 border-none rounded hover:bg-blue-500 hover:text-gray-100">Sign up</button>
            </div>
          </div>
          <!-- END Actions -->
        </div>
      </div>
    </header>
  </div>
    <!-- END Header -->
</template>







<script>
import { mapGetters } from 'vuex'

const accountsStore = "accountsStore";

export default {
  name: "ProfileView",
  data() {
    return {
      showMenu: false,
    };
  },
  methods: {
    toggleNavbar() {
      this.showMenu = !this.showMenu;
    },
  },
  components: {},
  computed: {
    // 유저 정보 가져오기
    ...mapGetters(accountsStore, ["user"]),
    // 로그인 여부 가져오기
    ...mapGetters(accountsStore, ["isLogin"]),
  }
};
</script>

<style scoped>

#_body {
  height: 2500px;
}


.dropdown:focus-within .dropdown-menu {
  opacity:1;
  transform: translate(0) scale(1);
  visibility: visible;
}
</style>
