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


export default {
  name: 'MovieView',
  components: {
    MovieCard,
    NowMovie,
  },
  computed: {
    movies(){
      return this.$store.state.movies
    },
    nowmovies() {
      return this.$store.state.nowmovies
    }
      
    
  },

  methods: {

   getMovies() {
    this.$store.dispatch('getMovies')
    // console.log(this.movies)
   },
   getNowMovies() {
    this.$store.dispatch('getNowMovies')
   },

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