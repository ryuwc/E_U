<template>
  <div>
    <!-- <div class="flex items-center">
      <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 hi-solid hi-star">
        <path
          fill-rule="evenodd"
          d="M10 2.5l2.928 5.364 6.072.866-4.428 4.286 1.072 6.07L10 14.93 4.5 18l1.072-6.07L0 7.23l6.072-.866L10 2.5z"
          clip-rule="evenodd"
        ></path>
        >
        <path
          d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
        ></path>
      </svg>
      <p class="ml-2 text-sm font-bold text-gray-900 dark:text-white">4.95</p>
      <span class="w-1 h-1 mx-1.5 bg-gray-500 rounded-full dark:bg-gray-400"></span>
      <a href="#" class="text-sm font-medium text-gray-900 underline hover:no-underline dark:text-white">73 reviews</a>
    </div> -->
    
    <div class="flex justify-center mb-2">
      <a href="#_" @click.prevent="currentTab = 'MovieReview'" class="px-5 py-2.5 text-black font-medium mx-2 bg-blue-50 hover:bg-blue-100 hover:text-blue-600 text-blue-500 rounded-lg text-sm">리뷰</a>
      <a href="#_" @click.prevent="currentTab = 'MovieClip'" class="px-5 py-2.5 text-black font-medium mx-2 bg-blue-50 hover:bg-blue-100 hover:text-blue-600 text-blue-500 rounded-lg text-sm">무비 클립</a>
      <!-- <button @click="currentTab = 'MovieReview'">리뷰 및 평점</button>
      <button @click="currentTab = 'MovieClip'">무비 클립</button> -->
    </div>
    <component :is="currentTabComponent"></component>
  </div>
</template>

<script>
import MovieReview from '@/components/MovieReview.vue';
import MovieClip from '@/components/MovieClip';
export default {
  name: 'MovieDetailR',
  components: {
    MovieReview,
    MovieClip,
  },
  data() {
    return {
      currentTab: 'MovieReview',
    };
  },
  computed: {
    currentTabComponent() {
      return this.currentTab;
    },
  },
};
</script>

<style></style>
