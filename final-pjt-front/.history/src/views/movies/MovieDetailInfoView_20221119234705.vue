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
          <p class="text-2xl leading-normal">{{ movie.overview }}</p>
          <!-- 가로 스크롤바 시작 -->
          <button
            id="dropdownDefault"
            data-dropdown-toggle="dropdown"
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            type="button"
          >
            Dropdown button
            <svg
              class="w-4 h-4 ml-2"
              aria-hidden="true"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M19 9l-7 7-7-7"
              ></path>
            </svg>
          </button>
          <!-- Dropdown menu -->
          <div
            id="dropdown"
            class="z-10 hidden bg-white divide-y divide-gray-100 rounded shadow w-44 dark:bg-gray-700"
          >
            <ul
              class="py-1 text-sm text-gray-700 dark:text-gray-200"
              aria-labelledby="dropdownDefault"
            >
              <li>
                <a
                  href="#"
                  class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                  >Dashboard</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                  >Settings</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                  >Earnings</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                  >Sign out</a
                >
              </li>
            </ul>
          </div>
          <div
            style="margin-top: 100px"
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
