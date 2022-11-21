<template>
    <!-- <router-link
      style="display: inline-block; width: 20rem;"
      :to="{ name: 'MovieDetailInfoView', params: { id: movie.id } }"
    > -->
      <div
        id="card-div"
        class="m-3 card"
        style="width: 18rem; cursor:pointer"
        data-toggle="tab-hover"
        @click="goToDetail(movie.id)"
      >
        <img
          v-if="movie.poster_path"
          :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
          class="mt-2 h-100 card-img-top"
          alt="..."
        />
        <img
          v-else
          src="https://i.ytimg.com/vi/EMhKeVHboiA/maxresdefault.jpg"
          class="mt-2 h-100 card-img-top"
          alt="..."
        />
        <div class="card-body">
          <h5 class="card-title text-truncate">{{ movie.title }}</h5>
          <p class="card-text">평점: {{ movie.vote_average }}</p>
        </div>
      </div>
    <!-- </router-link> -->
</template>

<script>
export default {
  name: "MovieCard",
  props: {
    movie: Object,
  },
  methods: {
    goToDetail(id) {
      this.$router.push({ name: "MovieDetailInfoView", params: { id: id } });
    },
  }
};
</script>

<style></style>
