<script setup></script>

<template>
  <div class="bg-white">
    <div id="for_nav"></div>
    <div class="container px-4 py-16 mx-auto space-y-16 xl:max-w-7xl lg:px-8 lg:py-32">
      <div class="text-center">
        <h2 class="mb-4 text-3xl font-extrabold md:text-4xl">
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-500 via-pink-500 to-rose-500">이:유에서 최신 영화를 살펴봐요!</span>
        </h2>
      </div>
      

      <!-- 예비 후보 -->
      <!-- <div class="grid grid-cols-4">
        <MovieCard2
          class="col-span-1"
          v-for="(movie, index) in nowmovies"
          :key="index"
          :movie="movie"
        />
      </div> -->

      <!-- 영화 카드 시작 -->
      <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4 md:gap-16">
        <div class="relative overflow-hidden rounded-lg shadow-lg group rotate-1"
        v-for="(movie, index) in nowmovies"
        :key="index"
        :movie="movie"
        >
          <router-link :to="{ name:'MovieDetailInfoView', params: { id: movie.id } }">
            <div class="absolute inset-0 flex items-end justify-center p-4 text-white bg-gradient-to-t from-black/90 via-transparent z-1">
              <div class="text-center">
                <h4 class="mb-1 text-xl font-semibold">
                  {{ movie.title }}
                </h4>
                
              </div>
            </div>
            <img class="transition duration-150 ease-out aspect-w-3 aspect-h-4 group-hover:scale-110" style="width: 100%; height: 20vw;" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`">
          </router-link>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
// import VueSlickCarousel from 'vue-slick-carousel';
import 'vue-slick-carousel/dist/vue-slick-carousel.css';
// import MovieCard2 from '@/components/MovieCard2.vue';

import { mapGetters } from 'vuex';
const moviesStore = 'moviesStore';

export default {
  name: 'NowMoviesView',
  components: {
    // MovieCard2
    // VueSlickCarousel,
  },
  data() {
    return {
      settings: {
        dots: false,
        focusOnSelect: true,
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 3,
        touchThreshold: 5,
        centerPadding: '10%'
      },
    };
  },
  computed: {
    ...mapGetters(moviesStore, ['nowmovies']),
  },

  mounted() {},

  methods: {
    showNext() {
      this.$refs.carousel.next();
    },
    showPrev() {
      this.$refs.carousel.prev();
    },
  },
};
</script>

<style scoped>
#for_nav{
  position: absolute;
    top: 0;
    height: 100px;
    width: 100%;
    /* background-color: rgba(0, 0, 0, 0.2); */
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0));
}
</style>
