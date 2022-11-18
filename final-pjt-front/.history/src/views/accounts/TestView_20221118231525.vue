<!-- 네브바 연습 1  -->
<template>
  <nav class="flex justify-between">
    <div class="relative overflow-hidden bg-white">
      <!-- Header -->
      <header
        id="page-header"
        style="height: 40px"
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

            <!-- END Actions -->
          </div>
        </div>
      </header>
    </div>
    <!-- END Header -->

    <!-- 로그인, 회원가입 버튼 시작 -->
    <div
      class="flex flex-wrap items-center justify-end order-2 mr-0 md:order-3 md:mr-4"
      id="nav-content"
      v-if="!isLogin"
    >
      <div class="flex items-center w-full auth md:w-full">
        <button
          class="p-2 mr-4 text-gray-800 bg-transparent border-gray-300 border-none rounded hover:bg-gray-200 hover:text-gray-700"
        >
          Sign in
        </button>
        <button
          class="p-2 text-gray-200 bg-blue-600 border-none rounded hover:bg-blue-500 hover:text-gray-100"
        >
          Sign up
        </button>
      </div>
    </div>
    <!-- 로그인, 회원가입 버튼 끝 -->
    
    <!-- 프로필 이미지 영역 시작 -->
    <div v-if="isLogin" class="flex flex-col pt-5 pr-5">
      <div class="flex items-center justify-center">
        <div class="relative inline-block text-left dropdown">
          <button class="bg-white border-none">
            <img
              class="w-12"
              src="data:image/png;base64,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"
            />
          </button>
          <div
            class="invisible transition-all duration-300 origin-top-right transform scale-95 -translate-y-2 opacity-0 dropdown-menu"
          >
            <div
              class="absolute right-0 mt-2 origin-top-right bg-white border border-gray-200 divide-y divide-gray-100 rounded-md shadow-lg outline-none w-44"
              aria-labelledby="headlessui-menu-button-1"
              id="headlessui-menu-items-117"
              role="menu"
            >
              <div class="py-1 hover:scale-110">
                <router-link to="/edit"
                  ><a
                    tabindex="0"
                    class="flex justify-between w-full px-4 py-2 text-sm leading-5 text-left text-gray-700"
                    role="menuitem"
                    >Account settings</a
                  ></router-link
                >
                <a
                  href="javascript:void(0)"
                  tabindex="1"
                  class="flex justify-between w-full px-4 py-2 text-sm leading-5 text-left text-gray-700"
                  role="menuitem"
                  >Support</a
                >
                <a
                  href="javascript:void(0)"
                  tabindex="2"
                  class="flex justify-between w-full px-4 py-2 text-sm leading-5 text-left text-gray-700"
                  role="menuitem"
                  >License</a
                >
              </div>
              <div class="py-1">
                <a
                  href="javascript:void(0)"
                  tabindex="3"
                  class="flex justify-between w-full px-4 py-2 text-sm leading-5 text-left text-gray-700"
                  role="menuitem"
                  >Sign out</a
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 프로필 이미지 영역 끝 -->
  </nav>
</template>

<script>
import { mapGetters } from "vuex";

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
  },
  created() {
  },
};
</script>

<style scoped>
#_body {
  height: 2500px;
}

.dropdown:focus-within .dropdown-menu {
  opacity: 1;
  transform: translate(0) scale(1);
  visibility: visible;
}
</style>
