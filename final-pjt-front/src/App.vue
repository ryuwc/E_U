<template>
  <div id="app">
    <body>
      <header id="header">
        <div class="header">
          <router-link style="margin-left: 100px; position: relative;" to="/home">
            <img src="./image/logo2.png" style="width: 65px; height: 65px; margin-left: 100px; margin-top: 20px; margin-bottom: 20px"
          /></router-link>
          <nav>
            <ul>
              <li style="margin-left: 100px;">
                <div class="list">
                  <router-link to="/allmovies"><h3 style="font-size: 40px;" class="nav_text">Movie</h3></router-link>
                  <div class="hidden_nav_list">
                    <a href="">
                      <router-link to="/allmovies"><p style="font-size: 25px;" class="hidden_nav_list_text">전체영화</p></router-link>
                    </a>
                    <a href="">
                      <router-link to="/nowmovies"><p style="font-size: 25px;" class="hidden_nav_list_text">최신영화</p></router-link>
                    </a>
                    
                    <!-- 우리가 추천하는 영화 라우터 링크 걸어놈 -->
                    <a href="">
                      <router-link to="/werecommendmovies"><p style="font-size: 25px; width: 160px;" class="text-transparent hidden_nav_list_text">이:유 추천영화</p></router-link>
                    </a>
                  </div>
                </div>
              </li>
              <li>
                <div class="list">
                  <router-link to="/feeling"
                    ><a href=""><h3 style="font-size: 40px;" class="nav_text">Feel</h3></a></router-link
                  >
                </div>
              </li>
              <li>
                <div class="list">
                  <router-link to="/random"
                    ><a href=""><h3 style="font-size: 40px; width: 140px;" class="nav_text">Random</h3></a></router-link
                  >
                </div>
              </li>
              
              <!-- 서치바 -->
              <li style="margin-left: 200px; width: 360px;">
                <div id="searchBox">
                  <div id="search" @click="searchClick">
                    <i style="color: black;" class="fa-solid fa-magnifying-glass"></i>
                  </div>
                <div id="searchInput">
                  <input style="background: rgba(255, 255, 255, 0.5); color: black;"  type="text" placeholder="영화를 검색해주세요!"
                  v-model="searchContent" @keyup.enter="[searchMoviesFind(searchContent), searchClick()]" />
                  >
                </div>
                <div id="close" @click="searchClick">
                  <i style="color: black;" class="fa-solid fa-xmark"></i>
                </div>
                </div>
              </li>
              
              <!-- 유저 프로필 -->
              <li v-if="isLogin" style="margin-left: 0px;">
                <div class="dropdown hover:scale-125">
                  <div class="" type="button" data-bs-toggle="dropdown">
                    <img :src="user.profile_path" alt="Avatar Photo" class="w-16 h-16" />
                  </div>
                  <ul style="border: none;background-color: rgba(0, 0, 0, 0);position: absolute;inset: 0px auto auto 0px;margin: 0px;transform: translate(0px, 50px);position: relative;" class="dropdown-menu">
                    <li @click="[getProfileUser({ user: user.id, nickname: nickname })]"><router-link :to="{ name:'ProfileView', params: { id: user.id } }"><a id="profilemenu" class="dropdown-item" href="#"> 프로필</a></router-link></li>
                    <li><router-link to="/edit"><a id="profilemenu" class="dropdown-item" href="#">정보수정</a></router-link></li>
                    <li @click.prevent="logOut"><a id="profilemenu" class="dropdown-item" href="#">로그아웃</a></li>
                  </ul>
                </div>
              </li>
            </ul>
          </nav>

          <div class="header_button_group">
            <router-link v-if="!isLogin" to="/login"><button class="header_button_signin" style="color: black; background-color: white; width: 80px;">Sign in</button></router-link>
            <router-link v-if="!isLogin" to="/signup"><button class="header_button_signup" style="width: 80px;">Sign up</button></router-link>
          </div>
        </div>
      </header>
    </body>

    <!-- 임시로 사용한 네브바 -->
    <!-- <nav>
      <router-link  to="/home">| Home |</router-link>
      <router-link v-if="!isLogin" to="/signup">| Sign Up |</router-link>
      <router-link v-if="!isLogin" to="/login">Login |</router-link>
      <button v-if="isLogin" @click="logOut">로그아웃 |</button>
      <router-link v-if="isLogin" to="/edit">정보수정</router-link> |
      <router-link v-if="isLogin" to="/profile">Profile |</router-link>
      <router-link to="/practice">연습</router-link> |
    </nav> -->

    <router-view />
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

const moviesStore = 'moviesStore';

export default {
  name: 'App',
  components: {
  },

  data() {
    return {
      header: null,
      logo: null,
      navText: null,
      hiddenNavText: null,
      headerBtnSignin: null,
      searchContent: null,
      searchMovies: null,
    };
  },
  methods: {
    ...mapActions('accountsStore', ['getProfileUser','logOut']),
    ...mapActions(moviesStore, ['getNowMovies', 'searchMoviesFind', 'getMovies']),
    getId: (id) => {
      return document.getElementById(id);
    },
    getClass: (className) => {
      return document.getElementsByClassName(className);
    },
    test() {
      return console.log(this.getId('header'));
    },
    handleHoverHeader() {
      this.header.style.backgroundColor = '#fff';
      this.header.style.height = '270px';
      // if (this.headerBtnSignin) {
      //   this.headerBtnSignin[0].style.color = '#000';
      // }
      // this.logo.src = 'https://e7.pngegg.com/pngimages/941/692/png-clipart-black-small-apple-logo-logo-material-apple-logo.png';
      Object.values(this.navText).map((text) => (text.style.color = '#000'));
      Object.values(this.hiddenNavText).map((text) => {
        text.style.display = 'block';
        text.style.color = '#000';
      });
    },
    handleLeaveHeader() {
      this.header.style.backgroundColor = 'rgba(0,0,0,0)';
      this.header.style.height = '100px';
      // if (this.headerBtnSignin) {
      //   this.headerBtnSignin[0].style.color = '#fff';
      // }
      // this.logo.src = 'https://e7.pngegg.com/pngimages/941/692/png-clipart-black-small-apple-logo-logo-material-apple-logo.png';
      Object.values(this.navText).map((text) => (text.style.color = '#fff'));
      Object.values(this.hiddenNavText).map((text) => {
        text.style.display = 'none';
        text.style.color = '#000';
      });
    },
    main: () => {
      // header = this.getId('header');
    },
    searchClick() {
      const searchBox = document.querySelector('#searchBox');
      searchBox.classList.toggle('active');
    },
  },
  computed: {
    ...mapGetters('accountsStore', ['isLogin', 'nickname', 'username', 'user']),
    ...mapGetters(moviesStore, ['movies']),
  },
  created() {
    this.getMovies(), this.getNowMovies();
  },
  mounted() {
    this.header = this.getId('header');
    this.logo = this.getId('logo');
    this.navText = this.getClass('nav_text');
    this.hiddenNavText = this.getClass('hidden_nav_list_text');
    this.headerBtnSignin = this.getClass('header_button_signin');
    // console.log(this.header);
    this.header.addEventListener('mouseover', this.handleHoverHeader);
    this.header.addEventListener('mouseleave', this.handleLeaveHeader);
  },
};
</script>

<style>
#profilemenu:hover {
  background-color: white;
}

* {
  font-family: 'Jua', sans-serif;
}

body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background-color: white;
  color: white;
  font-family: 'Noto Sans KR', sans-serif;
}

body::-webkit-scrollbar {
  display: none;
}

h1,
h2,
h3,
h4,
h5,
h6,
ul,
li,
p {
  margin: 0;
  padding: 0;
}

ul {
  display: flex;
  height: 100%;
  list-style-type: none;
  color: inherit;
}

li {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 120px;
  height: 100%;
  text-align: center;
  margin-right: 80px;
}

a {
  text-decoration: none;
  color: inherit;
}

button {
  background-color: #000;
  padding: 8px 12px;
  border: 1px solid #000;
  cursor: pointer;
  border-radius: 3px;
  color: white;
  height: fit-content;
}

button:hover {
  transform: scale(1.05);
}

button:active {
  transform: scale(0.97);
}

header {
  position: absolute;
  top: 0;
  width: 100%;
  /* height: 300px; */
  height: 90px;
  transition: 0.2s ease-in-out;
  z-index: 100;
  background-color: rgba(0, 0, 0, 0);
  overflow: hidden;
}

#header {
  display: flex;
  justify-content: space-between;
}

.header {
  display: flex;
  justify-content: space-between;
  width: 1280px;
  height: 100px;
}

.header_wrapper {
  display: flex;
  justify-content: space-between;
  /* width: 1280px; */
}

.logo {
  display: flex;
  align-items: center;
  width: 100px;
  height: 100px;
}

.logo img {
  width: 100%;
}

.header_button_group {
  display: flex;
  align-items: center;
  height: 100%;
}

.header_button_signin {
  margin-right: 15px;
  background-color: transparent;
}

.list {
  position: relative;
}

.hidden_nav_list {
  position: absolute;
  top: 60px;
  left: 0;
  width: 120px;
  text-align: left;
}

.hidden_nav_list p {
  margin-bottom: 12px;
  cursor: pointer;
}

.section {
  position: relative;
  width: 100vw;
  height: 100vh;
  transition: all 700ms ease 0s;
}

.section_text {
  position: absolute;
  display: flex;
  justify-content: center;
  width: 100vw;
  z-index: 2;
  top: 150px;
}

.section_header {
  top: 200px;
}

.section_text div {
  width: 1280px;
}

.section_text h2 {
  font-size: 64px;
  text-shadow: 2px 2px 2px #000;
}

.img {
  position: absolute;
  width: 100%;
  height: 100vh;
}

.img img {
  width: 100%;
  height: 100vh;
}

.more_btn {
  top: unset;
  bottom: 100px;
}

.more_btn button {
  width: 200px;
  height: 40px;
  background-color: #eee;
  border: 1px solid #000;
  color: #000;
  border: none;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
}

#section_1_title,
#section_2_title,
#section_3_title,
#section_4_title,
#section_5_title,
#section_6_title {
  opacity: 0;
  transition: 0.5s ease-in-out;
  transition-delay: 0.5s;
  margin-left: 100px;
}

#section_6_btn {
  opacity: 0;
  transition: 0.5s ease-in-out;
  transition-delay: 0.5s;
  transform: translateY(100px);
}

#section_1_title {
  margin-left: 0;
}

.balls {
  width: 10em;
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
  justify-content: space-between;
}

.balls div {
  width: 3em;
  height: 3em;
  border-radius: 50%;
  background-color: #fc2f70;
  transform: translateY(-100%);
  animation: wave 3s ease-in-out alternate infinite;
}

.balls div:nth-of-type(1) {
  animation-delay: -0.4s;
}

.balls div:nth-of-type(2) {
  animation-delay: -0.2s;
}
.balls div:nth-of-type(3) {
  animation-delay: -0.1s;
}

@keyframes wave {
  from {
    transform: translateY(-50%);
  }
  to {
    transform: translateY(50%);
  }
}

#searchBox {
  position: relative;
  width: 58px;
  height: 60px;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 30px;
  display: flex;
  justify-content: space-between;
  transition: 0.5s;
  overflow: hidden;
  /* box-shadow: 0 25px 35px rgba(0, 0, 0, 0.1); */
}

#searchBox.active {
  width: 360px;
}

#searchBox #search {
  position: relative;
  min-width: 60px;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
  justify-content: center;
  font-size: 1.5em;
  cursor: pointer;
}

#searchBox #close {
  position: relative;
  width: 60px;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  font-size: 1.25em;
}

#searchBox.active #close {
  scale: 1;
  transition-delay: 0.5s;
}

#searchBox #searchInput {
  position: absolute;
  left: 60px;
  width: calc(100% - 120px);
  line-height: 60px;
  background: rgba(255, 255, 255, 0.5);
}

#searchBox #searchInput input {
  position: absolute;
  left: 0;
  width: 100%;
  height: auto;
  border: none;
  outline: none;
  font-size: 1.25em;
}
</style>
