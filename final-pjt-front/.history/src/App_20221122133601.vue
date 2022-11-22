<template>
  <div id="app">
    <body>
    <header id="header">
      <div class="header">
        <!-- <div class="header_wrapper"> -->
        <h1 class="logo">
          <img id="logo" src="https://e7.pngegg.com/pngimages/941/692/png-clipart-black-small-apple-logo-logo-material-apple-logo.png" alt="logo" />
        </h1>

        <nav>
          <ul>
            <li>
              <div class="list">
                <h3 class="nav_text">nav1</h3>
                <div class="hidden_nav_list">
                  <a href="">
                    <p class="hidden_nav_list_text">nav1-1</p>
                  </a>
                  <a href="">
                    <p class="hidden_nav_list_text">nav1-2</p>
                  </a>
                  <a href="">
                    <p class="hidden_nav_list_text">nav1-3</p>
                  </a>
                  <a href="">
                    <p class="hidden_nav_list_text">nav1-4</p>
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
                <h3 class="nav_text">nav3</h3>
                <div class="hidden_nav_list">
                  <a href="">
                    <p class="hidden_nav_list_text">nav3-1</p>
                  </a>
                  <a href="">
                    <p class="hidden_nav_list_text">nav3-2</p>
                  </a>
                  <a href="">
                    <p class="hidden_nav_list_text">nav3-3</p>
                  </a>
                  <a href="">
                    <p class="hidden_nav_list_text">nav3-4</p>
                  </a>
                </div>
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
          </ul>
        </nav>
        <!-- </div> -->

        <div class="header_button_group">
          <button class="header_button_signin">Sign in</button>
          <button class="header_button_signup">Sign up</button>
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

    <router-view/>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

const moviesStore = 'moviesStore'

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
      this.headerBtnSignin[0].style.color = '#000';
      this.logo.src = 'https://e7.pngegg.com/pngimages/941/692/png-clipart-black-small-apple-logo-logo-material-apple-logo.png';
      Object.values(this.navText).map((text) => (text.style.color = '#000'));
      Object.values(this.hiddenNavText).map((text) => {
        text.style.display = 'block';
        text.style.color = '#000';
      });
    },
    handleLeaveHeader() {
      this.header.style.backgroundColor = 'rgba(0,0,0,0.5)';
      this.header.style.height = '100px';
      this.headerBtnSignin[0].style.color = '#fff';
      this.logo.src = 'https://e7.pngegg.com/pngimages/941/692/png-clipart-black-small-apple-logo-logo-material-apple-logo.png';
      Object.values(this.navText).map((text) => (text.style.color = '#fff'));
      Object.values(this.hiddenNavText).map((text) => {
        text.style.display = 'none';
        text.style.color = '#000';
      });
    },
    
  },
  computed: {
    ...mapGetters('accountsStore', ['isLogin']),
    ...mapGetters('accountsStore', ['nickname']),
  },
  created() {
    this.getMovies(),
    this.getNowMovies()
  },
  mounted() {
    this.header = this.getId('header');
    this.logo = this.getId('logo');
    this.navText = this.getClass('nav_text');
    this.hiddenNavText = this.getClass('hidden_nav_list_text');
    this.headerBtnSignin = this.getClass('header_button_signin');
    console.log(this.header);
    this.header.addEventListener('mouseover', this.handleHoverHeader);
    this.header.addEventListener('mouseleave', this.handleLeaveHeader);
  }
};
</script>

<style>

nav {
  padding: 30px;
  z-index: 1;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
