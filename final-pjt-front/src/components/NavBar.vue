

<template>
  <!-- Page Container -->
<div id="page-container" class="flex flex-col w-full min-h-screen mx-auto bg-gray-100">
  <!-- Page Header -->
  <header id="page-header" class="flex items-center flex-none bg-gray-800 z-1">
    <div class="container px-4 mx-auto xl:max-w-7xl lg:px-8">
      <div class="flex justify-between py-4">
        <!-- Left Section -->
        <div class="flex items-center space-x-2 lg:space-x-6">
          <!-- Logo -->
          <a href="javascript:void(0)" class="inline-flex items-center space-x-2 text-lg font-semibold tracking-wide text-gray-200 group hover:text-blue-300 active:text-gray-200">
            <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 text-blue-400 transition transform opacity-90 group-hover:scale-110 hi-solid hi-cube-transparent"><path fill-rule="evenodd" d="M9.504 1.132a1 1 0 01.992 0l1.75 1a1 1 0 11-.992 1.736L10 3.152l-1.254.716a1 1 0 11-.992-1.736l1.75-1zM5.618 4.504a1 1 0 01-.372 1.364L5.016 6l.23.132a1 1 0 11-.992 1.736L4 7.723V8a1 1 0 01-2 0V6a.996.996 0 01.52-.878l1.734-.99a1 1 0 011.364.372zm8.764 0a1 1 0 011.364-.372l1.733.99A1.002 1.002 0 0118 6v2a1 1 0 11-2 0v-.277l-.254.145a1 1 0 11-.992-1.736l.23-.132-.23-.132a1 1 0 01-.372-1.364zm-7 4a1 1 0 011.364-.372L10 8.848l1.254-.716a1 1 0 11.992 1.736L11 10.58V12a1 1 0 11-2 0v-1.42l-1.246-.712a1 1 0 01-.372-1.364zM3 11a1 1 0 011 1v1.42l1.246.712a1 1 0 11-.992 1.736l-1.75-1A1 1 0 012 14v-2a1 1 0 011-1zm14 0a1 1 0 011 1v2a1 1 0 01-.504.868l-1.75 1a1 1 0 11-.992-1.736L16 13.42V12a1 1 0 011-1zm-9.618 5.504a1 1 0 011.364-.372l.254.145V16a1 1 0 112 0v.277l.254-.145a1 1 0 11.992 1.736l-1.735.992a.995.995 0 01-1.022 0l-1.735-.992a1 1 0 01-.372-1.364z" clip-rule="evenodd"></path></svg>
            <span class="hidden sm:inline-block">Company</span>
          </a>
          <!-- END Logo -->

          <!-- Desktop Navigation -->
          <nav class="hidden lg:flex lg:items-center lg:space-x-2">
            <a href="javascript:void(0)" class="flex items-center px-3 py-2 space-x-2 text-sm font-medium text-white bg-gray-700 border border-gray-700 rounded">
              <span>Dashboard</span>
            </a>
            <a href="javascript:void(0)" class="flex items-center px-3 py-2 space-x-2 text-sm font-medium text-gray-300 border border-transparent rounded hover:text-white hover:bg-gray-700 hover:border-gray-700 active:bg-gray-600 active:border-gray-600">
              <span>Projects</span>
            </a>
            <a href="javascript:void(0)" class="flex items-center px-3 py-2 space-x-2 text-sm font-medium text-gray-300 border border-transparent rounded hover:text-white hover:bg-gray-700 hover:border-gray-700 active:bg-gray-600 active:border-gray-600">
              <span>Users</span>
            </a>
            <a href="javascript:void(0)" class="flex items-center px-3 py-2 space-x-2 text-sm font-medium text-gray-300 border border-transparent rounded hover:text-white hover:bg-gray-700 hover:border-gray-700 active:bg-gray-600 active:border-gray-600">
              <span>Invoices</span>
            </a>
          </nav>
          <!-- END Desktop Navigation -->
        </div>
        <!-- END Left Section -->

        <!-- Right Section -->
        <div class="flex items-center space-x-1 lg:space-x-2">
          <!-- Notifications -->
          <a href="javascript:void(0)" class="inline-flex items-center justify-center px-3 py-2 space-x-2 text-sm font-semibold leading-5 text-gray-200 bg-gray-700 border border-gray-900 rounded shadow-sm focus:outline-none hover:text-white hover:bg-opacity-50 hover:shadow focus:ring focus:ring-gray-500 focus:ring-opacity-25 active:bg-opacity-100 active:shadow-none">
            <svg stroke="currentColor" fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 hi-outline hi-bell"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>
          </a>
          <!-- END Notifications -->

          <!-- User Dropdown -->
          <div class="relative inline-block">
            <!-- Dropdown Toggle Button -->
            <button
              type="button"
              class="inline-flex items-center justify-center px-3 py-2 space-x-2 text-sm font-semibold leading-5 text-gray-200 bg-gray-700 border border-gray-900 rounded shadow-sm focus:outline-none hover:text-white hover:bg-opacity-50 hover:shadow focus:ring focus:ring-gray-500 focus:ring-opacity-25 active:bg-opacity-100 active:shadow-none"
              id="tk-dropdown-layouts-user"
              aria-haspopup="true"
              aria-expanded="true"
            >
              <span>John</span>
              <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-50 hi-solid hi-chevron-down"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
            </button>
            <!-- END Dropdown Toggle Button -->

            <!-- Dropdown -->
            <!-- 
              Visibility
                Closed        'hidden'
                Opened        '' (no class)

              Show/Hide with transitions
                enter         'transition ease-out duration-150'
                enter-start   'transform opacity-0 scale-75'
                enter-end     'transform opacity-100 scale-100'
                leave         'transition ease-in duration-100'
                leave-start   'transform opacity-100 scale-100'
                leave-end     'transform opacity-0 scale-75'
            -->
            <div role="menu" aria-labelledby="tk-dropdown-layouts-user" class="absolute right-0 w-48 mt-2 origin-top-right rounded shadow-xl">
              <div class="bg-white divide-y divide-gray-100 rounded ring-1 ring-black ring-opacity-5">
                <div class="p-2 space-y-1">
                  <a role="menuitem" href="javascript:void(0)" class="flex items-center px-3 py-2 space-x-2 text-sm font-medium text-gray-600 rounded hover:bg-gray-100 hover:text-gray-700 focus:outline-none focus:bg-gray-100 focus:text-gray-700">
                    <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-50 hi-solid hi-user-circle"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z" clip-rule="evenodd"></path></svg>
                    <span>Profile</span>
                  </a>
                  <a role="menuitem" href="javascript:void(0)" class="flex items-center px-3 py-2 space-x-2 text-sm font-medium text-gray-600 rounded hover:bg-gray-100 hover:text-gray-700 focus:outline-none focus:bg-gray-100 focus:text-gray-700">
                    <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-50 hi-solid hi-inbox"><path fill-rule="evenodd" d="M5 3a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2V5a2 2 0 00-2-2H5zm0 2h10v7h-2l-1 2H8l-1-2H5V5z" clip-rule="evenodd"></path></svg>
                    <span>Inbox</span>
                  </a>
                </div>
                <div class="p-2 space-y-1">
                  <a role="menuitem" href="javascript:void(0)" class="flex items-center px-3 py-2 space-x-2 text-sm font-medium text-gray-600 rounded hover:bg-gray-100 hover:text-gray-700 focus:outline-none focus:bg-gray-100 focus:text-gray-700">
                    <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-50 hi-solid hi-cog"><path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd"></path></svg>
                    <span>Settings</span>
                  </a>
                </div>
                <div class="p-2 space-y-1">
                  <form onsubmit="return false;">
                    <button type="submit" role="menuitem" class="flex items-center w-full px-3 py-2 space-x-2 text-sm font-medium text-left text-gray-600 rounded hover:bg-gray-100 hover:text-gray-700 focus:outline-none focus:bg-gray-100 focus:text-gray-700">
                      <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-50 hi-solid hi-lock-closed"><path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd"></path></svg>
                      <span>Sign out</span>
                    </button>
                  </form>
                </div>
              </div>
            </div>
            <!-- END Dropdown -->
          </div>
          <!-- END User Dropdown -->

          <!-- Toggle Mobile Navigation -->
          <div class="lg:hidden">
            <button type="button" class="inline-flex items-center justify-center px-3 py-2 space-x-2 text-sm font-semibold leading-5 text-gray-200 bg-gray-700 border border-gray-900 rounded shadow-sm focus:outline-none hover:text-white hover:bg-opacity-50 hover:shadow focus:ring focus:ring-gray-500 focus:ring-opacity-25 active:bg-opacity-100 active:shadow-none">
              <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 hi-solid hi-menu"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
            </button>
          </div>
          <!-- END Toggle Mobile Navigation -->
        </div>
        <!-- END Right Section -->
      </div>

      <!-- Mobile Navigation -->
      <!-- 
        Visibility
          Closed        'hidden'
          Opened        '' (no class)
      -->
      <div class="lg:hidden">
        <nav class="flex flex-col py-4 space-y-2 border-t border-gray-700">
          <a href="javascript:void(0)" class="flex items-center px-3 py-2 space-x-2 text-sm font-medium text-white bg-gray-700 border border-gray-700 rounded">
            <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-50 hi-solid hi-home"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path></svg>
            <span>Dashboard</span>
          </a>
          <a href="javascript:void(0)" class="flex items-center px-3 py-2 space-x-2 text-sm font-medium text-gray-300 border border-transparent rounded hover:text-white hover:bg-gray-700 hover:border-gray-700 active:bg-gray-600 active:border-gray-600">
            <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-50 hi-solid hi-briefcase"><path fill-rule="evenodd" d="M6 6V5a3 3 0 013-3h2a3 3 0 013 3v1h2a2 2 0 012 2v3.57A22.952 22.952 0 0110 13a22.95 22.95 0 01-8-1.43V8a2 2 0 012-2h2zm2-1a1 1 0 011-1h2a1 1 0 011 1v1H8V5zm1 5a1 1 0 011-1h.01a1 1 0 110 2H10a1 1 0 01-1-1z" clip-rule="evenodd"></path><path d="M2 13.692V16a2 2 0 002 2h12a2 2 0 002-2v-2.308A24.974 24.974 0 0110 15c-2.796 0-5.487-.46-8-1.308z"></path></svg>
            <span>Projects</span>
          </a>
          <a href="javascript:void(0)" class="flex items-center px-3 py-2 space-x-2 text-sm font-medium text-gray-300 border border-transparent rounded hover:text-white hover:bg-gray-700 hover:border-gray-700 active:bg-gray-600 active:border-gray-600">
            <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-50 hi-solid hi-users"><path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z"></path></svg>
            <span>Users</span>
          </a>
          <a href="javascript:void(0)" class="flex items-center px-3 py-2 space-x-2 text-sm font-medium text-gray-300 border border-transparent rounded hover:text-white hover:bg-gray-700 hover:border-gray-700 active:bg-gray-600 active:border-gray-600">
            <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 opacity-50 hi-solid hi-document-text"><path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z" clip-rule="evenodd"></path></svg>
            <span>Invoices</span>
          </a>
        </nav>
      </div>
      <!-- END Mobile Navigation -->
    </div>
  </header>
  <!-- END Page Header -->

  <!-- Page Content -->
  <main id="page-content" class="flex flex-col flex-auto max-w-full">
    <!-- Page Heading -->
    <div class="h-48 bg-gray-800">
      <div class="container px-4 mx-auto xl:max-w-7xl lg:px-8">
        <div class="flex items-center py-4 border-t border-gray-700">
          <div class="grow">
            <h1 class="text-2xl font-semibold text-gray-200">
              Dashboard
            </h1>
          </div>
          <div class="flex items-center justify-center flex-none px-2 py-3 space-x-2 rounded sm:justify-end sm:bg-transparent sm:px-0">
            <a href="javascript:void(0)" class="inline-flex items-center justify-center px-3 py-2 space-x-2 text-sm font-semibold leading-5 text-white bg-blue-700 border border-blue-700 rounded focus:outline-none hover:text-white hover:bg-blue-800 hover:border-blue-800 focus:ring focus:ring-blue-500 focus:ring-opacity-50 active:bg-blue-700 active:border-blue-700">
              <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 sm:opacity-50 hi-solid hi-plus"><path fill-rule="evenodd" d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z" clip-rule="evenodd"></path></svg>
              <span class="hidden sm:inline-block">New Project</span>
            </a>
          </div>
        </div>
      </div>
    </div>
    <!-- END Page Heading -->

    <!-- Page Section -->
    <div class="container p-4 mx-auto -mt-28 lg:-mt-32 xl:max-w-7xl lg:p-8">
      <div class="p-5 bg-white rounded shadow-sm lg:p-6">
        <!--

        ADD YOUR MAIN CONTENT BELOW

        -->

        
        <!-- Placeholder -->
        <div class="flex items-center justify-center py-64 text-gray-400 border-2 border-gray-200 border-dashed rounded-xl bg-gray-50">Content (max width 1280px)</div>

        
        <!--
        
        ADD YOUR MAIN CONTENT ABOVE
              
        -->
      </div>
    </div>
    <!-- END Page Section -->
  </main>
  <!-- END Page Content -->
</div>
<!-- END Page Container -->
</template>

<script setup>


</script>

<script>
export default {
  name: 'FinalPjtFrontNavBar',

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