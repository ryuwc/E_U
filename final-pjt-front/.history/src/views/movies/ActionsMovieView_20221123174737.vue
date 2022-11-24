<script setup></script>

<template>
  <div class="bg-white">
    <div id="for_nav"></div>
    <div class="container px-4 py-16 mx-auto space-y-16 xl:max-w-7xl lg:px-8 lg:py-32">
      <div class="text-center">
        <h2 class="mb-4 text-3xl font-extrabold md:text-4xl">
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-500 via-pink-500 to-rose-500">화려한 연출과 타격감 넘치는 액션영화!</span>
        </h2>
      </div>
  
      <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4 md:gap-16">
        <div class="relative overflow-hidden rounded-lg shadow-lg group rotate-1"
        v-for="(movie, index) in actionMovies"
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
import _ from 'lodash';
import { mapGetters } from 'vuex';
const moviesStore = 'moviesStore';

window.addEventListener('scroll', function() {
      let value = window.screenY
      console.log('스크롤', value);
    });

export default {
  name: 'ActionsMovieView',

  data() {
    return {
      actionMovies: [],
    };
  },
  computed: {
    ...mapGetters(moviesStore, ['genre28']),
    
  },
  mounted() {
    this.getRandomMovies()
    
  },
  methods: {
    getRandomMovies() {
      const movies = this.genre28
      const randomMovies = _.sampleSize(movies, 12)
      this.actionMovies.push(...randomMovies)
    }
  },
};
</script>

<style scoped>

</style>