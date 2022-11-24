<script setup></script>

<template>
  <!-- Team Section: Vertical Photos with Asymmetrical Alignment -->
  <div class="bg-white">
    <div class="container w-full px-4 py-16 mx-auto space-y-16 lg:px-8 lg:py-32">
      <!-- Heading -->
      <div class="text-center">
        <h2 class="mb-4 text-3xl font-extrabold md:text-4xl">
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-500 via-pink-500 to-rose-500">이:유에서 최신 영화를 살펴봐요!</span>
        </h2>
        <h3 class="mx-auto text-lg font-medium text-gray-600 md:text-xl md:leading-relaxed lg:w-2/3"></h3>
      </div>
      <!-- END Heading -->

      <VueSlickCarousel
        ref="slick"
        :options="slickOptions"
        @beforeChange="beforeChange"
        @afterChange="afterChange"
      >
      <!-- 이거 하나씩 시작 -->
      <div style="width: 20vw; height: 20vw;" class="relative overflow-hidden rounded-lg shadow-lg group rotate-1">
        <div class="absolute inset-0 flex items-end justify-center p-4 text-white bg-gradient-to-t from-black/90 via-transparent z-1">
          <div class="text-center">
            <h4 class="mb-1 text-xl font-semibold">Irma Norton</h4>
            <p class="mb-3 font-medium text-gray-300">Founder &amp; CEO</p>
          </div>
        </div>
        <div style="width: 20vw; height: 20vw;" class="w-64 transition duration-150 ease-out bg-cover h-60 group-hover:scale-110">
          <img class="w-full h-auto" src="https://source.unsplash.com/nHoaFkrJEx4/600x800" alt="User Avatar" />
        </div>
      </div>
      <!-- 이거 하나씩 끝 -->
      
      </VueSlickCarousel>
      <div class="text-center">
        <a
          href="#"
          class="inline-flex items-center justify-center px-4 py-3 space-x-2 font-semibold leading-6 text-white bg-gray-700 border border-gray-700 rounded focus:outline-none hover:text-white hover:bg-gray-800 hover:border-gray-800 focus:ring focus:ring-gray-500 focus:ring-opacity-50 active:bg-gray-700 active:border-gray-700"
        >
          Join our team today
        </a>
      </div>
      
    </div>
  </div>
  <!-- END Team Section: Vertical Photos with Asymmetrical Alignment -->
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";

import { mapGetters } from 'vuex';
const moviesStore = 'moviesStore';

export default {
  name: 'NowMoviesView',
  components: {
    VueSlickCarousel,
  },
  data() {
    return {};
  },
  computed: {
    ...mapGetters(moviesStore, ['nowmovies']),
  },

  mounted() {},

  methods: {},
};
</script>

<style scoped></style>
