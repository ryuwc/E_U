import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

const accountsStore = {
  namespaced: true,
  state: {
    token: "",
    user: {},
  },
  getters: {
    authHead: (state) => ({ Authorization: `Token ${state.token}` }),
    user: (state) => state.user,
    nickname: (state) => state.user.nickname || state.user.username,
    isLogin: (state) => state.token ? true : false,
  },
  mutations: {
    SET_TOKEN: (state, token) => ( state.token = token ),
    SET_USER: (state, user) => (state.user = user),
  },
  actions: {
    test() {
      console.log("test");
    },
    getUserInfo({ commit, getters }, username) {
      axios({
        method: "get",
        url: `${API_URL}/accounts/profile/${username}`,
        headers: getters.authHead,
      })
        .then((res) => {
          console.log(res.data);
          commit("SET_USER", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    login({ commit, dispatch }, user) {
        // console.log(user);
        axios({
          method: 'post',
          url: `${API_URL}/accounts/login/`,
          data: { ...user },
        })
        .then(res => {
          // console.log(res);
          commit('SET_TOKEN', res.data.key);
          dispatch('getUserInfo', user.username);
        })
        .catch((err) => {
          console.log(err);
        });
      },
      logOut( commit, getters ) {
        axios({
          method: 'post',
          url: `${API_URL}/accounts/logout/`,
          headers: getters.authHead,
        })
        .then(res => {
          console.log(res);
          getters.isLogin && commit('SET_TOKEN', '');
          getters.user && commit('SET_USER', {});
        })
      }

  }
}

export default accountsStore