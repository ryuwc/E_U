<template>
  <div>
    <div id="main_poster_dark"></div>
    <img
      id="main_poster"
      :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
      class=""
      alt="..."
    />

    <div class="flex grid grid-cols-10 gap-10">
      <!-- 디테일 왼쪽 시작 -->
      <div id="left" style="width: 80%" class="col-span-6 md:w-10">
        <div class="relative top-8 left-10 right-10">
          <p class="text-6xl font-medium">{{ movie.title }}</p>
          <p class="text-4xl">{{ movie.thisMovieGenre.join(', ') }}</p>
          <p class="text-3xl">{{ movie.release_date }} 개봉</p>
          <p class="text-2xl font-thin leading-normal">{{ movie.overview }}</p>
          <!-- 가로 스크롤바 시작 -->
          <div
            style="margin-top: 130px;"
            id="journal-scroll"
            class="relative flex w-full gap-6 pb-4 overflow-x-auto snap-x snap-mandatory"
          >
            <div class="snap-start shrink-0"
            v-for="(poster, index) in moviePosters"
            :key="index"
            >
              <img
                class="w-32 bg-white rounded-lg shadow-xl h-72 shrink-0"
                :src="`https://image.tmdb.org/t/p/original${poster.file_path}`"
              />
            </div>
          </div>
          <!-- 가로 스크롤바 끝 -->
        </div>
      </div>
      <!-- 디테일 왼쪽 끝 -->
      
      <!-- 디테일 오른쪽 시작 -->
      <MovieDetailR
      class="col-span-4 mr-10"
      />
      <!-- 디테일 오른쪽 끝 -->
    </div>

  </div>
</template>

<script>
import MovieDetailR from '@/components/MovieDetailR.vue' 
import { mapActions, mapGetters } from "vuex";
const moviesStore = "moviesStore";

// 11.21 집에서 작성
import axios from 'axios';
import _ from 'lodash';

export default {
  name: "MovieDetailInfo",
  data() {
    return {
      movieGenres: ['액션', '드라마'],
      movieId: this.$route.params.id,
      moviePosters: null,
    };
  },
  components: {
    MovieDetailR,
  },
  computed: {
    ...mapGetters(moviesStore, ["movie"]),
    ...mapGetters(moviesStore, ["reviews"]),
    ...mapGetters(moviesStore, ["allGenres"]),
  },
  methods: {
    ...mapActions(moviesStore, ["getMovieDetail"]),
    ...mapActions(moviesStore, ["getReview"]),
    // 여기다가 요청 무비포스터 axios 요청 보내는 함수 넣어주고

    // 11.21 집에서 작성
    getMoviePoster() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movieId}/images?api_key=0d169ae4fecc50f95828ef6ee1b664e9`
      })
      .then((res) => {
        // console.log('영화 포스터: ', res.data);
        this.moviePosters = _.sampleSize(res.data.posters, 10)
        
      })
    },
  },
  created() {
    const movieId = this.$route.params.id;
    this.getMovieDetail(movieId);
    this.getReview(movieId);
    // this.getMovieGenres();
    // console.log('새로운 무비 객체', this.movie)
    // 여기다가 무비포스터 요청보내는 함수 호출해서 컴퓨티드나 data에 넣어주고

    // 11.21 집에서 작성
    this.getMoviePoster();
    // for (let poster of this.moviePosters) {
    //   console.log('포스터: ', poster)
    // }
  },
  mounted() {
    // 
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cute+Font&family=Do+Hyeon&family=Pacifico&display=swap');

left {
  z-index: 1;
  font-family: 'Do Hyeon', sans-serif;
}

#left {
  color: white;
}

MovieDetailR {
  color: black;
  z-index: -1;
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
