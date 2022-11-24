<template>
  <div id="bg">
    <div>
      
      <!-- 영상 재생 -->
      <div>
        <div id='area'>
          <h2 style="padding-top: 70px;" class="welcome">Welcome</h2>
          <iframe id='video' :src=videoURL
          frameborder="0" allow="autoplay">
          </iframe>
        </div>
      </div>

      <!-- 영화 카테고리 시작-->
      <div class="mx-5">


        <!-- 알고리즘 추천 영화 담기 2-3개-->
        <div class="mt-5">
          <p class="">@@@@@@@@@@</p>
          <div class="d-flex scroll type2">
            <div v-for="(movie, index) in mg6" :key='index'>
              <router-link :to="{ name:'MovieDetailInfoView', params: { id: movie.id } }">
              <div class="card-item effect11 left_to_right">
                <a href="#">
                  <div class="img w-100">
                    <img 
                    :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" 
                    alt="img">
                  </div>
                <div class="info">
                  <h3>{{ movie.title }}</h3>
                  <br>
                  <br>
                  <p>{{ movie.release_date }}</p>
                </div>
                </a>
              </div>
              </router-link>
            </div>
          </div>
        </div>

        <!-- # 장르 카테고리 분류 시작 -->

        <!-- 장르 (코미디 + 드라마) -->
        <div class="mt-5">
          <p class="">배꼽 빠지게 웃긴 코미디</p>
          <!-- <div class="d-flex" style="white-space:nowrap; overflow:auto;  width:100%;"> -->
          <div class="d-flex scroll type2" >
            <div v-for="(movie, index) in mg1" :key='index'>
              <router-link :to="{ name:'MovieDetailInfoView', params: { id: movie.id } }">
              <div class="card-item effect11 left_to_right">
                <a href="#" >
                  <div class="img w-100">
                    <img 
                    :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" 
                    alt="img">
                  </div>
                <div class="info">
                  <h3>{{ movie.title }}</h3>
                  <br>
                  <br>
                  <p>{{ movie.release_date }}</p>
                </div>
                </a>
              </div>
              </router-link>
            </div>
          </div>
        </div>

        <!-- 장르 (공포) -->
        <div class="mt-5">
          <p class="">등골이 서늘해지는 공포</p>
          <div class="d-flex scroll type2">
            <div v-for="(movie, index) in mg2" :key='index'>
              <router-link :to="{ name:'MovieDetailInfoView', params: { id: movie.id } }">
              <div class="card-item effect11 left_to_right">
                <a href="#">
                  <div class="img w-100">
                    <img 
                    :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" 
                    alt="img">
                  </div>
                <div class="info">
                  <h3>{{ movie.title }}</h3>
                  <br>
                  <br>
                  <p>{{ movie.release_date }}</p>
                </div>
                </a>
              </div>
            </router-link>
            </div>
          </div>
        </div>

        <!-- 장르 ( 범죄 + 스릴러 ) -->
        <div class="mt-5">
          <p class="">범인은 누구..범죄 스릴러</p>
          <div class="d-flex scroll type2">
            <div v-for="(movie, index) in mg3" :key='index'>
              <router-link :to="{ name:'MovieDetailInfoView', params: { id: movie.id } }">
              <div class="card-item effect11 left_to_right">
                <a href="#">
                  <div class="img w-100">
                    <img 
                    :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" 
                    alt="img">
                  </div>
                <div class="info">
                  <h3>{{ movie.title }}</h3>
                  <br>
                  <br>
                  <p>{{ movie.release_date }}</p>
                </div>
                </a>
              </div>
              </router-link>
            </div>
          </div>
        </div>

        <!-- 장르 ( 애니메이션 + 가족 )-->
        <div class="mt-5">
          <p class="">자녀와 함께보는 가족 영화</p>
          <div class="d-flex scroll type2">
            <div v-for="(movie, index) in mg4" :key='index'>
              <router-link :to="{ name:'MovieDetailInfoView', params: { id: movie.id } }">
              <div class="card-item effect11 left_to_right">
                <a href="#">
                  <div class="img w-100">
                    <img 
                    :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" 
                    alt="img">
                  </div>
                  <div class="info">
                    <h3>{{ movie.title }}</h3>
                    <br>
                    <br>
                  <p>{{ movie.release_date }}</p>
                </div>
                </a>
              </div>
              </router-link>
            </div>
          </div>
        </div>

        <!-- 장르 (판타지 + SF) -->
        <div class="mt-5">
          <p class="">판타지와 SF의 세계로</p>
          <div class="d-flex scroll type2">
            <div v-for="(movie, index) in mg5" :key='index'>
              <router-link :to="{ name:'MovieDetailInfoView', params: { id: movie.id } }">
              <div class="card-item effect11 left_to_right">
                <a href="#">
                  <div class="img w-100">
                    <img 
                    :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" 
                    alt="img">
                  </div>
                <div class="info">
                  <h3>{{ movie.title }}</h3>
                  <br>
                  <br>
                  <p>{{ movie.release_date }}</p>
                </div>
                </a>
              </div>
              </router-link>
            </div>
          </div>
        </div>

        <!-- 장르 ( 전쟁 ) -->
        <div class="mt-5">
          <p class="">전쟁의 참혹함..</p>
          <div class="d-flex scroll type2">
            <div v-for="(movie, index) in mg6" :key='index'>
              <router-link :to="{ name:'MovieDetailInfoView', params: { id: movie.id } }">
              <div class="card-item effect11 left_to_right">
                <a href="#">
                  <div class="img w-100">
                    <img 
                    :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" 
                    alt="img">
                  </div>
                <div class="info">
                  <h3>{{ movie.title }}</h3>
                  <br>
                  <br>
                  <p>{{ movie.release_date }}</p>
                </div>
                </a>
              </div>
              </router-link>
            </div>
          </div>
        </div>

        <!-- 배우 카테고리 분류 시작 -->

        <!-- 배우 (톰쿠르즈) -->
        <div class="mt-5">
          <p class="">탑건의 톰크루즈가 출연한 영화</p>
          <div class="d-flex scroll type2">
            <div v-for="(movie, index) in mg6" :key='index'>
              <router-link :to="{ name:'MovieDetailInfoView', params: { id: movie.id } }">
              <div class="card-item effect11 left_to_right">
                <a href="#">
                  <div class="img w-100">
                    <img 
                    :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" 
                    alt="img">
                  </div>
                <div class="info">
                  <h3>{{ movie.title }}</h3>
                  <br>
                  <br>
                  <p>{{ movie.release_date }}</p>
                </div>
                </a>
              </div>
              </router-link>
            </div>
          </div>
        </div>



      <!-- 영화 카테고리 끝-->
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
// import MovieDetailInfoView from '@/views/movies/MovieDetailInfoView.vue'
import { mapGetters, mapActions } from 'vuex';


const moviesStore = 'moviesStore'

export default {
  name: 'MovieView',
  components: {
    // MovieDetailInfoView
  },
  data() {
    return {
      playMovieUrl: '',

      mg1: null,
      mg2: null,
      mg3: null,
      mg4: null,
      mg5: null,
      mg6: null,

    }
  },
  computed: {
    ...mapGetters(moviesStore, ['g1', 'g2', 'g3', 'g4', 'g5', 'g6']),
    ...mapGetters(moviesStore, ['movies', 'nowmovies', 'loading',]),
    
    videoURL() {
      return `https://www.youtube.com/embed/${this.playMovie}?autoplay=1&mute=1`
    },


  },
  

  methods: {
    // DB 영화 정보 axios요청
    ...mapActions(moviesStore, ['getMovies']),

    // DB => 현재 상영되는 영화 정보 axios요청
    ...mapActions(moviesStore, ['getNowMovies',]),

    //페이지 상단에 재생 되는 영화 유튜브ID 요청
    ...mapActions(moviesStore, ['playMovie']),

    // 사용자가 좋아요 한 영화 정보 axios 요청
    ...mapActions(moviesStore, ['getLikeMovies']),

    // 페이지 상단에 재생 되는 영화 유튜브ID 요청
    pickPlayMovie() {
      // 현재 상영 중인 영화 랜덤으로 선택 
      // const play = _.sample(this.nowmovies)
      // this.playMovie = play.youtube_key

      // 발표를 위해 현제 상영중인 영화 트레일러중 잔혹한 영상을 제거
      this.playMovie = 'kyMMq8Kz-8I'
    },

    // 홈페이지에 보여 줄 영화 카테고리 불러오기 
    getSectionMovies() {
      const m1 = _.sampleSize(this.g1, 12)
      this.mg1 = m1
      const m2 = _.sampleSize(this.g2, 12)
      this.mg2 = m2
      const m3 = _.sampleSize(this.g3, 12)
      this.mg3 = m3
      const m4 = _.sampleSize(this.g4, 12)
      this.mg4 = m4
      const m5 = _.sampleSize(this.g5, 12)
      this.mg5 = m5
      const m6 = _.sampleSize(this.g6, 12)
      this.mg6 = m6
    },

  },

  created() {

    // DB => 영화 정보 axios요청
    this.getMovies()

    // DB => 현재 상영되는 영화 정보 axios요청
    this.getNowMovies()

    // 페이지 상단에 재생 되는 영화 유튜브ID 요청
    this.pickPlayMovie()

    // 홈페이지에 보여 줄 영화 카테고리 불러오기 
    this.getSectionMovies()

    // 사용자가 좋아요 한 영화 목록 불러오기
    this.getLikeMovies()

  },
};
</script>

<style scoped>

@charset "UTF-8";

@import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cute+Font&family=Do+Hyeon&family=Pacifico&display=swap');

* {
  z-index: 1;
  font-family: 'Do Hyeon', sans-serif;
  font-size: 40px;
  font-weight: 7500;
  color: white;
  /* background-color: black; */
}
#bg{
  background-color: rgb(1, 13, 23);
}
.welcome {
  color: rgba(255, 255, 255, 0.1);
  font-size: 100px;
  font-family: 'Pacifico', cursive;
  font-weight: 100;
  animation: animateText 5s linear infinite;
  margin-left: 30%;
}
@keyframes animateText
{
  0%{
    color: rgba(255, 255, 255, 0.1);
    text-shadow: none;
  }
  100%{
    color: rgba(255, 255, 255, 1);
    text-shadow: 0 0 10px #b01558, 0 0 20px #fff, 0 0 40px #b01558, 0 0 80px #b01558, 0 0 90px #b01558, 0 0 100px #b01558, 0 0 150px #b01558;
  }
  
}


.scroll{
    width: 100%;
    /* padding: 0px 13px 0px 13px; */
    overflow-y: scroll;
    box-sizing: border-box;
    color: white;
    font-family: 'Nanum Gothic';
    /* background-color: rgba(0,0,0,0.8); */
    margin-right: 50px;
}

/* 스크롤바 설정*/
.type2::-webkit-scrollbar{
    width: 100%;
}

/* 스크롤바 막대 설정*/
.type2::-webkit-scrollbar-thumb{
    height: 17%;
    background-color: rgb(34, 36, 33);
    border-radius: 10px;  
}

/* 스크롤바 뒷 배경 설정*/
.type2::-webkit-scrollbar-track{
    background-color: rgba(71, 34, 34, 0.33);
}

#area {
  position: relative; /* absolute는 부모가 relative일 때 부모를 따라간다. */
  width: 100%;
  height: 830px;
  padding-bottom: 35%;
  padding-left: 15%; /* 16:9 비율 */
  justify-content: center;
  background-image: url('@/assets/background.jpg');
  background-size: cover;
  background-position: center;
  
}

#video {
  position: absolute;
  width: 70%; /* 부모에 맞게 꽉 채운다. */
  height: 70%;
  margin: auto;
  margin-bottom: 5%;
  margin-top: 3%;
  animation: fadein 10s;
  animation-delay: 10s; 
  -webkit-animation: fadein 5s; /* Safari and Chrome */
}
@keyframes fadein {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
.row {
    display: flex;
    flex-direction: row;

}
.card-item {
  margin-right: 20px;
    position: relative;
    -webkit-transition: all 0.35s ease-in-out;
    -moz-transition: all 0.35s ease-in-out;
    transition: all 0.35s ease-in-out;
  }
  .card-item img {
    width: 100%;
    height: 100%;
  }
  
  .card-item{
    position: relative;
    width:270px;
    height: 270px;
    border-radius: 50%;
  }
  .card-item .img {
    position: relative;
    width: 270px;
    height: 270px;
    border-radius: 50%;
  }
  .card-item .img:before {
    position: absolute;
    display: block;
    content: '';
    width: 100%;
    height: 100%;
    /* box-shadow: inset 0 0 0 16px rgba(255, 255, 255, 0.6), 0 1px 2px rgba(0, 0, 0, 0.3); */
    -webkit-transition: all 0.35s ease-in-out;
    -moz-transition: all 0.35s ease-in-out;
    transition: all 0.35s ease-in-out;
  }
  .card-item .info {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    text-align: center;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
  }
.effect11 {
    -webkit-perspective: 900px;
    -moz-perspective: 900px;
    perspective: 900px;
  }
.effect11 .img {
    opacity: 1;
    -webkit-transform-origin: 50% 50%;
    -moz-transform-origin: 50% 50%;
    -ms-transform-origin: 50% 50%;
    -o-transform-origin: 50% 50%;
    transform-origin: 50% 50%;
    -webkit-transition: all 0.35s ease-in-out;
    -moz-transition: all 0.35s ease-in-out;
    transition: all 0.35s ease-in-out;
  }
.effect11.colored .info {
    background: #1a4a72;
  }
.effect11 .info {
    background: rgb(58, 55, 55);
    opacity: 0;
    visibility: hidden;
    -webkit-transition: all 0.35s ease 0.35s;
    -moz-transition: all 0.35s ease 0.35s;
    transition: all 0.35s ease 0.35s;
  }
.effect11 .info h3 {
    color: #fff;
    text-transform: uppercase;
    position: relative;
    letter-spacing: 2px;
    font-size: 35px;
    margin: 0 30px;
    padding: 55px 0 0 0;
    height: 110px;
    text-shadow: 0 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.3);
    
  }
.effect11 .info p {
    color: #bbb;
    padding: 10px 5px;
    font-style: italic;
    margin: 0 30px;
    font-size: 20px;

  }
.effect11 a:hover .img {
    opacity: 0;
  }
.effect11 a:hover .info {
    visibility: visible;
    opacity: 1;
  }
  
.effect11.left_to_right .img {
    -webkit-transform: translateZ(0) rotateY(0);
    -moz-transform: translateZ(0) rotateY(0);
    -ms-transform: translateZ(0) rotateY(0);
    -o-transform: translateZ(0) rotateY(0);
    transform: translateZ(0) rotateY(0);
  }
.effect11.left_to_right .info {
    -webkit-transform: translateZ(-1000px) rotateY(-90deg);
    -moz-transform: translateZ(-1000px) rotateY(-90deg);
    -ms-transform: translateZ(-1000px) rotateY(-90deg);
    -o-transform: translateZ(-1000px) rotateY(-90deg);
    transform: translateZ(-1000px) rotateY(-90deg);
  }
.effect11.left_to_right a:hover .img {
    -webkit-transform: translateZ(-1000px) rotateY(90deg);
    -moz-transform: translateZ(-1000px) rotateY(90deg);
    -ms-transform: translateZ(-1000px) rotateY(90deg);
    -o-transform: translateZ(-1000px) rotateY(90deg);
    transform: translateZ(-1000px) rotateY(90deg);
  }
.effect11.left_to_right a:hover .info {
    -webkit-transform: translateZ(0) rotateY(0);
    -moz-transform: translateZ(0) rotateY(0);
    -ms-transform: translateZ(0) rotateY(0);
    -o-transform: translateZ(0) rotateY(0);
    transform: translateZ(0) rotateY(0);
  }
  
.effect11.right_to_left .img {
    -webkit-transform: translateZ(0) rotateY(0);
    -moz-transform: translateZ(0) rotateY(0);
    -ms-transform: translateZ(0) rotateY(0);
    -o-transform: translateZ(0) rotateY(0);
    transform: translateZ(0) rotateY(0);
  }
.effect11.right_to_left .info {
    -webkit-transform: translateZ(-1000px) rotateY(90deg);
    -moz-transform: translateZ(-1000px) rotateY(90deg);
    -ms-transform: translateZ(-1000px) rotateY(90deg);
    -o-transform: translateZ(-1000px) rotateY(90deg);
    transform: translateZ(-1000px) rotateY(90deg);
  }
.effect11.right_to_left a:hover .img {
    -webkit-transform: translateZ(-1000px) rotateY(-90deg);
    -moz-transform: translateZ(-1000px) rotateY(-90deg);
    -ms-transform: translateZ(-1000px) rotateY(-90deg);
    -o-transform: translateZ(-1000px) rotateY(-90deg);
    transform: translateZ(-1000px) rotateY(-90deg);
  }
.effect11.right_to_left a:hover .info {
    -webkit-transform: translateZ(0) rotateY(0);
    -moz-transform: translateZ(0) rotateY(0);
    -ms-transform: translateZ(0) rotateY(0);
    -o-transform: translateZ(0) rotateY(0);
    transform: translateZ(0) rotateY(0);
  }
  
.effect11.top_to_bottom .img {
    -webkit-transform: translateZ(0) rotateX(0);
    -moz-transform: translateZ(0) rotateX(0);
    -ms-transform: translateZ(0) rotateX(0);
    -o-transform: translateZ(0) rotateX(0);
    transform: translateZ(0) rotateX(0);
  }
.effect11.top_to_bottom .info {
    -webkit-transform: translateZ(-1000px) rotateX(90deg);
    -moz-transform: translateZ(-1000px) rotateX(90deg);
    -ms-transform: translateZ(-1000px) rotateX(90deg);
    -o-transform: translateZ(-1000px) rotateX(90deg);
    transform: translateZ(-1000px) rotateX(90deg);
  }
.effect11.top_to_bottom a:hover .img {
    -webkit-transform: translateZ(-1000px) rotateX(-90deg);
    -moz-transform: translateZ(-1000px) rotateX(-90deg);
    -ms-transform: translateZ(-1000px) rotateX(-90deg);
    -o-transform: translateZ(-1000px) rotateX(-90deg);
    transform: translateZ(-1000px) rotateX(-90deg);
  }
.effect11.top_to_bottom a:hover .info {
    -webkit-transform: translateZ(0) rotateX(0);
    -moz-transform: translateZ(0) rotateX(0);
    -ms-transform: translateZ(0) rotateX(0);
    -o-transform: translateZ(0) rotateX(0);
    transform: translateZ(0) rotateX(0);
  }
  
.effect11.bottom_to_top .img {
    -webkit-transform: translateZ(0) rotateX(0);
    -moz-transform: translateZ(0) rotateX(0);
    -ms-transform: translateZ(0) rotateX(0);
    -o-transform: translateZ(0) rotateX(0);
    transform: translateZ(0) rotateX(0);
  }
.effect11.bottom_to_top .info {
    -webkit-transform: translateZ(-1000px) rotateX(-90deg);
    -moz-transform: translateZ(-1000px) rotateX(-90deg);
    -ms-transform: translateZ(-1000px) rotateX(-90deg);
    -o-transform: translateZ(-1000px) rotateX(-90deg);
    transform: translateZ(-1000px) rotateX(-90deg);
  }
.effect11.bottom_to_top a:hover .img {
    -webkit-transform: translateZ(-1000px) rotateX(90deg);
    -moz-transform: translateZ(-1000px) rotateX(90deg);
    -ms-transform: translateZ(-1000px) rotateX(90deg);
    -o-transform: translateZ(-1000px) rotateX(90deg);
    transform: translateZ(-1000px) rotateX(90deg);
  }
.effect11.bottom_to_top a:hover .info {
    -webkit-transform: translateZ(0) rotateX(0);
    -moz-transform: translateZ(0) rotateX(0);
    -ms-transform: translateZ(0) rotateX(0);
    -o-transform: translateZ(0) rotateX(0);
    transform: translateZ(0) rotateX(0);
  }


</style>