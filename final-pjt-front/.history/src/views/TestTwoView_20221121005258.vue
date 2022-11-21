<template>
  <div>
    <button @click="getPoster">+</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TestView',

  data() {
    return {
      
    };
  },
  components: {
  },

  mounted() {
    
  },

  methods: {
    getPoster() {
      axios({
        url: 'https://api.themoviedb.org/3/movie/12/images?api_key=0d169ae4fecc50f95828ef6ee1b664e9'
      })
      .then(response => {
        console.log(response.data)
      })
    }
  },
};
</script>

<style scoped>

</style>