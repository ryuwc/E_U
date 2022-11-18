<template>
  <div>
    <h1>movie detail info</h1>
    <div>
      <img :src="`https://image.tmdb.org/t/p/w185${movie.poster_path}`" class="mt-2 h-100 card-img-top" alt="...">
      <div>
        <h5>{{ movie.title }}</h5>
        <p>평점: {{ movie.vote_average }}</p>
      </div>
    </div>
    <MovieReviewView
      v-for="(review, index) in reviews" 
      :key="index"
      :review="review"
    />

  </div>
</template>

<script>

import { mapActions, mapGetters } from 'vuex';
import MovieReviewView from '@/views/movies/MovieReviewView.vue'
const moviesStore = 'moviesStore'


export default {
  name: 'MovieDetailInfoView',
  components: {
    MovieReviewView
  },
  computed: {
    ...mapGetters(moviesStore, ['movie']),
    ...mapGetters(moviesStore, ['reviews'])
  },
  methods: {
    ...mapActions(moviesStore, ['getMovieDetail']),
    ...mapActions(moviesStore, ['getReview']),
  },
  created() {
    const movieId = this.$route.params.id
    this.getMovieDetail(movieId)
    this.getReview(movieId)
  }
}
</script>

<style>

</style>