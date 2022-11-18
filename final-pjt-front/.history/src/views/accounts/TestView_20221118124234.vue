<template>
  <div>
    <!-- component -->

    <div class="container max-w-full px-6 mx-auto md:py-24">
      <div class="max-w-sm px-6 mx-auto">
        <div class="relative flex flex-wrap">
          <div class="relative w-full">
            <div class="md:mt-6">
              <div class="font-semibold text-center text-black">
                Lorem ipsum dolor
              </div>
              <div class="text-center text-black font-base">
                Sed ut perspiciatis unde?
              </div>
              <form class="mt-8" x-data="{password: '',password_confirm: ''}">
                <div class="max-w-lg mx-auto">
                  <div class="py-1">
                    <span class="px-1 text-sm text-gray-600">Username</span>
                    <input
                      placeholder=""
                      type="text"
                      class="block w-full px-3 py-2 placeholder-gray-600 bg-white border-2 border-gray-300 rounded-lg shadow-md text-md focus:placeholder-gray-500 focus:bg-white focus:border-gray-600 focus:outline-none"
                    />
                  </div>
                  <div class="py-1">
                    <span class="px-1 text-sm text-gray-600">Email</span>
                    <input
                      placeholder=""
                      type="email"
                      class="block w-full px-3 py-2 placeholder-gray-600 bg-white border-2 border-gray-300 rounded-lg shadow-md text-md focus:placeholder-gray-500 focus:bg-white focus:border-gray-600 focus:outline-none"
                    />
                  </div>
                  <div class="py-1">
                    <span class="px-1 text-sm text-gray-600">Password</span>
                    <input
                      placeholder=""
                      type="password"
                      x-model="password"
                      class="block w-full px-3 py-2 placeholder-gray-600 bg-white border-2 border-gray-300 rounded-lg shadow-md text-md focus:placeholder-gray-500 focus:bg-white focus:border-gray-600 focus:outline-none"
                    />
                  </div>
                  <div class="py-1">
                    <span class="px-1 text-sm text-gray-600"
                      >Password Confirm</span
                    >
                    <input
                      placeholder=""
                      type="password"
                      x-model="password_confirm"
                      class="block w-full px-3 py-2 placeholder-gray-600 bg-white border-2 border-gray-300 rounded-lg shadow-md text-md focus:placeholder-gray-500 focus:bg-white focus:border-gray-600 focus:outline-none"
                    />
                  </div>
                  <div class="flex justify-start p-1 mt-3 ml-4">
                    <ul>
                      <li class="flex items-center py-1">
                        <div
                          :class="{
                            'bg-green-200 text-green-700':
                              password == password_confirm &&
                              password.length > 0,
                            'bg-red-200 text-red-700':
                              password != password_confirm ||
                              password.length == 0,
                          }"
                          class="p-1 rounded-full fill-current"
                        >
                          <svg
                            class="w-4 h-4"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              x-show="password == password_confirm && password.length > 0"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M5 13l4 4L19 7"
                            />
                            <path
                              x-show="password != password_confirm || password.length == 0"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M6 18L18 6M6 6l12 12"
                            />
                          </svg>
                        </div>
                        <span
                          :class="{
                            'text-green-700':
                              password == password_confirm &&
                              password.length > 0,
                            'text-red-700':
                              password != password_confirm ||
                              password.length == 0,
                          }"
                          class="ml-3 text-sm font-medium"
                          x-text="password == password_confirm && password.length > 0 ? 'Passwords match' : 'Passwords do not match' "
                        ></span>
                      </li>
                      <li class="flex items-center py-1">
                        <div
                          :class="{
                            'bg-green-200 text-green-700': password.length > 7,
                            'bg-red-200 text-red-700': password.length < 7,
                          }"
                          class="p-1 rounded-full fill-current"
                        >
                          <svg
                            class="w-4 h-4"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                          >
                            <path
                              x-show="password.length > 7"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M5 13l4 4L19 7"
                            />
                            <path
                              x-show="password.length < 7"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              stroke-width="2"
                              d="M6 18L18 6M6 6l12 12"
                            />
                          </svg>
                        </div>
                        <span
                          :class="{
                            'text-green-700': password.length > 7,
                            'text-red-700': password.length < 7,
                          }"
                          class="ml-3 text-sm font-medium"
                          x-text="password.length > 7 ? 'The minimum length is reached' : 'At least 8 characters required' "
                        ></span>
                      </li>
                    </ul>
                  </div>
                  <div class="flex justify-start">
                    <label
                      class="flex items-center block my-4 font-bold text-gray-500"
                    >
                      <input
                        class="top-0 leading-loose text-pink-600"
                        type="checkbox"
                      />
                      <span class="py-2 ml-2 text-sm text-left text-gray-600"
                        >Accept the
                        <a
                          href="#"
                          class="font-semibold text-black border-b-2 border-gray-200 hover:border-gray-500"
                        >
                          Terms and Conditions of the site </a
                        >and
                        <a
                          href="#"
                          class="font-semibold text-black border-b-2 border-gray-200 hover:border-gray-500"
                        >
                          the information data policy.</a
                        >
                      </span>
                    </label>
                  </div>
                  <button
                    class="block w-full px-6 py-3 mt-3 text-lg font-semibold text-white bg-gray-800 rounded-lg shadow-xl hover:text-white hover:bg-black"
                  >
                    Register
                  </button>
                </div>
              </form>

              <div
                class="flex justify-center block py-6 text-sm font-semibold sm:hidden"
              >
                <a
                  href="#"
                  class="font-normal text-black border-b-2 border-gray-200 hover:border-teal-500"
                  >You're already member?
                  <span class="font-semibold text-black"> Login </span>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.js" defer></script>
<script>
export default {
  name: "FinalPjtFrontTestView",

  data() {
    return {};
  },

  mounted() {},

  methods: {},
};
</script>

<style scoped></style>
