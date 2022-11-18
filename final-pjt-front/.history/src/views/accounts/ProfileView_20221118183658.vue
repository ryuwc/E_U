<script setup>
import { ref } from "vue";

const mobileNavOpen = ref(false);
</script>

<template>
  <!-- Main Header Section: With Mega Menu -->
  <div class="bg-white">
    <!-- Header -->
    <header id="page-header" class="flex items-center flex-none py-10 bg-white">
      <div class="container relative px-4 mx-auto xl:max-w-7xl lg:px-10">
        <div class="flex items-center justify-between">
          <!-- Logo -->
          <a href="#" class="inline-flex items-center space-x-2 text-lg font-bold tracking-wide text-blue-600 hover:text-blue-400">
            <svg stroke="currentColor" fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="inline-block w-6 h-6 opacity-75 hi-outline hi-cube-transparent"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 10l-2 1m0 0l-2-1m2 1v2.5M20 7l-2 1m2-1l-2-1m2 1v2.5M14 4l-2-1-2 1M4 7l2-1M4 7l2 1M4 7v2.5M12 21l-2-1m2 1l2-1m-2 1v-2.5M6 18l-2-1v-2.5M18 18l2-1v-2.5"></path></svg>
            <span>Company</span>
          </a>
          <!-- END Logo -->

          <!-- Mega Menu visible on large screens -->
          <ul class="items-center hidden lg:flex">
            <li class="group">
              <!-- Solutions Link -->
              <a href="#" class="inline-flex items-center h-8 px-4 space-x-1 font-semibold text-gray-900 group-hover:text-blue-500 hover:text-gray-500">
                <span>Solutions</span>
                <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-4 h-4 transition duration-200 ease-out transform opacity-50 group-hover:rotate-180 hi-solid hi-chevron-down"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
              </a>
              <!-- END Solutions Link -->

              <!-- Solutions Menu -->
              <div class="absolute invisible pt-8 top-8 right-10 left-10 z-1 group-hover:visible">
                <div class="overflow-hidden transition duration-300 ease-out origin-top transform scale-75 bg-white rounded-lg shadow-xl opacity-0 ring-1 ring-black ring-opacity-5 group-hover:opacity-100 group-hover:scale-100">
                  <div class="grid grid-cols-4 transition duration-500 ease-out transform scale-90 opacity-0 group-hover:opacity-100 group-hover:scale-100">
                    <div class="p-8 space-y-6">
                      <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                        Products
                      </h4>
                      <nav class="flex flex-col space-y-3">
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          HTML Editor
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          CSS Editor
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Web Page Builder
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Animations Pack
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          3D Web Studio
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Web Templates
                        </a>
                      </nav>
                    </div>
                    <div class="p-8 space-y-6">
                      <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                        Features
                      </h4>
                      <nav class="flex flex-col space-y-3">
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Overview
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Components
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Media Libraries
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Databases
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Auto Backups
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          24/7 Phone Support
                        </a>
                      </nav>
                    </div>
                    <div class="col-span-2 p-8 space-y-6 bg-gray-50">
                      <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                        From the blog
                      </h4>
                      <div class="grid grid-cols-2 gap-4 xl:gap-8">
                        <a href="#" class="block space-y-3 text-sm font-semibold transition-opacity hover:opacity-90 hover:text-blue-600">
                          <div class="p-2 bg-blue-100 rounded-2xl">
                            <img src="https://source.unsplash.com/8pb7Hq539Zw/300x180" alt="Preview Image" class="rounded-xl">
                          </div>
                          <h4>
                            How to create the best web apps online with our app
                          </h4>
                        </a>
                        <a href="#" class="block space-y-3 text-sm font-semibold transition-opacity hover:opacity-90 hover:text-blue-600">
                          <div class="p-2 bg-blue-100 rounded-2xl">
                            <img src="https://source.unsplash.com/TxXuh_hAFd8/300x180" alt="Preview Image" class="rounded-xl">
                          </div>
                          <h4>
                            Inspiring results from your first work week online
                          </h4>
                        </a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <!-- END Solutions Menu -->
            </li>
            <li class="group">
              <!-- Developers Link -->
              <a href="#" class="inline-flex items-center h-8 px-4 space-x-1 font-semibold text-gray-900 group-hover:text-blue-500 hover:text-gray-500">
                <span>Developers</span>
                <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-4 h-4 transition duration-200 ease-out transform opacity-50 group-hover:rotate-180 hi-solid hi-chevron-down"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
              </a>
              <!-- END Developers Link -->

              <!-- Developers Menu -->
              <div class="absolute invisible pt-8 top-8 right-10 left-10 z-1 group-hover:visible">
                <div class="overflow-hidden transition duration-300 ease-out origin-top transform scale-75 bg-white rounded-lg shadow-xl opacity-0 ring-1 ring-black ring-opacity-5 group-hover:opacity-100 group-hover:scale-100">
                  <div class="grid grid-cols-4 transition duration-500 ease-out transform scale-90 opacity-0 group-hover:opacity-100 group-hover:scale-100">
                    <div class="p-8 space-y-6">
                      <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                        Getting Started
                      </h4>
                      <nav class="flex flex-col space-y-3">
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Installation
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Configuration
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Structure
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Starter Kits
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Deployment
                        </a>
                      </nav>
                    </div>
                    <div class="p-8 space-y-6">
                      <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                        The Basics
                      </h4>
                      <nav class="flex flex-col space-y-3">
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Routing
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Middleware
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Controllers
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Responses
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Views
                        </a>
                      </nav>
                    </div>
                    <div class="p-8 space-y-6">
                      <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                        Database
                      </h4>
                      <nav class="flex flex-col space-y-3">
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Query Builder
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Pagination
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Migrations
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Seeding
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Redis
                        </a>
                      </nav>
                    </div>
                    <div class="p-8 space-y-6 bg-gray-50">
                      <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                        From the docs
                      </h4>
                      <a href="#" class="block space-y-3 text-sm font-semibold transition-opacity hover:opacity-90 hover:text-blue-600">
                        <div class="p-2 bg-blue-100 rounded-2xl">
                          <div class="py-8 text-center text-blue-500 bg-blue-200 rounded-xl">
                            <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-10 h-10 hi-solid hi-document-text"><path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z" clip-rule="evenodd"></path></svg>
                          </div>
                        </div>
                        <h4>
                          Getting started with ease
                        </h4>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
              <!-- END Developers Menu -->
            </li>
            <li class="group">
              <!-- Resources Link -->
              <a href="#" class="inline-flex items-center h-8 px-4 space-x-1 font-semibold text-gray-900 group-hover:text-blue-500 hover:text-gray-500">
                <span>Resources</span>
                <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-4 h-4 transition duration-200 ease-out transform opacity-50 group-hover:rotate-180 hi-solid hi-chevron-down"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
              </a>
              <!-- END Resources Link -->

              <!-- Resources Menu -->
              <div class="absolute invisible pt-8 top-8 right-10 left-10 z-1 group-hover:visible">
                <div class="overflow-hidden transition duration-300 ease-out origin-top transform scale-75 bg-white rounded-lg shadow-xl opacity-0 ring-1 ring-black ring-opacity-5 group-hover:opacity-100 group-hover:scale-100">
                  <div class="grid grid-cols-4 transition duration-500 ease-out transform scale-90 opacity-0 group-hover:opacity-100 group-hover:scale-100">
                    <div class="p-8 space-y-6">
                      <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                        Learn
                      </h4>
                      <nav class="flex flex-col space-y-3">
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Resource Center
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Developer Docs
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          User Guides
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Starters
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Video Library
                        </a>
                        <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                          Tutorials
                        </a>
                      </nav>
                    </div>
                    <div class="col-span-3 p-8 space-y-6 bg-gray-50">
                      <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                        From the blog
                      </h4>
                      <div class="grid grid-cols-3 gap-4 xl:gap-8">
                        <a href="#" class="block space-y-3 text-sm font-semibold transition-opacity hover:opacity-90 hover:text-emerald-600">
                          <div class="p-2 rounded-2xl bg-emerald-100">
                            <div class="py-10 text-center bg-emerald-200 text-emerald-500 rounded-xl">
                              <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-10 h-10 hi-solid hi-users"><path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z"></path></svg>
                            </div>
                          </div>
                          <h4>
                            How to work with your colleagues on the same app
                          </h4>
                        </a>
                        <a href="#" class="block space-y-3 text-sm font-semibold transition-opacity hover:opacity-90 hover:text-red-600">
                          <div class="p-2 bg-red-100 rounded-2xl">
                            <div class="py-10 text-center text-red-500 bg-red-200 rounded-xl">
                              <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-10 h-10 hi-solid hi-terminal"><path fill-rule="evenodd" d="M2 5a2 2 0 012-2h12a2 2 0 012 2v10a2 2 0 01-2 2H4a2 2 0 01-2-2V5zm3.293 1.293a1 1 0 011.414 0l3 3a1 1 0 010 1.414l-3 3a1 1 0 01-1.414-1.414L7.586 10 5.293 7.707a1 1 0 010-1.414zM11 12a1 1 0 100 2h3a1 1 0 100-2h-3z" clip-rule="evenodd"></path></svg>
                            </div>
                          </div>
                          <h4>
                            Most popular tips and tricks to integration with APIs
                          </h4>
                        </a>
                        <a href="#" class="block space-y-3 text-sm font-semibold transition-opacity hover:opacity-90 hover:text-orange-600">
                          <div class="p-2 bg-orange-100 rounded-2xl">
                            <div class="py-10 text-center text-orange-500 bg-orange-200 rounded-xl">
                              <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-10 h-10 hi-solid hi-puzzle"><path d="M10 3.5a1.5 1.5 0 013 0V4a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-.5a1.5 1.5 0 000 3h.5a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-.5a1.5 1.5 0 00-3 0v.5a1 1 0 01-1 1H6a1 1 0 01-1-1v-3a1 1 0 00-1-1h-.5a1.5 1.5 0 010-3H4a1 1 0 001-1V6a1 1 0 011-1h3a1 1 0 001-1v-.5z"></path></svg>
                            </div>
                          </div>
                          <h4>
                            How to put together the components to create your UI
                          </h4>
                        </a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <!-- END Resources Menu -->
            </li>
            <li class="group">
              <a href="#" class="inline-flex items-center h-8 px-4 space-x-1 font-semibold text-gray-900 group-hover:text-blue-500 hover:text-gray-500">
                <span>Pricing</span>
              </a>
            </li>
          </ul>
          <!-- END Mega Menu visible on large screens -->

          <!-- Actions -->
          <div class="flex items-center justify-center space-x-1 sm:space-x-2">
            <a href="#" class="inline-flex items-center justify-center px-3 py-2 space-x-2 text-sm font-semibold leading-5 text-white bg-blue-700 border border-blue-700 rounded focus:outline-none hover:text-white hover:bg-blue-800 hover:border-blue-800 focus:ring focus:ring-blue-500 focus:ring-opacity-50 active:bg-blue-700 active:border-blue-700">
              <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-50 hi-solid hi-login"><path fill-rule="evenodd" d="M3 3a1 1 0 011 1v12a1 1 0 11-2 0V4a1 1 0 011-1zm7.707 3.293a1 1 0 010 1.414L9.414 9H17a1 1 0 110 2H9.414l1.293 1.293a1 1 0 01-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg>
              <span>Sign In</span>
            </a>

            <!-- Toggle Button for navigation on smaller screens -->
            <button
              type="button"
              class="inline-flex items-center justify-center px-3 py-2 space-x-2 text-sm font-semibold leading-5 text-white bg-blue-700 border border-blue-700 rounded focus:outline-none lg:hidden hover:text-white hover:bg-blue-800 hover:border-blue-800 focus:ring focus:ring-blue-500 focus:ring-opacity-50 active:bg-blue-700 active:border-blue-700"
            >
              <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 hi-solid hi-menu"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
            </button>
            <!-- END Toggle Button for navigation on smaller screens -->
          </div>
          <!-- END Actions -->
        </div>

        <!-- Navigation on smaller screens -->
        <div
          class="lg:hidden"
          :class="{
            'hidden': !mobileNavOpen  
          }"
        >
          <div class="grid grid-cols-1 mt-5 sm:grid-cols-3 bg-gray-50 rounded-xl">
            <div class="p-8 space-y-6">
              <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                Solutions
              </h4>
              <nav class="flex flex-col space-y-3">
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  HTML Editor
                </a>
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  CSS Editor
                </a>
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  Web Page Builder
                </a>
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  Animations Pack
                </a>
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  3D Web Studio
                </a>
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  Web Templates
                </a>
              </nav>
            </div>
            <div class="p-8 space-y-6">
              <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                Developers
              </h4>
              <nav class="flex flex-col space-y-3">
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  Overview
                </a>
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  Components
                </a>
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  Media Libraries
                </a>
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  Databases
                </a>
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  Auto Backups
                </a>
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  24/7 Phone Support
                </a>
              </nav>
            </div>
            <div class="p-8 space-y-6">
              <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                Resources
              </h4>
              <nav class="flex flex-col space-y-3">
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  Resource Center
                </a>
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  Developer Docs
                </a>
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  User Guides
                </a>
              </nav>
              <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                More
              </h4>
              <nav class="flex flex-col space-y-3">
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  Pricing
                </a>
              </nav>
            </div>
          </div>
        </div>
        <!-- Navigation on smaller screens -->
      </div>
    </header>
    <!-- END Header -->

    <!--

    ADD YOUR HERO CONTENT BELOW

    -->

    
    <!-- Placeholder -->
    <div class="container px-4 pb-12 mx-auto xl:max-w-7xl lg:px-10"><div class="flex items-center justify-center py-64 text-gray-400 border-2 border-gray-200 border-dashed rounded-xl bg-gray-50">Hero Content</div></div>

    
    <!--
    
    ADD YOUR HERO CONTENT ABOVE
    
    -->
  </div>
  <!-- END Main Header Section: With Mega Menu -->
</template>

<script>

export default {
  name: "ProfileView",
  components: {
  },
};
</script>

<style></style>
