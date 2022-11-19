<template>
  <div>
    <div id="main_poster_dark"></div>
    <img
      id="main_poster"
      :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
      class=""
      alt="..."
    />
    <div class="flex grid grid-cols-3 gap-10">
      <div class="w-auto col-span-2 md:w-10">
        <div class="relative top-8 left-10">
          <p class="text-5xl font-medium">{{ movie.title }}</p>
          <p class="text-2xl">{{ movie.genres }}</p>
          <p class="text-2xl">{{ movie.vote_average }}</p>
          <p class="text-2xl"></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
const moviesStore = "moviesStore";

export default {
  name: "MovieDetailInfoView",
  components: {},
  computed: {
    ...mapGetters(moviesStore, ["movie"]),
    ...mapGetters(moviesStore, ["reviews"]),
  },
  methods: {
    ...mapActions(moviesStore, ["getMovieDetail"]),
    ...mapActions(moviesStore, ["getReview"]),
  },
  created() {
    const movieId = this.$route.params.id;
    this.getMovieDetail(movieId);
    this.getReview(movieId);
  },
};
</script>

<style scoped>
* {
  color: white;
  z-index: 1;
}

#main_poster_dark {
  position: absolute;
  top: 0;
  left: 0;
  width: 66.666%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1;
}

#main_poster {
  position: absolute;
  top: 0;
  left: 0;
  /*이미지 앞에 검은색 배경  */
  /* background-color: rgba(0, 0, 0, 0.5); */
  z-index: -1;
  height: 100vh;
  width: 66.666%;
}
</style>
