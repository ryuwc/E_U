<template>
  <nav class="flex justify-between">
    <router-link to="/"><img class="w-10 h-auto pl-5" src="@/assets/logo.png" alt="logo"></router-link>
    <div
      class="flex flex-col"
    >
      <div class="flex items-center justify-center">
        <div class="relative inline-block text-left dropdown">
          <span class="rounded-md shadow-sm"
            ><button
              class="inline-flex justify-center w-full px-4 py-2 text-sm font-medium leading-5 text-gray-700 transition duration-150 ease-in-out bg-white border border-gray-300 rounded-md hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-50 active:text-gray-800"
              type="button"
              aria-haspopup="true"
              aria-expanded="true"
              aria-controls="headlessui-menu-items-117"
            >
              <span>Options</span>
              </button
          ></span>
          <div
            class="invisible transition-all duration-300 origin-top-right transform scale-95 -translate-y-2 opacity-0 dropdown-menu"
          >
            <div
              class="absolute right-0 w-56 mt-2 origin-top-right bg-white border border-gray-200 divide-y divide-gray-100 rounded-md shadow-lg outline-none"
              aria-labelledby="headlessui-menu-button-1"
              id="headlessui-menu-items-117"
              role="menu"
            >
              <div class="px-4 py-3">
                <p class="text-sm leading-5">Signed in as</p>
                <p class="text-sm font-medium leading-5 text-gray-900 truncate">
                  tom@example.com
                </p>
              </div>
              <div class="py-1">
                <a
                  href="javascript:void(0)"
                  tabindex="0"
                  class="flex justify-between w-full px-4 py-2 text-sm leading-5 text-left text-gray-700"
                  role="menuitem"
                  >Account settings</a
                >
                <a
                  href="javascript:void(0)"
                  tabindex="1"
                  class="flex justify-between w-full px-4 py-2 text-sm leading-5 text-left text-gray-700"
                  role="menuitem"
                  >Support</a
                >
                <span
                  role="menuitem"
                  tabindex="-1"
                  class="flex justify-between w-full px-4 py-2 text-sm leading-5 text-left text-gray-700 opacity-50 cursor-not-allowed"
                  aria-disabled="true"
                  >New feature (soon)</span
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
  </nav>
</template>

<script>
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
};
</script>

<style scoped>

nav {
  height: 2500px;
}


.dropdown:focus-within .dropdown-menu {
  opacity:1;
  transform: translate(0) scale(1);
  visibility: visible;
}
</style>
