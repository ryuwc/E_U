<template>
  <div>
    <h1>Choice</h1>
  </div>
</template>

<script>
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
    getMovieInfo() {
      return this.$store.getters['moviesStore/getMovieInfo']
    },
  },
};
</script>

<style scoped>

</style>