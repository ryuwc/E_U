import Vue from 'vue'
import Vuex from 'vuex'
import accountsStore from './modules/accountsStore'
import moviesStore from './modules/moviesStore';
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],

  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    accountsStore: accountsStore,
    moviesStore: moviesStore,
  }
})
