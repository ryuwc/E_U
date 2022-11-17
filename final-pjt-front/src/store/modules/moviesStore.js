import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

const moviesStore = {
  namespaced: true,
  state: {
    movies: null,
    nowmovies: null,
  },
  getters: {
  },
  mutations: {
    SET_MOVIES (state, movies){
      state.movies = movies
      console.log('movie', state.movies)
    },
    SET_NOW_MOVIES (state, nowmovies){
      state.nowmovies = nowmovies
      console.log('now_movie',state.nowmovies)
    },
  },
  actions: {
    getMovies({ commit }) {
      axios({
        method: "get",
        url: `${API_URL}/movies/`,
      })
      .then(res => {
        commit('SET_MOVIES', res.data);
      })
      .catch(err => {
        console.log(err);
      })
    },

    getNowMovies({ commit }) {
      console.log('bb')
      axios({
        method: "get",
        url: `${API_URL}/movies/now/`,
      })
      .then(res => {
        console.log('res응답' ,res)
        commit('SET_NOW_MOVIES', res.data);
      })
      .catch(err => {
        console.log(err);
      })
    }
  }
}

export default moviesStore