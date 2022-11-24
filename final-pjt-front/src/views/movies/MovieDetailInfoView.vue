<template>
  <div>
    <div id="for_nav"></div>
    <div id="main_poster_dark"></div>
    <img id="main_poster" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" class="" alt="..." />

    <div class="relative flex grid grid-cols-10 gap-10 mt-28">
      <!-- 디테일 왼쪽 시작 -->
      <div id="left" style="width: 89%" class="col-span-6 md:w-10">
        <div v-if="user.username">
          <button
          v-if="!isWish"
          class="hoverbutton"
          data-hover="내 위시리스트에 추가"
          @click="[addMovieToWishList({ movieId: movie.id, nowUser: nowUser, authHead: authHead }), toggleIsWish()]"
          >
            <img src="data:image/png;base64,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">
          </button>
          <button
          v-if="isWish"
          class="hoverbutton"
          data-hover="내 위시리스트에서 삭제"
          @click="[addMovieToWishList({ movieId: movie.id, nowUser: nowUser, authHead: authHead }), toggleIsWish()]"
          >
            <img src="data:image/png;base64,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">
          </button>
        </div>
        <div style="width: 55%;" class="absolute top-8 left-10 right-10">
          <p class="mb-3 text-6xl font-medium">{{ movie.title }}</p>
          <p class="mb-3 text-4xl">{{ movie.thisMovieGenre.join(', ') }}</p>
          <p class="mb-3 text-3xl">{{ movie.release_date }} 개봉</p>
          <p id="overview" class="text-xl leading-normal">{{ movie.overview }}</p>

          <PosterSlider class="h-32" :moviePosters="moviePosters" />
          <!-- 가로 스크롤바 시작 -->
          <!-- <div
            style="margin-top: 50px;"
            id="journal-scroll"
            class="relative flex w-full gap-6 pb-4 overflow-x-auto snap-x snap-mandatory"
          >
            <div class="snap-start shrink-0"
            v-for="(poster, index) in moviePosters"
            :key="index"
            >
              <img
                class="w-40 bg-white rounded-lg shadow-xl h-80 shrink-0"
                :src="`https://image.tmdb.org/t/p/original${poster.file_path}`"
              />
            </div>
          </div> -->
          <!-- 가로 스크롤바 끝 -->
        </div>
      </div>
      <!-- 디테일 왼쪽 끝 -->

      <!-- 디테일 오른쪽 시작 -->
      <MovieDetailR class="col-span-4 mt-10 mr-10" />
      <!-- 디테일 오른쪽 끝 -->
    </div>
  </div>
</template>

<script>
import MovieDetailR from '@/components/MovieDetailR.vue';
import PosterSlider from '@/components/PosterSlider.vue';

import { mapActions, mapGetters, mapMutations } from 'vuex';
const moviesStore = 'moviesStore';
const accountsStore = 'accountsStore';

// 11.21 집에서 작성
import axios from 'axios';
import _ from 'lodash';

export default {
  name: 'MovieDetailInfo',
  data() {
    return {
      movieGenres: ['액션', '드라마'],
      movieId: this.$route.params.id,
      moviePosters: null,
      movieVideos: null,
      // 영화가 현재 위시리스에 있는지 확인하는 변수
      isWish: false,
    };
  },
  components: {
    MovieDetailR,
    PosterSlider,
  },
  computed: {
    ...mapGetters(moviesStore, ['movie', 'reviews', 'allGenres', 'nowUserWishList']),
    ...mapGetters(accountsStore, ['user', 'authHead']),
    nowUser() {
      return JSON.parse(JSON.stringify(this.user))
    },
  },
  methods: {
    ...mapActions(moviesStore, ['getMovieDetail']),
    ...mapActions(moviesStore, ['getReview']),

    // 11.21 집에서 작성
    getMoviePoster() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movieId}/images?api_key=0d169ae4fecc50f95828ef6ee1b664e9`,
      }).then((res) => {
        // console.log('영화 포스터: ', res.data);
        this.moviePosters = _.sampleSize(res.data.posters, 10);
      });
    },
    getMovieVideos() {
      axios({
        url: `https://api.themoviedb.org/3/movie/${this.movieId}/videos?api_key=0d169ae4fecc50f95828ef6ee1b664e9`,
      }).then((res) => {
        // console.log('영화 비디오: ', res.data);
        this.movieVideos = res.data.results;
        // console.log('영화 비디오 가져오기 완료: ', this.movieVideos);
      });
    },
    ...mapMutations(moviesStore, ['SET_NOW_MOVIE_VIDEO']),

    // 영화 찜 버튼 클릭 시 실행되는 함수
    toggleIsWish() {
      this.isWish = !this.isWish;
    },
    ...mapActions(moviesStore, ['addMovieToWishList']),
    ...mapActions(moviesStore, ['getNowUserWishList']),

    // 클릭 수 1 증가시키는 함수
    increaseClickCount() {
      axios({
        method: 'post',
        url: `http://localhost:8000/movies/click/${this.movieId}/`,
        headers: this.authHead,
      }).then((res) => {
        console.log('클릭 수 1 증가 완료: ', res.data);
      });
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
    this.getMovieVideos();
  },
  mounted() {
    this.getNowUserWishList({ userId: this.nowUser.id, authHead: this.authHead })
    // movieStore의 state에 있는 nowMovieVideo에 저장
    setTimeout(() => {
      this.SET_NOW_MOVIE_VIDEO(this.movieVideos);
    }, 500);
    this.nowUserWishList.forEach((wish) => {
      console.log('wish.movie.id: ', wish.id)
      if (wish.id == this.movieId) {
        this.isWish = true;
      }
    })
    this.increaseClickCount();
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cute+Font&family=Do+Hyeon&family=Pacifico&display=swap');
/* @import url('https://fonts.googleapis.com/css2?family=Dongle&family=Jua&display=swap'); */
@import url('https://fonts.googleapis.com/css2?family=Dongle:wght@300;400&family=Jua&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Dongle:wght@300;400&family=Gamja+Flower&family=Jua&display=swap');

#for_nav{
  position: absolute;
    top: 0;
    height: 100px;
    width: 100%;
    /* background-color: rgba(0, 0, 0, 0.2); */
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0));
}

h1 {
  font-size: 32px;
}

h2 {
  font-size: 24px;
}

h3 {
    font-size: 1.75rem;
}

h4 {
  font-size: 16px;
}

h5 {
  font-size: 14px;
}

h6 {
  font-size: 12px;
}

/* 찜 하기 버튼 후버 */
.hoverbutton {
  position: relative;
  border-bottom: 1px dotted black;
  position: absolute;
  top: 2rem;
  left: 50rem;
  z-index: 1;
  width: 64px;
  height: 64px;
  border: none;
}

.hoverbutton:before {
  content: attr(data-hover);
  visibility: hidden;
  opacity: 0;
  width: 140px;
  background-color: black;
  color: #fff;
  text-align: center;
  border-radius: 5px;
  padding: 5px 0;
  transition: opacity 1s ease-in-out;

  position: absolute;
  z-index: 1;
  left: 0;
  top: 110%;
}

.hoverbutton:hover:before {
  opacity: 1;
  visibility: visible;
}

#overview {
  font-weight: initial;
}

#left {
  color: white;
  z-index: 1;
  /* 폰트 1번 후보 */
  /* font-family: 'Do Hyeon', sans-serif; */

  /* 폰트 2번 후보 */
  /* font-family: 'Dongle', sans-serif; */

  /* 폰트 3번 후보 */
  font-family: 'Jua', sans-serif;

  /* 폰트 4번 후보 */
  /* font-family: 'Gamja Flower', cursive; */
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
