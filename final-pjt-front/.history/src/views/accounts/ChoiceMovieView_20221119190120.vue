<template>
  <div>
    <h1>Choice</h1>
    <button @click="getRandomMovies">랜덤무비</button>
    <MoviveCard/>
  </div>
</template>

<script>
import MoviveCard from '@/components/MoviveCard.vue'

import { mapGetters } from 'vuex'
import _ from 'lodash'

const accountsStore = 'accountsStore'
const moviesStore = 'moviesStore'

export default {
  name: 'ChoiceMovieView',

  data() {
    return {
      forMovies: []
    };
  },
  components: {
    MoviveCard
  },
  methods: {
    getRandomMovies() {
      const movies = this.movies
      const randomMovies = _.sampleSize(movies, 10)
      this.forMovies.push(randomMovies)
    }
  },
  computed: {
    ...mapGetters(moviesStore, ['movies']),
    ...mapGetters(accountsStore, ['user']),
    highVoteMovies() {
      const movies = this.movies
      const highVoteMovies = _.filter(movies, (movie) => {
        return movie.vote_average >= 8
      })
      return highVoteMovies
    }
  },
  mounted() {
    this.getRandomMovies()
  },
};
</script>

<style scoped>

</style>