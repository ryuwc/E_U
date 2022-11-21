<script setup></script>

<template>
  <!-- Page Container -->
  <div id="page-container" class="flex flex-col w-full min-h-screen mx-auto bg-gray-100">
    <!-- Page Content -->
    <main id="page-content" class="flex flex-col flex-auto max-w-full">
      <div class="relative flex items-center min-h-screen overflow-hidden bg-white">
        <!-- Left/Right Background -->
        <div class="absolute top-0 bottom-0 left-0 w-48 -ml-48 transform skew-x-6 bg-red-50 md:-ml-28"></div>
        <div class="absolute top-0 bottom-0 right-0 w-48 -mr-48 transform skew-x-6 bg-red-50 md:-mr-28"></div>
        <!-- END Left/Right Background -->
  
        <!-- Error Content -->
        <div class="container relative px-4 py-16 mx-auto space-y-10 text-center xl:max-w-7xl lg:px-8 lg:py-32">
          <div>
            <div class="relative inline-block mb-10 text-6xl font-extrabold md:text-9xl md:mb-20">
              <div class="absolute inset-0 border-4 border-red-50 animate-ping"></div>
              <span class="relative text-transparent bg-clip-text bg-gradient-to-r from-red-400 to-orange-500">
                404
              </span>
            </div>
            <h2 class="mb-4 text-3xl font-extrabold md:text-4xl">
              Page Not Found
            </h2>
            <h3 class="mx-auto text-lg font-medium text-gray-600 md:text-xl md:leading-relaxed lg:w-2/3">
              We are sorry but the page you are looking for was not found..
            </h3>
          </div>
          <router-link to="/home"  
          class="inline-flex items-center justify-center px-3 py-2 space-x-2 text-sm font-semibold leading-5 text-gray-800 bg-white border border-gray-300 rounded shadow-sm focus:outline-none hover:text-gray-800 hover:bg-gray-100 hover:border-gray-300 hover:shadow focus:ring focus:ring-gray-500 focus:ring-opacity-25 active:bg-white active:border-white active:shadow-none">
            <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-50 hi-solid hi-arrow-left"><path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clip-rule="evenodd"></path></svg>
            <span>Back to Home</span>
          </router-link>
        </div>
        <!-- END Error Content -->
      </div>
    </main>
    <!-- END Page Content -->
  </div>
  <!-- END Page Container -->
</template>

<script>
export default {
  name: 'NotPound404View',

  data() {
    return {
      
    };
  },

  mounted() {
    
  },

  methods: {
    
  },
};
</script>

<style scoped>

</style>