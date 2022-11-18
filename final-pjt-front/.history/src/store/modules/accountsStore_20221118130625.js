import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

const accountsStore = {
  namespaced: true,
  state: {
    token: "",
    user: {},
    usernames: [],
  },
  getters: {
    authHead: (state) => ({ Authorization: `Token ${state.token}` }),
    user: (state) => state.user,
    username: (state) => state.user.username,
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
    signUp(user) {
      // console.log("sign up");
      console.log(user);
      let signUpuser = {
        username: user.username,
        nickname: user.nickname,
        password1: user.password1,
        password2: user.password2,
      };
      if (!user.nickname) {
        user = {
          username: user.username,
          password1: user.password1,
          password2: user.password2,
        };
      }
      console.log(signUpuser);
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/signup/",
        data: { ...signUpuser },
      })
        .then((res) => {
          // console.log(res.data);
          
          this.$store.state.token = res.data.key;
          this.$router.push({ name: "login" });
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
      logOut({ commit, getters }) {
        axios({
          method: 'post',
          url: `${API_URL}/accounts/logout/`,
          headers: getters.authHead,
        })
        .then(res => {
          console.log(res);
          commit('SET_TOKEN', '');
          commit('SET_USER', {});
        })
      },
      editUserInfo({ dispatch, commit, getters }, user) {
        // console.log(user);
        commit
        user
        const userOrigin = getters.user;
        // console.log(userOrigin);
        const userNew = { ...userOrigin, ...user };
        // console.log(userNew);
        // console.log(getters.authHead);
        axios({
          method: 'put',
          url: `${API_URL}/accounts/profile/${getters.username}/`,
          data: { ...userNew },
          headers: getters.authHead,
        })
        .then(res => {
          console.log(res);
          // commit('SET_USER', res.data);
          dispatch('getUserInfo', res.data.username);
        })
      },
      editPassword({ getters }, password) {
        // console.log(password);
        axios({
          method: 'post',
          url: `${API_URL}/accounts/password/change/`,
          headers: getters.authHead,
          data: { ...password }, 
        })
        .then(() => {
          alert('비밀번호 변경에 성공했습니다.');
        })
        .catch(err => {
          console.log(err);
        })
      },
  }
}

export default accountsStore