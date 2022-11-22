<template>
  <div>
    <div id="main_poster_dark"></div>
    <img id="main_poster" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" class="" alt="..." />

    <div class="relative flex grid grid-cols-10 gap-10">
      <!-- 디테일 왼쪽 시작 -->
      <div id="left" style="width: 60%" class="col-span-6 md:w-10">
        <button
        class="hoverbutton"
        data-hover="Hello, this is the tooltip"
        >
          <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAABmJLR0QA/wD/AP+gvaeTAAAHQ0lEQVR4nO2dXWwU1xXH/+fOmgVvbSclQiWA6hR3d9ukKBYvUZIqcmgTCeGsA9WqUkVpsB1LVDFqm1R95LUJldrNAzUYXNq3TesFm7pVUbDUNH1LKU0ddl2HpsSURFEDBhvq8c49fQgINcKeOzN39mvu79Xny/fv+bh3zr0GDAaDwWAwGAwGQ9SgahewEoc2j66zmkQnMVIEpACkGFhHoATA9wJI3DJdAOgKgxdA+JAY00RcBFCi8tLZvTPZj6r3W6xMTQkwtHW8Wczz1wXkkxLoIuAhBK+RAbwN8CRBnGlZWDydnc3e1FCuFqouwAEcEJuSWx4FrN1M/E0ArSGnvAbgJAivtRbtiSyyTsj5VqRqAoy0T652Vs3tBeFFAA9Upwq6wJAHbzrxY4Mz2xerUkGlEw5tHW+2Fpx9YHwfwPpK51+Gy8R0sNwifj7wVveNSiauqADD6RPdYOQAtFcyrwdmGfhef6nn15VKWBEBRtKFdinFq0y8oxL5NDDmxKwXBqa6L4adKHQBhpOFHhAdA3Bv2Lk0c43A/b2lZ/NhJglNgFzHRDxh2S8zMBhWjkpATIcXZNNgWA/pUAQ4nh5duyTFKRAeCSN+FXgTMfuZvqnsx7oDaxfgaOrk/RL8ewK+ojt2lTkvynh677s97+sMqlWAoeR42iLnDwA26YxbQ1wk0FO9pUxJV0BtAhxPjm9YIudNAJ/XFbMWYeASCeexvvO7/qUjntAR5Hh6dO0SOafR4IMPAARsAFsTww/mP6sjXmABch0T8SUpTgH4koZ66gPGl6m8ajzXMREPGiqwAImY/ZMGettRhoFHE5b9ctA4gZ4BR1InvkHAa0GLqGeYaFd/MTPq19+3ACPpQrvD9FcAbX5jNAhXIZyH/T6Ufd+CHKYczOADwD2Q4md+nX0JMJws9ADo9pu08aDMcPqEr/HwfAsa2jrebM077yACr5we+Wfrgv2g18+dnq+A2Lz8Lszg340HrieaBrw6eboCch0T8WbLvgDgfq+JdNFbzKz486PpkxWq5K5cthbbvvDce13/VXXwdAU0C7sXVRz8OmC9s3pujxcHZQEO4IC49QHdsBKMlxisfGdRFmBTqvMJVK17oa7YfPSLY19VNfZwC+LdfqqJJEJ9rJQEyG/Mr2Fgp/+KIkc2vzG/RsVQSYC5xOqnYGa9Xmi9tib+pIqhkgACUimY4Q5E6FKxUxJAQi2Y4Q5MvE3FzlWAQ5tH193qUjZ4Y8tQcvw+NyNXAawm0Yka6KKuQ0QTnIddjdwMiJHSU0/0cOA+du4CKAQxLEtwAZiQ1FNL9CByFyDmGoTxOT3l/D9uq5qVjhvSKqrr2Km8hrZoKCSquI6dESBctAjwGQ2FRBUtAhhCREWA+dCraFyuuxmoCOAaxLAsRoAq4zp2rvMAJnxArH8xzu97d413RXyaD9wMVNaCpvXUEj2Y4bqTxn0pAu5BDMuiQQAyAvjF0iFArGz/BZ8c+WLwhrSEPOtm5CrA3pnsRwz8XU9NEYJwbk9x53/czJRmwgQ+E7yiaEGSlMZMUQBhBPCIVPyjVRKgZWHxNIC5QBVFi7m2G/akiqGSAJ9sOuDfBKspQhDyqhs1lFdDmfAr/xVFC5bqY6UswKXiuT8CdMFfSRGCMdM3nfmTqrmX/QGSIQ/6qyo6sOBXCKQ8b/L0QeamEz8G4N+eq4oOszfL8eNeHDx3vB1JF35ATOZKuAsM7O8v9eS8+Hj+JCkTsUMA3vPqFwHejS22Hfbq5FmAgbe6bxDzPq9+DY+k/V52R97G10f53ulnfwdgzI9vI8KEQt8/Mr/14+v/rIiY9QKAq379G4gr1hL2+3X2LcDAVPdFSXI3or1UzcToDXKQX6C+oOeLO08R8GqQGHUN4ae90z2FICECN2YtOKt+SMCfg8apQ95otewfBQ0SWIDBme2L5SV7O0DngsaqGxhTiNk92amsHTSUObbSO7NOzHpM18He2npD90x3XyLQ0wBCP3G8ilyUJLfpPFVda3NubylTcoTzCIC/6YxbExDeEWU8/nxxp9Y+Ke3d0QPnd11GzO5qsAfzG3ZT7HHd50YDIbWn901lP35/fdsTAH6M+p4nMAG51pj9tX1v77gSRoLQ9/8eSY1lCHIEdfgPHADq6ytlQj0XNfQNGv2lZ05COJ2oo7UjJhREGQ+FPfhAhXfAH06P7hAscqjZg5/oAiQG/S6s+cpYqUS3yW/Mr7meaBqQoBcJ2FDp/MswC9BBa7F1yM+SchCqdgZErmMi3hyzvwPGSwA2V6UIxgwLfqXNWvqFjlmtH2riEI4j6cJWwfRtBr4FYG3I6eYAjAnGL5+bzrzu5QN6GNSEALcZaZ9c7TRd2waLt4HRBWALgr8oSBDOATzJkl6P2W1nKn2bWYmaEuDTDCXH7xOW7ITDSQKnAaRAYh2AFoDvwZ09zPMAXQVwHeAPwTzNoKIFlCwhz6p0KRsMBoPBYDAYDAZDpfgfSvcrSThc2dEAAAAASUVORK5CYII=">
        </button>
        <div class="absolute top-8 left-10 right-10">
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
      <MovieDetailR class="col-span-4 mr-10" />
      <!-- 디테일 오른쪽 끝 -->
    </div>
  </div>
</template>

<script>
import MovieDetailR from '@/components/MovieDetailR.vue';
import PosterSlider from '@/components/PosterSlider.vue';

import { mapActions, mapGetters, mapMutations } from 'vuex';
const moviesStore = 'moviesStore';

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
    };
  },
  components: {
    MovieDetailR,
    PosterSlider,
  },
  computed: {
    ...mapGetters(moviesStore, ['movie']),
    ...mapGetters(moviesStore, ['reviews']),
    ...mapGetters(moviesStore, ['allGenres']),
  },
  methods: {
    ...mapActions(moviesStore, ['getMovieDetail']),
    ...mapActions(moviesStore, ['getReview']),
    // 여기다가 요청 무비포스터 axios 요청 보내는 함수 넣어주고

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
        console.log('영화 비디오 가져오기 완료: ', this.movieVideos);
      });
    },
    ...mapMutations(moviesStore, ['SET_NOW_MOVIE_VIDEO']),

    // 영화 찜 버튼 클릭 시 실행되는 함수
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
    // movieStore의 state에 있는 nowMovieVideo에 저장
    setTimeout(() => {
      this.SET_NOW_MOVIE_VIDEO(this.movieVideos);
    }, 1000);
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cute+Font&family=Do+Hyeon&family=Pacifico&display=swap');
/* @import url('https://fonts.googleapis.com/css2?family=Dongle&family=Jua&display=swap'); */
@import url('https://fonts.googleapis.com/css2?family=Dongle:wght@300;400&family=Jua&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Dongle:wght@300;400&family=Gamja+Flower&family=Jua&display=swap');

/* 찜 하기 버튼 후버 */
.hoverbutton {
  position: relative;
  border-bottom: 1px dotted black;
  position: absolute;
  top: 2rem;
  left: 40rem;
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
