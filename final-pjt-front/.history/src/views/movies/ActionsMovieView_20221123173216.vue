<template>
  <div>
    
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
const moviesStore = 'moviesStore';

export default {
  name: 'ActionsMovieView',

  data() {
    return {
    };
  },
  computed: {
    ...mapGetters(moviesStore, ['genre28']),
  },
  mounted() {
  },
  methods: {
    
  },
};
</script>

<style scoped>

</style>