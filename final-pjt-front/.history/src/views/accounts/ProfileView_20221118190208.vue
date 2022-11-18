<template>
  <!-- component -->
<div class="flex justify-center h-screen">
<div x-data="{ dropdownOpen: true }" class="relative my-32">
  <button @click="dropdownOpen = !dropdownOpen" class="relative z-10 block p-2 bg-white rounded-md focus:outline-none">
    <svg class="w-5 h-5 text-gray-800" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
      <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
    </svg>
  </button>

  <div x-show="dropdownOpen" @click="dropdownOpen = false" class="fixed inset-0 z-10 w-full h-full"></div>

  <div x-show="dropdownOpen" class="absolute right-0 z-20 w-48 py-2 mt-2 bg-white rounded-md shadow-xl">
    <a href="#" class="block px-4 py-2 text-sm text-gray-700 capitalize hover:bg-blue-500 hover:text-white">
      your profile
    </a>
    <a href="#" class="block px-4 py-2 text-sm text-gray-700 capitalize hover:bg-blue-500 hover:text-white">
      Your projects
    </a>
    <a href="#" class="block px-4 py-2 text-sm text-gray-700 capitalize hover:bg-blue-500 hover:text-white">
      Help
    </a>
    <a href="#" class="block px-4 py-2 text-sm text-gray-700 capitalize hover:bg-blue-500 hover:text-white">
      Settings
    </a>
    <a href="#" class="block px-4 py-2 text-sm text-gray-700 capitalize hover:bg-blue-500 hover:text-white">
      Sign Out
    </a>
  </div>
</div>
</div>
</template>

<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js" defer></script>
<script>

export default {
  name: "ProfileView",
  components: {
  },
};
</script>

<style></style>
