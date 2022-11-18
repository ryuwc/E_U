<script setup>
import { ref } from "vue";

const mobileNavOpen = ref(false);
</script>

<template>
  <!-- Main Header Section: With Mega Menu Alternate -->
  <div class="bg-white">
    <!-- Header -->
    <header id="page-header" class="flex items-center flex-none py-10 bg-white">
      <div class="container px-4 mx-auto xl:max-w-7xl lg:px-10">
        <div class="flex items-center justify-between">
          <!-- Logo -->
          <a href="#" class="inline-flex items-center space-x-2 text-lg font-bold tracking-wide text-blue-600 hover:text-blue-400">
            <svg stroke="currentColor" fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="inline-block w-6 h-6 opacity-75 hi-outline hi-cube-transparent"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 10l-2 1m0 0l-2-1m2 1v2.5M20 7l-2 1m2-1l-2-1m2 1v2.5M14 4l-2-1-2 1M4 7l2-1M4 7l2 1M4 7v2.5M12 21l-2-1m2 1l2-1m-2 1v-2.5M6 18l-2-1v-2.5M18 18l2-1v-2.5"></path></svg>
            <span>Company</span>
          </a>
          <!-- END Logo -->

          <!-- Mega Menu visible on large screens -->
          <ul class="items-center hidden lg:flex">
            <li class="relative group">
              <!-- Solutions Link -->
              <a href="#" class="inline-flex items-center h-8 px-4 space-x-1 font-semibold text-gray-900 group-hover:text-blue-500 hover:text-gray-500">
                <span>Solutions</span>
                <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-4 h-4 transition duration-200 ease-out transform opacity-50 group-hover:rotate-180 hi-solid hi-chevron-down"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
              </a>
              <!-- END Solutions Link -->

              <!-- Solutions Menu -->
              <div class="absolute invisible pt-8 -ml-48 w-96 top-8 left-1/2 z-1 group-hover:visible">
                <div class="overflow-hidden transition duration-300 ease-out origin-top transform scale-75 bg-white rounded-lg shadow-xl opacity-0 ring-1 ring-black ring-opacity-5 group-hover:opacity-100 group-hover:scale-100">
                  <div class="p-3 space-y-6 transition duration-500 ease-out transform scale-90 opacity-0 group-hover:opacity-100 group-hover:scale-100">
                    <h4 class="px-3 pt-3 text-xs font-semibold tracking-wider text-blue-800 uppercase">
                      Featured Products
                    </h4>
                    <nav class="flex flex-col space-y-1">
                      <a href="#" class="flex items-center p-3 space-x-3 text-sm font-medium text-gray-600 rounded-xl hover:text-blue-600 hover:bg-blue-50">
                        <div class="flex items-center justify-center flex-none w-16 h-16 bg-blue-100 rounded-3xl">
                          <div class="flex items-center justify-center w-12 h-12 transform bg-blue-500 rounded-2xl rotate-3">
                            <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 text-white hi-solid hi-code"><path fill-rule="evenodd" d="M12.316 3.051a1 1 0 01.633 1.265l-4 12a1 1 0 11-1.898-.632l4-12a1 1 0 011.265-.633zM5.707 6.293a1 1 0 010 1.414L3.414 10l2.293 2.293a1 1 0 11-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0zm8.586 0a1 1 0 011.414 0l3 3a1 1 0 010 1.414l-3 3a1 1 0 11-1.414-1.414L16.586 10l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                          </div>
                        </div>
                        <div class="space-y-1">
                          <h5 class="font-semibold">HTML Editor</h5>
                          <p class="opacity-75">
                            Write and manipulate your markup directly in your browser
                          </p>
                        </div>
                      </a>
                      <a href="#" class="flex items-center p-3 space-x-3 text-sm font-medium text-gray-600 rounded-xl hover:text-emerald-600 hover:bg-emerald-50">
                        <div class="flex items-center justify-center flex-none w-16 h-16 bg-emerald-100 rounded-3xl">
                          <div class="flex items-center justify-center w-12 h-12 transform bg-emerald-500 rounded-2xl rotate-3">
                            <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 text-white hi-solid hi-color-swatch"><path fill-rule="evenodd" d="M4 2a2 2 0 00-2 2v11a3 3 0 106 0V4a2 2 0 00-2-2H4zm1 14a1 1 0 100-2 1 1 0 000 2zm5-1.757l4.9-4.9a2 2 0 000-2.828L13.485 5.1a2 2 0 00-2.828 0L10 5.757v8.486zM16 18H9.071l6-6H16a2 2 0 012 2v2a2 2 0 01-2 2z" clip-rule="evenodd"></path></svg>
                          </div>
                        </div>
                        <div class="space-y-1">
                          <h5 class="font-semibold">CSS Editor</h5>
                          <p class="opacity-75">
                            Style your markup code with smart tools supporting Sass
                          </p>
                        </div>
                      </a>
                      <a href="#" class="flex items-center p-3 space-x-3 text-sm font-medium text-gray-600 rounded-xl hover:text-orange-600 hover:bg-orange-50">
                        <div class="flex items-center justify-center flex-none w-16 h-16 bg-orange-100 rounded-3xl">
                          <div class="flex items-center justify-center w-12 h-12 transform bg-orange-500 rounded-2xl rotate-3">
                            <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 text-white hi-solid hi-puzzle"><path d="M10 3.5a1.5 1.5 0 013 0V4a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-.5a1.5 1.5 0 000 3h.5a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-.5a1.5 1.5 0 00-3 0v.5a1 1 0 01-1 1H6a1 1 0 01-1-1v-3a1 1 0 00-1-1h-.5a1.5 1.5 0 010-3H4a1 1 0 001-1V6a1 1 0 011-1h3a1 1 0 001-1v-.5z"></path></svg>
                          </div>
                        </div>
                        <div class="space-y-1">
                          <h5 class="font-semibold">Web Page Builder</h5>
                          <p class="opacity-75">
                            Explore all available components and build your website
                          </p>
                        </div>
                      </a>
                    </nav>
                  </div>
                </div>
              </div>
              <!-- END Solutions Menu -->
            </li>
            <li class="relative group">
              <!-- Developers Link -->
              <a href="#" class="inline-flex items-center h-8 px-4 space-x-1 font-semibold text-gray-900 group-hover:text-blue-500 hover:text-gray-500">
                <span>Developers</span>
                <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-4 h-4 transition duration-200 ease-out transform opacity-50 group-hover:rotate-180 hi-solid hi-chevron-down"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
              </a>
              <!-- END Developers Link -->

              <!-- Developers Menu -->
              <div class="absolute invisible pt-8 -ml-48 w-96 top-8 left-1/2 z-1 group-hover:visible">
                <div class="overflow-hidden transition duration-300 ease-out origin-top transform scale-75 bg-white rounded-lg shadow-xl opacity-0 ring-1 ring-black ring-opacity-5 group-hover:opacity-100 group-hover:scale-100">
                  <div class="grid grid-cols-2 transition duration-500 ease-out transform scale-90 opacity-0 group-hover:opacity-100 group-hover:scale-100">
                    <div class="p-6 space-y-6">
                      <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                        Getting Started
                      </h4>
                      <nav class="flex flex-col space-y-3">
                        <a href="#" class="flex items-center space-x-2 text-sm font-medium text-gray-600 hover:text-blue-600">
                          <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-25 hi-solid hi-arrow-right"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                          <span>Installation</span>
                        </a>
                        <a href="#" class="flex items-center space-x-2 text-sm font-medium text-gray-600 hover:text-blue-600">
                          <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-25 hi-solid hi-cog"><path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd"></path></svg>
                          <span>Configuration</span>
                        </a>
                        <a href="#" class="flex items-center space-x-2 text-sm font-medium text-gray-600 hover:text-blue-600">
                          <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-25 hi-solid hi-view-boards"><path d="M2 4a1 1 0 011-1h2a1 1 0 011 1v12a1 1 0 01-1 1H3a1 1 0 01-1-1V4zM8 4a1 1 0 011-1h2a1 1 0 011 1v12a1 1 0 01-1 1H9a1 1 0 01-1-1V4zM15 3a1 1 0 00-1 1v12a1 1 0 001 1h2a1 1 0 001-1V4a1 1 0 00-1-1h-2z"></path></svg>
                          <span>Structure</span>
                        </a>
                        <a href="#" class="flex items-center space-x-2 text-sm font-medium text-gray-600 hover:text-blue-600">
                          <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-25 hi-solid hi-archive"><path d="M4 3a2 2 0 100 4h12a2 2 0 100-4H4z"></path><path fill-rule="evenodd" d="M3 8h14v7a2 2 0 01-2 2H5a2 2 0 01-2-2V8zm5 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
                          <span>Starter Kits</span>
                        </a>
                        <a href="#" class="flex items-center space-x-2 text-sm font-medium text-gray-600 hover:text-blue-600">
                          <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-25 hi-solid hi-server"><path fill-rule="evenodd" d="M2 5a2 2 0 012-2h12a2 2 0 012 2v2a2 2 0 01-2 2H4a2 2 0 01-2-2V5zm14 1a1 1 0 11-2 0 1 1 0 012 0zM2 13a2 2 0 012-2h12a2 2 0 012 2v2a2 2 0 01-2 2H4a2 2 0 01-2-2v-2zm14 1a1 1 0 11-2 0 1 1 0 012 0z" clip-rule="evenodd"></path></svg>
                          <span>Deployment</span>
                        </a>
                      </nav>
                    </div>
                    <div class="p-6 space-y-6">
                      <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                        The Basics
                      </h4>
                      <nav class="flex flex-col space-y-3">
                        <a href="#" class="flex items-center space-x-2 text-sm font-medium text-gray-600 hover:text-blue-600">
                          <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-25 hi-solid hi-arrows-expand"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8V4m0 0h4M3 4l4 4m8 0V4m0 0h-4m4 0l-4 4m-8 4v4m0 0h4m-4 0l4-4m8 4l-4-4m4 4v-4m0 4h-4"></path></svg>
                          <span>Routing</span>
                        </a>
                        <a href="#" class="flex items-center space-x-2 text-sm font-medium text-gray-600 hover:text-blue-600">
                          <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-25 hi-solid hi-paper-airplane"><path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z"></path></svg>
                          <span>Middleware</span>
                        </a>
                        <a href="#" class="flex items-center space-x-2 text-sm font-medium text-gray-600 hover:text-blue-600">
                          <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-25 hi-solid hi-chip"><path d="M13 7H7v6h6V7z"></path><path fill-rule="evenodd" d="M7 2a1 1 0 012 0v1h2V2a1 1 0 112 0v1h2a2 2 0 012 2v2h1a1 1 0 110 2h-1v2h1a1 1 0 110 2h-1v2a2 2 0 01-2 2h-2v1a1 1 0 11-2 0v-1H9v1a1 1 0 11-2 0v-1H5a2 2 0 01-2-2v-2H2a1 1 0 110-2h1V9H2a1 1 0 010-2h1V5a2 2 0 012-2h2V2zM5 5h10v10H5V5z" clip-rule="evenodd"></path></svg>
                          <span>Controllers</span>
                        </a>
                        <a href="#" class="flex items-center space-x-2 text-sm font-medium text-gray-600 hover:text-blue-600">
                          <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-25 hi-solid hi-chevron-double-up"><path fill-rule="evenodd" d="M4.293 15.707a1 1 0 010-1.414l5-5a1 1 0 011.414 0l5 5a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414 0zm0-6a1 1 0 010-1.414l5-5a1 1 0 011.414 0l5 5a1 1 0 01-1.414 1.414L10 5.414 5.707 9.707a1 1 0 01-1.414 0z" clip-rule="evenodd"></path></svg>
                          <span>Responses</span>
                        </a>
                        <a href="#" class="flex items-center space-x-2 text-sm font-medium text-gray-600 hover:text-blue-600">
                          <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-25 hi-solid hi-share"><path d="M15 8a3 3 0 10-2.977-2.63l-4.94 2.47a3 3 0 100 4.319l4.94 2.47a3 3 0 10.895-1.789l-4.94-2.47a3.027 3.027 0 000-.74l4.94-2.47C13.456 7.68 14.19 8 15 8z"></path></svg>
                          <span>Views</span>
                        </a>
                      </nav>
                    </div>
                  </div>
                </div>
              </div>
              <!-- END Developers Menu -->
            </li>
            <li class="relative group">
              <!-- Resources Link -->
              <a href="#" class="inline-flex items-center h-8 px-4 space-x-1 font-semibold text-gray-900 group-hover:text-blue-500 hover:text-gray-500">
                <span>Resources</span>
                <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-4 h-4 transition duration-200 ease-out transform opacity-50 group-hover:rotate-180 hi-solid hi-chevron-down"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
              </a>
              <!-- END Resources Link -->

              <!-- Resources Menu -->
              <div class="absolute invisible pt-8 -ml-48 w-96 top-8 left-1/2 z-1 group-hover:visible">
                <div class="overflow-hidden transition duration-300 ease-out origin-top transform scale-75 bg-white rounded-lg shadow-xl opacity-0 ring-1 ring-black ring-opacity-5 group-hover:opacity-100 group-hover:scale-100">
                  <div class="transition duration-500 ease-out transform scale-90 opacity-0 group-hover:opacity-100 group-hover:scale-100">
                    <div class="grid grid-cols-2">
                      <div class="p-6 space-y-6">
                        <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                          Learn
                        </h4>
                        <nav class="flex flex-col space-y-3">
                          <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                            Resource Center
                          </a>
                          <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                            Developer
                          </a>
                          <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                            User Guides
                          </a>
                        </nav>
                      </div>
                      <div class="p-6 space-y-6">
                        <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                          Links
                        </h4>
                        <nav class="flex flex-col space-y-3">
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
                    </div>
                    <div class="grid grid-cols-2 bg-gray-50">
                      <nav class="flex flex-col p-6 space-y-4">
                        <a href="#" class="flex items-center space-x-2 text-sm font-semibold text-gray-600 hover:text-blue-600">
                          <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-25 hi-solid hi-beaker"><path fill-rule="evenodd" d="M7 2a1 1 0 00-.707 1.707L7 4.414v3.758a1 1 0 01-.293.707l-4 4C.817 14.769 2.156 18 4.828 18h10.343c2.673 0 4.012-3.231 2.122-5.121l-4-4A1 1 0 0113 8.172V4.414l.707-.707A1 1 0 0013 2H7zm2 6.172V4h2v4.172a3 3 0 00.879 2.12l1.027 1.028a4 4 0 00-2.171.102l-.47.156a4 4 0 01-2.53 0l-.563-.187a1.993 1.993 0 00-.114-.035l1.063-1.063A3 3 0 009 8.172z" clip-rule="evenodd"></path></svg>
                          <span>API Reference</span>
                        </a>
                        <a href="#" class="flex items-center space-x-2 text-sm font-semibold text-gray-600 hover:text-blue-600">
                          <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-25 hi-solid hi-document"><path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clip-rule="evenodd"></path></svg>
                          <span>Documentation</span>
                        </a>
                      </nav>
                      <nav class="flex flex-col p-6 space-y-4">
                        <a href="#" class="flex items-center space-x-2 text-sm font-semibold text-gray-600 hover:text-blue-600">
                          <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-25 hi-solid hi-support"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-2 0c0 .993-.241 1.929-.668 2.754l-1.524-1.525a3.997 3.997 0 00.078-2.183l1.562-1.562C15.802 8.249 16 9.1 16 10zm-5.165 3.913l1.58 1.58A5.98 5.98 0 0110 16a5.976 5.976 0 01-2.516-.552l1.562-1.562a4.006 4.006 0 001.789.027zm-4.677-2.796a4.002 4.002 0 01-.041-2.08l-.08.08-1.53-1.533A5.98 5.98 0 004 10c0 .954.223 1.856.619 2.657l1.54-1.54zm1.088-6.45A5.974 5.974 0 0110 4c.954 0 1.856.223 2.657.619l-1.54 1.54a4.002 4.002 0 00-2.346.033L7.246 4.668zM12 10a2 2 0 11-4 0 2 2 0 014 0z" clip-rule="evenodd"></path></svg>
                          <span>Support</span>
                        </a>
                        <a href="#" class="flex items-center space-x-2 text-sm font-semibold text-gray-600 hover:text-blue-600">
                          <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-25 hi-solid hi-chat-alt"><path fill-rule="evenodd" d="M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z" clip-rule="evenodd"></path></svg>
                          <span>Help Forum</span>
                        </a>
                      </nav>
                    </div>
                  </div>
                </div>
              </div>
              <!-- END Resources Menu -->
            </li>
            <li class="relative group">
              <a href="#" class="inline-flex items-center h-8 px-4 space-x-1 font-semibold text-gray-900 group-hover:text-blue-500 hover:text-gray-500">
                <span>Pricing</span>
              </a>
            </li>
            <li class="relative group">
              <a href="#" class="inline-flex items-center h-8 px-4 space-x-1 font-semibold text-gray-900 group-hover:text-blue-500 hover:text-gray-500">
                <span>About</span>
              </a>
            </li>
          </ul>
          <!-- END Mega Menu visible on large screens -->

          <!-- Actions -->
          <div class="flex items-center justify-center space-x-1 lg:hidden sm:space-x-2">
            <!-- Toggle Button for navigation on smaller screens -->
            <button
              type="button"
              class="inline-flex items-center justify-center px-3 py-2 space-x-2 font-semibold leading-6 text-white bg-blue-700 border border-blue-700 rounded focus:outline-none hover:text-white hover:bg-blue-800 hover:border-blue-800 focus:ring focus:ring-blue-500 focus:ring-opacity-50 active:bg-blue-700 active:border-blue-700"
              @click="mobileNavOpen = !mobileNavOpen"
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
          <div class="grid grid-cols-1 mt-5 border sm:grid-cols-3 rounded-xl">
            <div class="col-span-2 p-3 space-y-6">
              <h4 class="px-3 pt-3 text-xs font-semibold tracking-wider text-blue-800 uppercase">
                Featured Products
              </h4>
              <nav class="flex flex-col space-y-1">
                <a href="#" class="flex items-center p-3 space-x-3 text-sm font-medium text-gray-600 rounded-xl hover:text-blue-600 hover:bg-blue-50">
                  <div class="flex items-center justify-center flex-none w-16 h-16 bg-blue-100 rounded-3xl">
                    <div class="flex items-center justify-center w-12 h-12 transform bg-blue-500 rounded-2xl rotate-3">
                      <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 text-white hi-solid hi-code"><path fill-rule="evenodd" d="M12.316 3.051a1 1 0 01.633 1.265l-4 12a1 1 0 11-1.898-.632l4-12a1 1 0 011.265-.633zM5.707 6.293a1 1 0 010 1.414L3.414 10l2.293 2.293a1 1 0 11-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0zm8.586 0a1 1 0 011.414 0l3 3a1 1 0 010 1.414l-3 3a1 1 0 11-1.414-1.414L16.586 10l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                    </div>
                  </div>
                  <div class="space-y-1">
                    <h5 class="font-semibold">HTML Editor</h5>
                    <p class="opacity-75">
                      Write and manipulate your markup directly in your browser
                    </p>
                  </div>
                </a>
                <a href="#" class="flex items-center p-3 space-x-3 text-sm font-medium text-gray-600 rounded-xl hover:text-emerald-600 hover:bg-emerald-50">
                  <div class="flex items-center justify-center flex-none w-16 h-16 bg-emerald-100 rounded-3xl">
                    <div class="flex items-center justify-center w-12 h-12 transform bg-emerald-500 rounded-2xl rotate-3">
                      <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 text-white hi-solid hi-color-swatch"><path fill-rule="evenodd" d="M4 2a2 2 0 00-2 2v11a3 3 0 106 0V4a2 2 0 00-2-2H4zm1 14a1 1 0 100-2 1 1 0 000 2zm5-1.757l4.9-4.9a2 2 0 000-2.828L13.485 5.1a2 2 0 00-2.828 0L10 5.757v8.486zM16 18H9.071l6-6H16a2 2 0 012 2v2a2 2 0 01-2 2z" clip-rule="evenodd"></path></svg>
                    </div>
                  </div>
                  <div class="space-y-1">
                    <h5 class="font-semibold">CSS Editor</h5>
                    <p class="opacity-75">
                      Style your markup code with smart tools supporting Sass
                    </p>
                  </div>
                </a>
                <a href="#" class="flex items-center p-3 space-x-3 text-sm font-medium text-gray-600 rounded-xl hover:text-orange-600 hover:bg-orange-50">
                  <div class="flex items-center justify-center flex-none w-16 h-16 bg-orange-100 rounded-3xl">
                    <div class="flex items-center justify-center w-12 h-12 transform bg-orange-500 rounded-2xl rotate-3">
                      <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 text-white hi-solid hi-puzzle"><path d="M10 3.5a1.5 1.5 0 013 0V4a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-.5a1.5 1.5 0 000 3h.5a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-.5a1.5 1.5 0 00-3 0v.5a1 1 0 01-1 1H6a1 1 0 01-1-1v-3a1 1 0 00-1-1h-.5a1.5 1.5 0 010-3H4a1 1 0 001-1V6a1 1 0 011-1h3a1 1 0 001-1v-.5z"></path></svg>
                    </div>
                  </div>
                  <div class="space-y-1">
                    <h5 class="font-semibold">Web Page Builder</h5>
                    <p class="opacity-75">
                      Explore all available components and build your website
                    </p>
                  </div>
                </a>
              </nav>
            </div>
            <div class="p-6 space-y-6">
              <h4 class="text-xs font-semibold tracking-wider text-blue-800 uppercase">
                Learn
              </h4>
              <nav class="flex flex-col space-y-3">
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  Resource Center
                </a>
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  Developer
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
                <a href="#" class="text-sm font-medium text-gray-600 hover:text-blue-600">
                  About
                </a>
              </nav>
            </div>
          </div>
        </div>
        <!-- END Navigation on smaller screens -->
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
  <!-- END Main Header Section: With Mega Menu Alternate -->
</template>

<script>
export default {
  name: 'FinalPjtFrontTestView',

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