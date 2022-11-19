<template>
  <div>
    <h4>Movie View</h4>
    <NowMovie 
    v-for="(nowmovie, index) in nowmovies" 
    :key="index"
    :nowmovie='nowmovie'/>
    <MovieCard
      v-for="(movie, index) in movies" 
      :key="index"
      :movie="movie"
    />
    <hr>
    <!-- movies가 다 채워지지 않았을 때 모달 -->
    <div v-if="!movies" class="w-full h-screen bg-black">
      <div class="w-1/2 bg-white h-1/2">
        <h1>영화 정보를 불러오는 중입니다.</h1>
      </div>
    </div>
    
  </div>
</template>

<script>
import MovieCard from '@/components/MoviveCard.vue'
import NowMovie from '@/components/NowMovie.vue'
import { mapActions, mapGetters } from 'vuex';


const moviesStore = 'moviesStore'

export default {
  name: 'MovieView',
  components: {
    MovieCard,
    NowMovie,
  },
  computed: {
    ...mapGetters(moviesStore, ['movies', 'nowmovies']),
  },
  

  methods: {
    ...mapActions(moviesStore, ['getMovies']),
    ...mapActions(moviesStore, ['getNowMovies']),

  },

  created() {
    this.getMovies(),
    this.getNowMovies()
  },
  
  data() {
    return {
      
    };
  },

};
</script>

<style scoped>

</style>