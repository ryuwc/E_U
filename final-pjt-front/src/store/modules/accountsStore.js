import axios from "axios";
import router from "@/router";

const API_URL = "http://127.0.0.1:8000";

const accountsStore = {
  namespaced: true,
  state: {
    token: "",
    user: {},
    usernames: [],
    profileuser: null,
  },
  getters: {
    authHead: (state) => ({ Authorization: `Token ${state.token}` }),
    user: (state) => state.user,
    username: (state) => state.user.username,
    nickname: (state) => state.user.nickname || state.user.username,
    isLogin: (state) => state.token ? true : false,
    usernames: (state) => state.usernames,
    profileuser: (state) => state.profileuser,

  },
  mutations: {
    SET_TOKEN: (state, token) => ( state.token = token ),
    SET_USER: (state, user) => (state.user = user),
    GET_PROFILE_USER: (state, profileuser) => (state.profileuser = profileuser)
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
          // console.log(res.data);
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
        if (user.uporin === true) {
          router.push('/addwishlist')
        } else {
          router.push('/home');
        }
      })
      .catch((err) => {
        console.log(err);
      });
    },
    signUp({ dispatch, state }, user) {
      // console.log("sign up");
      // console.log(user);
      let signUpuser = {
        username: user.username,
        nickname: user.nickname,
        password1: user.password1,
        password2: user.password2,
      };
      if (!user.nickname) {
        signUpuser = {
          username: user.username,
          password1: user.password1,
          password2: user.password2,
        };
      }
      // console.log(signUpuser);
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/signup/",
        data: { ...signUpuser },
      })
        .then((res) => {
          res
          state.usernames.push(user.username);
          dispatch("login", { username: user.username, password: user.password1, uporin: true });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    
    
      logOut({ commit, getters }) {
        // console.log("logout", getters.authHead);
        axios({
          method: 'post',
          url: `${API_URL}/accounts/logout/`,
          headers: getters.authHead,
        })
        .then(res => {
          res
          // console.log(res);
          commit('SET_TOKEN', '');
          commit('SET_USER', {});
        })
        .catch(err => {
          console.log(err);
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

      // 11.22 수정 //////////////////////////////////////////////////

      // 프로필 페이지 유저 정보 갖고오기
      getProfileUser( {commit, getters }, profileUserId ) {
        // console.log(profileUserId)
        axios({
          method: "get",
          url: `${API_URL}/accounts/profile/${profileUserId.user}`,
          headers: getters.authHead,
        })
        .then((res) => {
          // console.log(res.data);
          commit('GET_PROFILE_USER', res.data)
        })
        .catch((err) => {
          console.log(err);
        });
      },
  }
}

export default accountsStore