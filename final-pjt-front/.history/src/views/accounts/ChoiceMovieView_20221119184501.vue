<template>
  <div>
    <h1>Choice</h1>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import _ from 'lodash'

const accountsStore = 'accountsStore'
const moviesStore = 'moviesStore'

export default {
  name: 'ChoiceMovieView',

  data() {
    return {
      
    };
  },
  mounted() {
    
  },
  methods: {
    getRandomMovies() {
      const movies = this[moviesStore].movies
      const randomMovies = _.sampleSize(movies, 10)
      return console.log(randomMovies)
    }
  },
  computed: {
    ...mapGetters(moviesStore, ['movies']),
    ...mapGetters(accountsStore, ['user'])
  },
};
</script>

<style scoped>

</style>