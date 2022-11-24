import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/signup',
    name: 'SignView',
    component: () => import('../views/accounts/SignUpView.vue')
  },
  {
    path: '/login',
    name: 'LoginView',
    component: () => import('../views/accounts/LoginView.vue'),
  },
  {
    path: '/edit',
    name: 'EditUserView',
    component: () => import('../views/accounts/EditUserView.vue')
  },
  {
    path: '/profile/:id',
    name: 'ProfileView',
    component: () => import('../views/accounts/ProfileView.vue')
  },
  {
    path: '/home',
    name: 'MovieView',
    component: () => import('../views/movies/MovieView.vue')
  },
  {
    path: '/random',
    name: 'RandomMovieView',
    component: () => import('../views/movies/RandomMovieView.vue')
  },
  {
    path: '/feeling',
    name: 'FeelingMovieView',
    component: () => import('../views/movies/FeelingMovieView.vue')
  },
  {
    path: '/movies/:id',
    name: 'MovieDetailInfoView',
    component: () => import('../views/movies/MovieDetailInfoView.vue')
  },
  {
    path: '/',
    name: 'onBoardingView',
    component: () => import('../views/onBoardingView.vue')
  },
  {
    path: '/nowmovies',
    name: 'NowMoviesView',
    component: () => import('../views/movies/NowMoviesView.vue')
  },
  {
    path: '/actionmovies',
    name: 'ActionsMovieView',
    component: () => import('../views/movies/ActionsMovieView.vue')
  },
  {
    path: '/animationmovies',
    name: 'AnimationMoviesView',
    component: () => import('../views/movies/AnimationMoviesView.vue')
  },
  {
    path: '/romancemovies',
    name: 'RomanceMoviesView',
    component: () => import('../views/movies/RomanceMoviesView.vue')
  },
  {
    path: '/crimemovies',
    name: 'CrimeMoviesView',
    component: () => import('../views/movies/CrimeMoviesView.vue')
  },
  {
    path: '/comedymovies',
    name: 'ComedyMoviesView',
    component: () => import('../views/movies/ComedyMoviesView.vue')
  },
  {
    path: '/search',
    name: 'SearchListView',
    component: () => import('../views/movies/SearchListView.vue')
  },
  {
    path: '/werecommendmovies',
    name: 'WeRecommendMoviesView',
    component: () => import('../views/movies/WeRecommendMoviesView.vue')
  },
  {
    path: '/allmovies',
    name: 'AllMoviesView',
    component: () => import('../views/movies/AllMoviesView.vue')
  },
  {
    path: '/addwishlist',
    name: 'AddWishListView',
    component: () => import('../views/accounts/AddWishListView.vue')
  },
  {
    path: '*',
    name: 'NotPound404View',
    component: () => import('../views/NotPound404View.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


export default router
