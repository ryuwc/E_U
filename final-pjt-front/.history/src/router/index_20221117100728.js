import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/signup',
    name: 'signup',
    component: () => import('../views/accounts/SignUpView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/accounts/LoginView.vue')
  },
  {
    path: '/edit',
    name: 'edit',
    component: () => import('../views/accounts/EditUserView.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
