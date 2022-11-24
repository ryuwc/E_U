<template>
  <div id="bg">
    <div>
      
      <!-- 영상 재생 -->
      <div>
        <div id='area'>
          <!-- <h2 style="padding-top: 70px;" class="welcome">Welcome</h2> -->
          <iframe style="margin-top: 120px;" id='video' :src=videoURL
          frameborder="0" allow="autoplay">
          </iframe>
        </div>
      </div>

    <!-- 영화 카테고리 시작-->
    <div class="mx-5" style="margin-top:4%">
  

      <!-- 사용자들이 가장 많이 조회한 영화 순위별 추천 -->

      <h1>실시간 인기 영화</h1>
      <div class="grid d-flex md:gap-10 scroll type2">
        <div class="relative m-auto overflow-hidden rounded-lg shadow-lg group"
          v-for="(movie, index) in userClickMovies" :key='index'>
          <router-link :to="{ name:'MovieDetailInfoView', params: { id: movie.id } }">
            <img style="width: 100%; height: 20vw;" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`">
          </router-link>
            <div style="position: relative; left:10px; top: -15px;"><h1 class="d-flex" id="rank">{{index+1}}</h1></div>
        </div>  
      </div>

      
      <div class="category" style="margin-top:4%">
        <h1 style="font-size:50px">{{ user.nickname }}님이 좋아할 만한 영화</h1>
      </div>

      <!-- 찜 한 목록에 가장 많이 등장한 장르 영화 추천-->
      <div class="mt-5">
        <p class="">당신이 좋아할 만한 장르</p>
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

      <!-- 찜 한 목록에 등장한 배우가 출현한 영화 추천-->
      <div class="mt-5">
        <p class="">당신이 선택한 배우가 출현한 영화</p>

        <div class="d-flex scroll type2">
          <div v-for="(movie, index) in actorMoviesWishList" :key='index'>
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
const accountsStore = 'accountsStore'

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

      // 현재 유저가 위시리스트에 담은 영화들에서 관련 배우들이 출연한 영화들을 저장할 빈 배열
      actorMoviesWishList: [],
    }
  },
  computed: {
    ...mapGetters(moviesStore, ['g1', 'g2', 'g3', 'g4', 'g5', 'g6']),
    ...mapGetters(moviesStore, ['movies', 'nowmovies', 'loading', 'nowUserWishList']),
    ...mapGetters(accountsStore, ['user', 'authHead']),
    nowUser() {
      return JSON.parse(JSON.stringify(this.user))
    },
    
    videoURL() {
      return `https://www.youtube.com/embed/2JomSAO_TGo?autoplay=1&mute=1`
      // return `https://www.youtube.com/embed/CkeiTBtCm7Y?autoplay=1&mute=1`
      // return `https://www.youtube.com/embed/WscLMTs-9Rw?autoplay=1&mute=1`
      // return `https://www.youtube.com/embed/p0_F0R1AWiA?autoplay=1&mute=1`
    },
    // 유저의 클릭수가 제일 많은 영화를 순서대로 나열 (user_click 키가 0이면 안가져옴)
    tempUserClickMovies() {
      return _.orderBy(this.movies, ['user_click'], ['desc']).filter(movie => movie.user_click > 0)
    },
    // 클릭수가 0 이상인 영화가 7개 이상이면 클릭수가 높은 순으로 6개 까지만 나열 (20개 이하면 모두 나열)
    userClickMovies() {
      if (this.tempUserClickMovies.length > 6) {
        return this.tempUserClickMovies.slice(0, 6)
      }
       else {
        return this.tempUserClickMovies
       }
    } 

  },

  methods: {
    // DB 영화 정보 axios요청
    ...mapActions(moviesStore, ['getMovies']),

    // DB => 현재 상영되는 영화 정보 axios요청
    ...mapActions(moviesStore, ['getNowMovies',]),

    //페이지 상단에 재생 되는 영화 유튜브ID 요청
    ...mapActions(moviesStore, ['playMovie']),

    // 사용자가 좋아요 한 영화 정보 axios 요청
    ...mapActions(moviesStore, ['getNowUserWishList']),

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
      console.log('main실행');

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
    // 현재 유저의 위시리스트에 담긴 영화 정보 중 배우들이 출연한 다른 영화들을 불러오는 함수
    getActorInNowWishList() {
      // 현재 유저의 위시리스트에 담긴 영화들의 배우들이 출연한 영화들을 불러온다.
      this.movies.forEach(movie => {
        movie.actors.forEach(actor => {
          this.nowUserWishList.forEach(wishMovie => {
            wishMovie.actors.forEach(wishActor => {
              if (actor === wishActor) {
                this.actorMoviesWishList.push(movie)
              }
            })
          })
        })
        // 중복된 영화들을 제거한다.
        this.actorMoviesWishList = _.uniqBy(this.actorMoviesWishList, 'id')

      })
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
    this.nowUser['userId'] = this.nowUser['id']
    this.nowUser['authHead'] = this.authHead
    this.getNowUserWishList(this.nowUser)
    this.getActorInNowWishList()
    
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
  color: black;
  /* background-color: black; */
}
#rank{
  font-size: 40px;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  color: black;
  text-shadow: -2px 0 rgb(255, 255, 255), 0 2px rgb(255, 255, 255), 2px 0 rgb(255, 255, 255), 0 -2px rgb(255, 255, 255);
}
#bg{
  /* background-color: rgb(1, 13, 23); */
  background: linear-gradient(#b4daf3, #fff, #b4daf3, #fff, #b4daf3, #fff, #b4daf3, #fff, #b4daf3, #fff);
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
    background-color: #98cff5;
    border-radius: 10px;  
}

/* 스크롤바 뒷 배경 설정*/
.type2::-webkit-scrollbar-track{
    background-color: #b4daf3;
}

#area {
  position: relative; /* absolute는 부모가 relative일 때 부모를 따라간다. */
  width: 100%;
  height: 995px;
  padding-bottom: 35%;
  padding-left: 15%; /* 16:9 비율 */
  justify-content: center;
  /* background-image: url('https://www.ghibli.jp/gallery/kazetachinu024.jpg'); */
  /* background-image: url('https://www.ghibli.jp/gallery/kazetachinu022.jpg'); */
  /* background-image: url('https://www.ghibli.jp/gallery/kazetachinu023.jpg'); */
  /* background-image: url('https://www.ghibli.jp/gallery/kazetachinu019.jpg'); */
  background-image: url('https://www.ghibli.jp/gallery/ponyo049.jpg');
  background-size: cover;
  background-position: center;
  
}

#video {
  position: absolute;
  width: 65%; /* 부모에 맞게 꽉 채운다. */
  height: 745px;
  margin: auto;
  margin-bottom: 5%;
  margin-top: 3%;
  animation: fadein 10s;
  animation-delay: 10s; 
  -webkit-animation: fadein 3s; /* Safari and Chrome */
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
  border-radius: 20px;
  margin-right: 20px;
    position: relative;
    -webkit-transition: all 0.35s ease-in-out;
    -moz-transition: all 0.35s ease-in-out;
    transition: all 0.35s ease-in-out;
  }
  .card-item img {
      border-radius: 20px;
    width: 100%;
    height: 100%;
  }
  
  .card-item{
      border-radius: 20px;
    position: relative;
    width:270px;
    height: 270px;
    border-radius: 50%;
  }
  .card-item .img {
      border-radius: 20px;
    position: relative;
    width: 270px;
    height: 270px;
    border-radius: 50%;
  }
  .card-item .img:before {
      border-radius: 20px;
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
      border-radius: 20px;
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
    border-radius: 20px;
    -webkit-perspective: 900px;
    -moz-perspective: 900px;
    perspective: 900px;
  }
.effect11 .img {
    border-radius: 20px;
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
    border-radius: 20px;
    background: #1a4a72;
  }
.effect11 .info {
    border-radius: 20px;
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