<script setup></script>

<script setup></script>

<template>
  <!-- Hero Section: Colorful Top Gradient With Header Links -->
  <div class="relative overflow-hidden bg-white">
    <!-- Gradient Background -->
    <!-- <div class="absolute inset-0 flex">
      <div
        class="w-1/4 h-64 bg-gradient-to-r from-blue-400 to-violet-400"
      ></div>
      <div class="w-1/4 h-64 bg-gradient-to-r from-violet-400 to-red-400"></div>
      <div class="w-1/4 h-64 bg-gradient-to-r from-red-400 to-orange-400"></div>
      <div
        class="w-1/4 h-64 bg-gradient-to-r from-orange-400 to-amber-400"
      ></div>
    </div>
    <div class="absolute inset-0">
      <div class="h-64 bg-gradient-to-b from-transparent to-white"></div>
    </div> -->
    <!-- END Gradient Background -->

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
          <div class="flex items-center justify-center space-x-2">
            <a
              href="#"
              class="inline-flex items-center justify-center px-3 py-2 space-x-2 text-sm font-semibold leading-5 text-white bg-blue-700 border border-blue-700 rounded focus:outline-none hover:text-white hover:bg-blue-800 hover:border-blue-800 focus:ring focus:ring-blue-500 focus:ring-opacity-50 active:bg-blue-700 active:border-blue-700"
            >
              <svg
                class="inline-block w-4 h-4 opacity-50 hi-solid hi-shopping-cart"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M3 1a1 1 0 000 2h1.22l.305 1.222a.997.997 0 00.01.042l1.358 5.43-.893.892C3.74 11.846 4.632 14 6.414 14H15a1 1 0 000-2H6.414l1-1H14a1 1 0 00.894-.553l3-6A1 1 0 0017 3H6.28l-.31-1.243A1 1 0 005 1H3zM16 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM6.5 18a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"
                ></path>
              </svg>
              <span>Get Access</span>
            </a>
          </div>
          <!-- END Actions -->
        </div>
      </div>
    </header>
  </div>
    <!-- END Header -->
</template>

<script>
export default {
  name: "PracticeView",

  data() {
    return {};
  },

  mounted() {},

  methods: {},
};
</script>

<style scoped></style>
