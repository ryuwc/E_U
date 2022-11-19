import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

const moviesStore = {
  namespaced: true,
  state: {
    movies: null,
    nowmovies: null,
    movie: null,
    reviews: null,
    loading: false,
  },
  getters: {
    movies: (state) => state.movies,
    nowmovies: (state) => state.nowmovies,
    movie: (state) => state.movie,
    reviews: (state) => state.reviews,
    loading: (state) => state.loading,
  },
  mutations: {
    GET_MOVIES (state, movies){
      state.movies = movies
      // console.log('movie', state.movies)
      state.loading = true
    },
    GET_NOW_MOVIES (state, nowmovies){
      state.nowmovies = nowmovies
      console.log('now_movie',state.nowmovies)
    },
    GET_MOVIE: (state, movie) => (state.movie = movie),
    GET_REVIEW: (state, reviews) => (state.reviews = reviews),


  },
  actions: {
    getMovies({ commit }) {
      axios({
        method: "get",
        url: `${API_URL}/movies/`,
      })
      .then(res => {
        commit('GET_MOVIES', res.data);
      })
      .catch(err => {
        console.log(err);
      })
    },

    getNowMovies({ commit }) {
      axios({
        method: "get",
        url: `${API_URL}/movies/now/`,
      })
      .then(res => {
        console.log('res응답' ,res)
        commit('GET_NOW_MOVIES', res.data);
      })
      .catch(err => {
        console.log(err);
      })
    },

    getMovieDetail({ commit }, movieId) {
      axios({
        method: "get",
        url: `${API_URL}/movies/${movieId}/`,
      })
      .then(res => {
        // console.log(res);
        commit("GET_MOVIE", res.data);
      })
      .catch(err => {
        console.log(err);
      })
    },

    getReview({ commit }, movieId) {
      axios({
        method: "get",
        url: `${API_URL}/movies/${movieId}/review/`,
      })
      .then(res => {
        console.log(res);
        commit("GET_REVIEW", res.data);
      })
      .catch(err => {
        console.log(err);
      })
    },


  }
}

export default moviesStore