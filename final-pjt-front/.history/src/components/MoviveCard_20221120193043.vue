<template>
  <!-- <router-link
      style="display: inline-block; width: 20rem;"
      :to="{ name: 'MovieDetailInfoView', params: { id: movie.id } }"
    > -->

  <!-- 수정 카드 11.20 류원창 -->
  <!-- Item -->
  <div
    class="relative overflow-hidden bg-blue-900 rounded-lg group focus:outline-none focus:ring-4 focus:ring-blue-500 focus:ring-opacity-50 focus:ring-offset-2 focus-within:ring-4 focus-within:ring-blue-500 focus-within:ring-opacity-50 focus-within:ring-offset-2"
    tabindex="0"
  >
    <img
      class="transition duration-300 ease-out transform group-hover:scale-125 group-focus:scale-125 group-focus-within:scale-125"
      src="https://source.unsplash.com/Bkci_8qcdvQ/800x600"
      alt="Image 2"
    />

    <!-- Item Overlay -->
    <div
      class="absolute inset-0 flex flex-col items-center justify-center transition duration-300 ease-out bg-blue-700 opacity-0 bg-opacity-80 group-hover:opacity-100 group-focus:opacity-100 group-focus-within:opacity-100"
    >
      <div class="text-center">
        <h4 class="text-lg font-semibold text-white">Main Title</h4>
        <h5 class="mb-5 font-medium text-white text-opacity-80">Image Description</h5>
        <a
          href="#"
          class="inline-flex items-center justify-center px-3 py-2 space-x-2 text-sm font-semibold leading-5 text-blue-800 bg-blue-200 border border-blue-200 rounded focus:outline-none hover:text-blue-800 hover:bg-blue-300 hover:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50 active:bg-blue-200 active:border-blue-200"
        >
          <svg class="inline-block w-4 h-4 opacity-50 hi-solid hi-external-link" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path d="M11 3a1 1 0 100 2h2.586l-6.293 6.293a1 1 0 101.414 1.414L15 6.414V9a1 1 0 102 0V4a1 1 0 00-1-1h-5z"></path>
            <path d="M5 5a2 2 0 00-2 2v8a2 2 0 002 2h8a2 2 0 002-2v-3a1 1 0 10-2 0v3H5V7h3a1 1 0 000-2H5z"></path>
          </svg>
          <span>More Info</span>
        </a>
      </div>
    </div>
    <!-- END Item Overlay -->
  </div>
  <!-- END Item -->

  <!-- 기존카드 -->
  <!-- <div
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
      </div> -->
  <!-- </router-link> -->
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  methods: {
    goToDetail(id) {
      this.$router.push({ name: 'MovieDetailInfoView', params: { id: id } });
    },
  },
};
</script>

<style></style>
