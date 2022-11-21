import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

const moviesStore = {
  namespaced: true,
  state: {
    movies: null,
    nowmovies: null,
    movie: null,
    movieId: null,
    reviews: null,
    loading: false,
    allGenres: 
      {
      12: "모험",
      14: "판타지",
      16: "애니메이션",
      18: "드라마",
      27: "공포",
      28: "액션",
      35: "코미디",
      36: "역사",
      37: "서부",
      53: "스릴러",
      80: "범죄",
      99: "다큐멘터리",
      878: "SF",
      9648: "미스터리",
      10402: "음악",
      10749: "로맨스",
      10751: "가족",
      10752: "전쟁",
      10770: "TV 영화"
    },
  },
  getters: {
    movies: (state) => state.movies,
    nowmovies: (state) => state.nowmovies,
    movie: (state) => state.movie,
    movieId: (state) => state.movieId,
    reviews: (state) => state.reviews,
    loading: (state) => state.loading,
    allGenres: (state) => state.allGenres,
    // 장르별 영화들
    genre12: (state) => state.movies.filter((movie) => movie.genre_ids.includes(12)),
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

    getMovieDetail({ state, commit, getters }, movieId) {
      axios({
        method: "get",
        url: `${API_URL}/movies/${movieId}/`,
      })
      .then(res => {
        // console.log(res);
        const thisMovieGenre = []
        const movie = {...res.data, thisMovieGenre}
        const keys = Object.keys(getters.allGenres);
        for(let i = 0; i < keys.length; i++) {
        const key = keys[i];
        const value = getters.allGenres[key];
        for (let i = 0; i < movie.genres.length; i++) {
          if (movie.genres[i] === Number(key)) {
            movie.thisMovieGenre.push(value);
          }
        }
      }
        state.movieId = movieId
        commit("GET_MOVIE", movie);
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