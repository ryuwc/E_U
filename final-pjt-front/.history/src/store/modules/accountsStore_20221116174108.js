import axios from "axios";

const accountsStore = {
  namespaced: true,
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    login(user) {
        axios({
          method: 'post',
          url: "http://127.0.0.1:8000/accounts/login/",
          data: { ...user },
        })
        .then(res => {
          console.log(res);
        })
      }
  }
}

export default accountsStore