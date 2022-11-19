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
      <div style="width: 80%" class="col-span-2 md:w-10">
        <div class="relative top-8 left-10 right-10">
          <p class="text-5xl font-medium">{{ movie.title }}</p>
          <p class="text-2xl">{{ movie.genres }}</p>
          <p class="text-2xl">{{ movie.release_date }} 개봉</p>
          <p class="text-2xl leading-normal">{{ movie.overview }}</p>
          <!-- 가로 스크롤바 시작 -->
          <div
            style="margin-top: 150px;"
            id="journal-scroll"
            class="relative flex w-full gap-6 overflow-x-auto snap-x snap-mandatory pb-14"
          >
            <div class="snap-start shrink-0">
              <img
                class="h-40 bg-white rounded-lg shadow-xl shrink-0 w-80"
                src="https://images.unsplash.com/photo-1604999565976-8913ad2ddb7c?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=320&amp;h=160&amp;q=80"
              />
            </div>
            <div class="snap-start shrink-0">
              <img
                class="h-40 bg-white rounded-lg shadow-xl shrink-0 w-80"
                src="https://images.unsplash.com/photo-1540206351-d6465b3ac5c1?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=320&amp;h=160&amp;q=80"
              />
            </div>
            <div class="snap-start shrink-0">
              <img
                class="h-40 bg-white rounded-lg shadow-xl shrink-0 w-80"
                src="https://images.unsplash.com/photo-1622890806166-111d7f6c7c97?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=320&amp;h=160&amp;q=80"
              />
            </div>
            <div class="snap-start shrink-0">
              <img
                class="h-40 bg-white rounded-lg shadow-xl shrink-0 w-80"
                src="https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=320&amp;h=160&amp;q=80"
              />
            </div>
            <div class="snap-start shrink-0">
              <img
                class="h-40 bg-white rounded-lg shadow-xl shrink-0 w-80"
                src="https://images.unsplash.com/photo-1575424909138-46b05e5919ec?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=320&amp;h=160&amp;q=80"
              />
            </div>
            <div class="snap-start shrink-0">
              <img
                class="h-40 bg-white rounded-lg shadow-xl shrink-0 w-80"
                src="https://images.unsplash.com/photo-1559333086-b0a56225a93c?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=320&amp;h=160&amp;q=80"
              />
            </div>
          </div>
          <!-- 가로 스크롤바 끝 -->
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
  width: 60%;
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
  width: 60%;
}

#journal-scroll::-webkit-scrollbar {
  width: 4px;
  cursor: pointer;
  /*background-color: rgba(229, 231, 235, var(--bg-opacity));*/
}
#journal-scroll::-webkit-scrollbar-track {
  background-color: rgba(229, 231, 235, var(--bg-opacity));
  cursor: pointer;
  /*background: red;*/
}
#journal-scroll::-webkit-scrollbar-thumb {
  cursor: pointer;
  background-color: #a0aec0;
  /*outline: 1px solid slategrey;*/
}
</style>
