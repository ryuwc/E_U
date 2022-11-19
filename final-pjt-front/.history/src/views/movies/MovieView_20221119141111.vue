<template>
  <div>
    <h4>Movie View</h4>
    <!-- 로딩 중일때 띄어줄 모달 -->
    <div v-if="loading" class="w-full h-auto bg-black">
    </div>
    <div v-else>
      <NowMovie 
      v-for="(nowmovie, index) in nowmovies" 
      :key="index"
      :nowmovie='nowmovie'/>
      <MovieCard
        v-for="(movie, index) in movies" 
        :key="index"
        :movie="movie"
      />
    </div>
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
  data() {
    return {
    }
  },
  computed: {
    ...mapGetters(moviesStore, ['movies', 'nowmovies']),
    loading() {
      return this.$store.getters['moviesStore/loading']
    },
  },
  

  methods: {
    ...mapActions(moviesStore, ['getMovies']),
    ...mapActions(moviesStore, ['getNowMovies']),

  },

  created() {
    this.getMovies(),
    this.getNowMovies()
  },
};
</script>

<style scoped>

</style>