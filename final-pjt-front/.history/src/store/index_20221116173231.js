import Vue from 'vue'
import Vuex from 'vuex'
import accountsStore from './modules/accountsStore'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: '',
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    accountsStore: accountsStore,
  }
})
