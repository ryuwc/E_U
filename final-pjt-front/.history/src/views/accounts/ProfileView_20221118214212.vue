<script setup></script>

<template>
  <nav id="header" class="z-30 w-full py-1 mt-24 bg-white border-b border-blue-400 shadow-lg top-10">
      <div class="flex items-center justify-between w-full px-6 py-2 mt-0">
         <label for="menu-toggle" class="block cursor-pointer md:hidden">
            <svg class="text-blue-600 fill-current" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20">
               <title>menu</title>
               <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"></path>
            </svg>
         </label>
         <input class="hidden" type="checkbox" id="menu-toggle">
         
         <div class="order-3 hidden w-full md:flex md:items-center md:w-auto md:order-1" id="menu">
            <nav>
               <ul class="items-center justify-between pt-4 text-base text-blue-600 md:flex md:pt-0">
                  <li><a class="inline-block px-4 py-2 text-lg font-medium no-underline hover:text-black lg:-ml-2" href="#">Home</a></li>
                  <li><a class="inline-block px-4 py-2 text-lg font-medium no-underline hover:text-black lg:-ml-2" href="#">Products</a></li>
                  <li><a class="inline-block px-4 py-2 text-lg font-medium no-underline hover:text-black lg:-ml-2" href="#">About</a></li>
               </ul>
            </nav>
         </div>
         
         <div class="flex flex-wrap items-center justify-end order-2 mr-0 md:order-3 md:mr-4" id="nav-content">
            <div class="flex items-center w-full auth md:w-full">
               <button class="p-2 mr-4 text-gray-800 bg-transparent border border-gray-300 rounded hover:bg-gray-100 hover:text-gray-700">Sign in</button>
               <button class="p-2 text-gray-200 bg-blue-600 rounded hover:bg-blue-500 hover:text-gray-100">Sign up</button>
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

#_body {
  height: 2500px;
}


.dropdown:focus-within .dropdown-menu {
  opacity:1;
  transform: translate(0) scale(1);
  visibility: visible;
}
</style>
