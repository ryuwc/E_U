<template>
  <div id="_body">
    <h3 class="my-8 text-transparent bg-clip-text bg-gradient-to-r from-purple-500 via-pink-500 to-rose-500">아래 영화가 마음에 드신다면 Add! 아니면 Pass!</h3>
    <div id="card">
      <div id="imgBx">
        <img id="img" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" alt="">
      </div>
      <div id="details">
          <h1>{{ movie.title }}<br><span style="font-size: 26px;">{{ movie.thisMovieGenre.join(', ') }}</span><br></h1>
          
        <h4 style="font-size: 17px;">{{ movie.release_date }} 개봉</h4>
        <br>
        <p>{{ movie.overview }}</p>
        <div style="position: absolute; bottom: 30px; left: 0;" id="wishBtn" class="flex justify-center">
          <button style="background: #4646CD; border: none;" class="w-32 ml-20 mr-10 text-xl hover:scale-110"
          @click="[addMovieToWishList({ movieId: movie.id, nowUser: nowUser, authHead: authHead }), getRandomMovie()]"
          >Add!</button>
          <button style="background: #FF28A7; border: none;" class="w-32 mx-10 text-xl hover:scale-110"
          @click="getRandomMovie"
          >Pass!</button>
        </div>
      </div>
  </div>
  <div class="pt-12 text-center">
      <router-link to="/home"><button type="button" class="inline-flex items-center justify-center px-4 py-2 space-x-2 font-semibold leading-6 text-white bg-purple-700 border border-purple-700 rounded focus:outline-none hover:text-white hover:bg-purple-800 hover:border-purple-800 focus:ring focus:ring-purple-500 focus:ring-opacity-50 active:bg-purple-700 active:border-purple-700">
        <span class="text-lg">Let's Go!</span>
        <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 hi-solid hi-arrow-right"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
      </button></router-link>
    </div>  
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import _ from 'lodash';
const moviesStore = 'moviesStore';
const accountsStore = 'accountsStore';
const commentsStore = "commentsStore";
export default {
  name: 'AddWishListView',
  data() {
    return {
      nowMovie: null,
    };
  },
  computed: {
    ...mapGetters(moviesStore, ['movies', 'movie']),
    ...mapGetters(accountsStore, ['user', 'authHead']),
    nowUser() {
      return JSON.parse(JSON.stringify(this.user))
    },
  },
  methods: {
    ...mapActions(commentsStore, ['createProfileUser']),
    ...mapActions(moviesStore, ['getMovieDetail', 'addMovieToWishList']),
    getRandomMovie() {
      const randomMovie = _.sample(this.movies);
      this.nowMovie = randomMovie;
      this.getMovieDetail(this.nowMovie.id);
      // console.log(this.nowMovie);
    },
  },
  mounted() {
    this.getRandomMovie();
    setTimeout(() => {
      console.log(this.nowUser, '@@@@')
      this.createProfileUser({ usernumber: this.nowUser.id, authHead: this.authHead });
    }, 500);
  },
};
</script>

<style scoped>
#_body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(#4ba9e9, #4ba9e9 50%, #fff 50%, #fff 100%);
}
#card {
  position: relative;
  width: 500px; 
  height: 600px;
  background: #000;
  box-shadow: 0 15px 45px rgba(0, 0, 0, 0.1);
  display: flex;
  overflow: hidden;
  transition: 0.5s ease-in-out;
  animation: fadein 3s;
}
@keyframes fadein {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
#card:hover {
  width: 1000px; 
}
#imgBx {
  position: relative; 
  min-width: 500px; height: 
  100%; background: #fff; 
  display: flex; 
  justify-content: center; 
  align-items: center;
  overflow: hidden;
  z-index: 0;
}
#img {
  max-width: 500px;
}
#details {
  position: relative;
  width: 500px;
  height: 100%;
  background: #4ba9e9;
  display: flex;
  /* justify-content: center; */
  /* align-items: center; */
  padding: 20px;
  flex-direction: column;
  z-index: 1;
}
#details::before {
  content: '';
  position: absolute;
  left: 0;
  width: 0;
  height: 0;
  border-top: 10px solid transparent;
  border-bottom: 10px solid transparent;
  border-left: 10px solid #fff;
}
#details h3 {
  text-transform: uppercase;
  font-weight: 600;
  font-size: 1.5em;
  line-height: 1em;
}
</style>