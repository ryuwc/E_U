<script setup></script>

<template>
  <div class="bg-white">
    <LeftBar
    style="position: absolute; top: 180px; left: 0; z-index: 1; color: black;"
    />
    <div id="for_nav"></div>
    <div style="margin-left: 300px;" class="container px-4 py-16 ml-64 space-y-16 lg:px-8 lg:py-32">
      <div class="text-center">
        <h2 class="mb-4 text-3xl font-extrabold md:text-4xl">
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-500 via-pink-500 to-rose-500">배꼽 빠지게 웃긴 코메디 영화!</span>
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
import LeftBar from '@/components/LeftBar.vue';
const moviesStore = 'moviesStore';

export default {
  name: 'AllMoviesView',
  components: {
    LeftBar,
  },

  data() {
    return {
      actionMovies: [],
    };
  },
  computed: {
    ...mapGetters(moviesStore, ['genre35']),
    
  },
  mounted() {
    this.getRandomMovies()
    console.log(this);
    window.addEventListener('scroll', () => {
      let value = window.scrollY;
      let hei = window.innerHeight

      // console.log('탑', top)
      // console.log('하이트', hei)
      // console.log('현재 스크롤', value);
      if (hei - value < 300) {
        // console.log(hei, value);
        // console.log('스크롤이 끝에 도달했습니다.');
        this.getRandomMovies()
      }
      
  });
    
  },
  methods: {
    getRandomMovies() {
      const movies = this.genre35
      const randomMovies = _.sampleSize(movies, 24)
      this.actionMovies.push(...randomMovies)
    }
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