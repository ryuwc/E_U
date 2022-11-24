import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

const commentssStore = {
  namespaced: true,
  state: {
    comments: null,
  },

  getters: {
    comments: (state) => state.comments,
  },

  mutations: {
    CREATE_COMMENT: (state, comment) => (state.comments.unshift(comment)),
    GET_COMMENTS: (state, comments) => (state.comments = comments),
    DELETE_COMMENT: (state, commentId) => (state.comments = state.comments.filter((comment) => comment.id !== commentId)),
  },

  actions:{
  createProfileUser( { commit }, profileUser ) {
    axios({  
      method: "post",
      url: `${API_URL}/comments/profileuser/`,
      data: {...profileUser},
      headers: profileUser.authHead
    })
    .then((res) => {
      commit
      console.log( '프로필 유저 생성 완료', res.data)
    })
    .catch((err) => {
      console.log(err)
    })
  },


  // 댓글 생성 
  createComment( { commit }, commentItem) {

    axios({
      method: "post",
      url: `${API_URL}/comments/profileuser/${commentItem.profile.id}/comment/`,
      data: {content: commentItem.content},
      headers: commentItem.authHead,
    })
    .then((res) => {
      alert('댓글 작성 완료!.')
      commit('CREATE_COMMENT', res.data)
      commit
    })
    .catch((err) => {
      console.log(err)
    })
  },

  // 댓글 조회(GET)
  getComments( { commit }, profileItem) {
    // console.log(profileItem.id)
    axios({
      method: "get",
      url: `${API_URL}/comments/profileuser/${profileItem.id.id}/comments/`,
      headers: profileItem.token,
    })
    .then((res) => {
      commit("GET_COMMENTS", res.data);
    })
    .catch((err) => {
      console.log(err)
    })
  },

  // 댓글 삭제(DELETE)
  deleteComment( { commit }, commentItem) {
    axios({
      method: "delete",
      url: `${API_URL}/comments/profileuser/${commentItem.profileId}/comment/${commentItem.commentId}/`,
      headers: commentItem.authHead,
    })
    .then((res) => {
      console.log( '삭제 완료', res)
      commit('DELETE_COMMENT', commentItem.commentId)
      this.$router.push({ name: "ProfileView", params: { id: commentItem.profileId } })
    })
    .catch((err) => {
      console.log(err)
    })
  },


  }
}

export default commentssStore