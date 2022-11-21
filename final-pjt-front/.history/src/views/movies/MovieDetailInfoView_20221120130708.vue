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
          <p class="text-6xl font-medium">{{ movie.title }}</p>
          <p class="text-4xl">{{ movie.genres }}</p>
          <p class="text-3xl">{{ movie.release_date }} 개봉</p>
          <p class="text-2xl font-thin leading-normal">{{ movie.overview }}</p>
          <!-- 가로 스크롤바 시작 -->
          <div
            style="margin-top: 130px;"
            id="journal-scroll"
            class="relative flex w-full gap-6 pb-4 overflow-x-auto snap-x snap-mandatory"
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
  name: "MovieDetailInfo",
  data() {
    return {
      movieGenres: [],
    };
  },
  components: {},
  computed: {
    ...mapGetters(moviesStore, ["movie"]),
    ...mapGetters(moviesStore, ["reviews"]),
    ...mapGetters(moviesStore, ["genres"]),
  },
  methods: {
    ...mapActions(moviesStore, ["getMovieDetail"]),
    ...mapActions(moviesStore, ["getReview"]),
    getMovieGenres() {
      console.log('getMovieGenres 시작');
      for (let i = 0; i < this.movie.genre_ids.length; i++) {
        for (let j = 0; j < this.genres.length; j++) {
          if (this.movie.genre_ids[i] === this.genres[j].id) {
            this.movieGenres.push(this.genres[j].name);
          }
        }
      } 
        // this.movie.genres.forEach((movieGenre) => {
        //   console.log('일치한거 발견');
        //   if (genre.id === movieGenre) {
        //     this.movieGenres.push(genre.name);
        //   }
        // });
    },
    // 여기다가 요청 무비포스터 axios 요청 보내는 함수 넣어주고
  },
  created() {
    const movieId = this.$route.params.id;
    this.getMovieDetail(movieId);
    this.getReview(movieId);
    this.getMovieGenres();
    // 여기다가 무비포스터 요청보내는 함수 호출해서 컴퓨티드나 data에 넣어주고
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cute+Font&family=Do+Hyeon&family=Pacifico&display=swap');

* {
  color: white;
  z-index: 1;
  font-family: 'Do Hyeon', sans-serif;
}

#main_poster_dark {
  position: absolute;
  top: 0;
  left: 0;
  width: 60%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: -1;
}

#main_poster {
  position: absolute;
  top: 0;
  left: 0;
  /*이미지 앞에 검은색 배경  */
  /* background-color: rgba(0, 0, 0, 0.5); */
  z-index: -2;
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
