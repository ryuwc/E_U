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