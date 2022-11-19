<template>
  <div>
    <h1>Choice</h1>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

const accoutnsStore = 'accountsStore'
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
    
  },
  computed: {
    ...mapGetters(moviesStore, ['movies']),
  },
};
</script>

<style scoped>

</style>