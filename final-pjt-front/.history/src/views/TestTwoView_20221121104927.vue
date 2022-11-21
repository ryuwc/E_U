<template>
    

      <!-- Item -->
      <div class="relative overflow-hidden bg-blue-900 rounded-lg group focus:outline-none focus:ring-4 focus:ring-blue-500 focus:ring-opacity-50 focus:ring-offset-2 focus-within:ring-4 focus-within:ring-blue-500 focus-within:ring-opacity-50 focus-within:ring-offset-2" tabindex="0">
        <img src="https://source.unsplash.com/Bkci_8qcdvQ/800x600" alt="Image 2">
        
        <!-- Item Overlay -->
        <div class="absolute inset-0 flex flex-col items-center justify-center transition duration-300 ease-out bg-blue-700 opacity-0 bg-opacity-80 group-hover:opacity-100 group-focus:opacity-100 group-focus-within:opacity-100">
          <div class="text-center">
            <h4 class="text-lg font-semibold text-white">
              Main Title
            </h4>
            <h5 class="mb-5 font-medium text-white text-opacity-80">
              Image Description
            </h5>
            <a href="javascript:void(0)" class="inline-flex items-center justify-center px-3 py-2 space-x-2 text-sm font-semibold leading-5 text-blue-800 bg-blue-200 border border-blue-200 rounded focus:outline-none hover:text-blue-800 hover:bg-blue-300 hover:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50 active:bg-blue-200 active:border-blue-200">
              <svg class="inline-block w-4 h-4 opacity-50 hi-solid hi-external-link" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M11 3a1 1 0 100 2h2.586l-6.293 6.293a1 1 0 101.414 1.414L15 6.414V9a1 1 0 102 0V4a1 1 0 00-1-1h-5z"></path><path d="M5 5a2 2 0 00-2 2v8a2 2 0 002 2h8a2 2 0 002-2v-3a1 1 0 10-2 0v3H5V7h3a1 1 0 000-2H5z"></path></svg>
              <span>More Info</span>
            </a>
          </div>
        </div>
        <!-- END Item Overlay -->
      </div>
      <!-- END Item -->

      
</template>

<script>
import axios from 'axios';

export default {
  name: 'TestView',

  data() {
    return {
      
    };
  },
  components: {
  },

  mounted() {
    
  },

  methods: {
    getPoster(moveId) {
      axios({
        url: `https://api.themoviedb.org/3/movie/${moveId}/images?api_key=0d169ae4fecc50f95828ef6ee1b664e9`
      })
      .then(response => {
        console.log(response.data)
      })
    }
  },
};
</script>

<style scoped>

</style>