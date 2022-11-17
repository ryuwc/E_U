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
  },
  mutations: {
    SET_TOKEN: (state, token) => ( state.token = token ),
    SET_USER: (state, user) => (state.user = user),
  },
  actions: {
    getUserInfo({ commit, getters }) {
      axios({
        method: "get",
        url: `${API_URL}/accounts/user/`,
        headers: getters.authHead,
      })
        .then((res) => {
          // console.log(res);
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
          console.log(res);
          commit('SET_TOKEN', res.data.key);
          dispatch('getUserInfo');
        })
        .catch((err) => {
          console.log(err);
        });
      },

  }
}

export default accountsStore