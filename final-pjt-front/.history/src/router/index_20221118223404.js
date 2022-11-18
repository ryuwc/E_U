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

  //   beforeEnter(to, from, next) {
  //     // 이미 로그인 되어있는 경우
  //     this.$store.getters[accountsStore + "/i"] ? next({ name: "home" }) : next();
  //     to, from, next;
  //     console.log();
  //     // if (localStorage.getItem('token')) {
  //     //   // 메인 페이지로 이동
  //     //   next({ name: 'main' });
  //     // } else {
  //     //   next();
  //     // }
  //   }
  },
  {
    path: '/edit',
    name: 'EditUserView',
    component: () => import('../views/accounts/EditUserView.vue')
  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: () => import('../views/accounts/ProfileView.vue')
  },
  {
    path: '/',
    name: 'IntroPage',
    component: () => import('../views/movies/IntroPage.vue')
  },
  {
    path: '/home',
    name: 'MovieView',
    component: () => import('../views/movies/MovieView.vue')
  },
  {
    path: '/practice',
    name: 'PracticeView',
    component: () => import('../views/accounts/PracticeView.vue')
  },
  {
    path: '/test',
    name: 'TestView',
    component: () => import('../views/accounts/TestView.vue')
  },
  {
    path: '/:id',
    name: 'MovieDetailInfoView',
    component: () => import('../views/movies/MovieDetailInfoView.vue')
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// 로컬스토리지에서 토큰 가져오기
// console.log(JSON.parse(localStorage.getItem("vuex")).accountsStore.token);


// 전역 가드
router.beforeEach((to, from, next) => {
  // 로그인 되어 있는지 확인 (위의 방법 확인)
  const isLogin = JSON.parse(localStorage.getItem("vuex")).accountsStore.token ? true : false;
  // 로그인이 필요한 페이지
  const authPages = ['EditUserView', 'profile'];
  // 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지에 속하는지 확인
  const authRequired = authPages.includes(to.name);
  // 로그인이 필요한 페이지에 로그인이 되어 있지 않으면 로그인 페이지로 이동
  if (authRequired && !isLogin) {
    next('/login');
    // 로그인이 필요 없는 페이지에 로그인이 되어 있으면 메인 페이지로 이동
  } else{
    next();
  }
})

export default router
