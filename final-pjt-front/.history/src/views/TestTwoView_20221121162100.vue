<template>
<div class="star-rating">
  <input type="radio" id="5-stars" name="rating" value="5" />
  <label for="5-stars" class="star">&#9733;</label>
  <input type="radio" id="4-stars" name="rating" value="4" />
  <label for="4-stars" class="star">&#9733;</label>
  <input type="radio" id="3-stars" name="rating" value="3" />
  <label for="3-stars" class="star">&#9733;</label>
  <input type="radio" id="2-stars" name="rating" value="2" />
  <label for="2-stars" class="star">&#9733;</label>
  <input type="radio" id="1-star" name="rating" value="1" />
  <label for="1-star" class="star">&#9733;</label>
</div> 
</template>

<script>
import axios from 'axios';

export default {
  name: 'TestView',

  data() {
    return {};
  },
  components: {},

  mounted() {},

  methods: {
    getPoster(moveId) {
      axios({
        url: `https://api.themoviedb.org/3/movie/${moveId}/images?api_key=0d169ae4fecc50f95828ef6ee1b664e9`,
      }).then((response) => {
        console.log(response.data);
      });
    },
  },
};
</script>

<style scoped></style>
