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
    allGenres: [
      { id: 12, name: '모험' },
      { id: 14, name: '판타지' },
      { id: 16, name: '애니메이션' },
      { id: 18, name: '드라마' },
      { id: 27, name: '공포' },
      { id: 28, name: '액션' },
      { id: 35, name: '코미디' },
      { id: 36, name: '역사' },
      { id: 37, name: '서부' },
      { id: 53, name: '스릴러' },
      { id: 80, name: '범죄' },
      { id: 99, name: '다큐멘터리' },
      { id: 878, name: 'SF' },
      { id: 9648, name: '미스터리' },
      { id: 10402, name: '음악' },
      { id: 10749, name: '로맨스' },
      { id: 10751, name: '가족' },
      { id: 10752, name: '전쟁' },
      { id: 10770, name: 'TV 영화' },
      // 12: "모험",
      // 14: "판타지",
      // 16: "애니메이션",
      // 18: "드라마",
      // 27: "공포",
      // 28: "액션",
      // 35: "코미디",
      // 36: "역사",
      // 37: "서부",
      // 53: "스릴러",
      // 80: "범죄",
      // 99: "다큐멘터리",
      // 878: "SF",
      // 9648: "미스터리",
      // 10402: "음악",
      // 10749: "로맨스",
      // 10751: "가족",
      // 10752: "전쟁",
      // 10770: "TV 영화"
    ],
  },
  getters: {
    movies: (state) => state.movies,
    nowmovies: (state) => state.nowmovies,
    movie: (state) => state.movie,
    reviews: (state) => state.reviews,
    loading: (state) => state.loading,
    allGenres: (state) => state.allGenres,
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