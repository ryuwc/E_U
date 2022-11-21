<template>
  <!-- Item -->
  <div
    class="relative overflow-hidden bg-blue-900 rounded-lg group focus:outline-none focus:ring-4 focus:ring-blue-500 focus:ring-opacity-50 focus:ring-offset-2 focus-within:ring-4 focus-within:ring-blue-500 focus-within:ring-opacity-50 focus-within:ring-offset-2"
    tabindex="0"
  >
    <img src="https://source.unsplash.com/Bkci_8qcdvQ/800x600" alt="Image 2" />

    <!-- Item Overlay -->
    <div
      class="absolute inset-0 flex flex-col items-center justify-center transition duration-300 ease-out bg-blue-700 opacity-0 bg-opacity-80 group-hover:opacity-100 group-focus:opacity-100 group-focus-within:opacity-100"
    >
      <div class="text-center">
        <h4 class="text-lg font-semibold text-white">Main Title</h4>
        <h5 class="mb-5 font-medium text-white text-opacity-80">Image Description</h5>
        <a
          href="javascript:void(0)"
          class="inline-flex items-center justify-center px-3 py-2 space-x-2 text-sm font-semibold leading-5 text-blue-800 bg-blue-200 border border-blue-200 rounded focus:outline-none hover:text-blue-800 hover:bg-blue-300 hover:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50 active:bg-blue-200 active:border-blue-200"
        >
          <svg class="inline-block w-4 h-4 opacity-50 hi-solid hi-external-link" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path d="M11 3a1 1 0 100 2h2.586l-6.293 6.293a1 1 0 101.414 1.414L15 6.414V9a1 1 0 102 0V4a1 1 0 00-1-1h-5z"></path>
            <path d="M5 5a2 2 0 00-2 2v8a2 2 0 002 2h8a2 2 0 002-2v-3a1 1 0 10-2 0v3H5V7h3a1 1 0 000-2H5z"></path>
          </svg>
          <span>More Info</span>
        </a>
        <div
          class="fixed top-0 left-0 hidden w-full h-full overflow-x-hidden overflow-y-auto outline-none modal fade"
          id="exampleModal"
          tabindex="-1"
          aria-labelledby="exampleModalLabel"
          aria-hidden="true"
        >
          <div class="relative w-auto pointer-events-none modal-dialog">
            <div
              class="relative flex flex-col w-full text-current bg-white border-none rounded-md shadow-lg outline-none pointer-events-auto modal-content bg-clip-padding"
            >
              <div class="flex items-center justify-between flex-shrink-0 p-4 border-b border-gray-200 modal-header rounded-t-md">
                <h5 class="text-xl font-medium leading-normal text-gray-800" id="exampleModalLabel">Modal title</h5>
                <button
                  type="button"
                  class="box-content w-4 h-4 p-1 text-black border-none rounded-none opacity-50 btn-close focus:shadow-none focus:outline-none focus:opacity-100 hover:text-black hover:opacity-75 hover:no-underline"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></button>
              </div>
              <div class="relative p-4 modal-body">Modal body text goes here.</div>
              <div class="flex flex-wrap items-center justify-end flex-shrink-0 p-4 border-t border-gray-200 modal-footer rounded-b-md">
                <button
                  type="button"
                  class="px-6 py-2.5 bg-purple-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-purple-700 hover:shadow-lg focus:bg-purple-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-purple-800 active:shadow-lg transition duration-150 ease-in-out"
                  data-bs-dismiss="modal"
                >
                  Close
                </button>
                <button
                  type="button"
                  class="px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out ml-1"
                >
                  Save changes
                </button>
              </div>
            </div>
          </div>
        </div>
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
    return {};
  },
  components: {},

  mounted() {},

  methods: {
    getPoster(moveId) {
      axios({
        url: `https://api.themoviedb.org/3/movie/${moveId}/images?api_key=0d169ae4fecc50f95828ef6ee1b664e9`,
      }).then((response) => {
        console.log(response.data);
      });
    },
  },
};
</script>

<style scoped></style>
