<template>
  <div id="app">
    <body>
      <header id="header">
        <div class="header">
          <router-link to="/home"
            ><img src="./image/logo.png" style="width: 65px; height: 65px; margin-left: 100px; margin-top: 20px; margin-bottom: 20px"
          /></router-link>

          <nav>
            <ul>
              <li>
                <div class="list">
                  <h3 class="nav_text">임시</h3>
                  <div class="hidden_nav_list">
                    <a href="">
                      <router-link to="/home"><p class="hidden_nav_list_text">Home</p></router-link>
                    </a>
                    <a href="" @click.prevent="logOut">
                      <p class="hidden_nav_list_text">로그아웃</p>
                    </a>
                    <a href="">
                      <router-link to="/edit"><p class="hidden_nav_list_text">정보수정</p></router-link>
                    </a>
                    <a href="">
                      <router-link to="/profile"><p class="hidden_nav_list_text">프로필</p></router-link>
                    </a>
                  </div>
                </div>
              </li>
              <li>
                <div class="list">
                  <h3 class="nav_text">nav2</h3>
                  <div class="hidden_nav_list">
                    <a href="">
                      <p class="hidden_nav_list_text">nav2-1</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav2-2</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav2-3</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav2-4</p>
                    </a>
                  </div>
                </div>
              </li>
              <li>
                <div class="list">
                  <router-link to="/random"
                    ><a href=""><h3 class="nav_text">랜덤영화</h3></a></router-link
                  >
                </div>
              </li>
              <li>
                <div class="list">
                  <h3 class="nav_text">nav4</h3>
                  <div class="hidden_nav_list">
                    <a href="">
                      <p class="hidden_nav_list_text">nav4-1</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav4-2</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav4-3</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav4-4</p>
                    </a>
                  </div>
                </div>
              </li>
              <li v-if="isLogin" style="margin-left: 600px;">
                <div class="dropdown">
                  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                  </button>
                  <ul style="border: none;" class="dropdown-menu">
                    <li><a id="profilemenu" class="dropdown-item" href="#">Action</a></li>
                    <li><a id="profilemenu" class="dropdown-item" href="#">Another action</a></li>
                    <li><a id="profilemenu" class="dropdown-item" href="#">Something else here</a></li>
                  </ul>
                </div>
              </li>
            </ul>
          </nav>

          <div class="header_button_group">
            <router-link v-if="!isLogin" to="/login"><button class="header_button_signin" style="color: black">Sign in</button></router-link>
            <router-link v-if="!isLogin" to="/signup"><button class="header_button_signup">Sign up</button></router-link>
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

  data() {
    return {
      header: null,
      logo: null,
      navText: null,
      hiddenNavText: null,
      headerBtnSignin: null,
    };
  },
  methods: {
    ...mapActions('accountsStore', ['logOut']),
    ...mapActions(moviesStore, ['getMovies']),
    ...mapActions(moviesStore, ['getNowMovies']),
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
      this.header.style.height = '250px';
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
  },
  computed: {
    ...mapGetters('accountsStore', ['isLogin', 'nickname', 'username']),
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
  height: 98px;
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
</style>
