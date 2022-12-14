<template>
  <div>
    <div class="d-flex">
      <div>
        <img :src="commentuser.profile_path" alt="Avatar Photo" >
        <div class="m-4">
          {{ commentuser.username }}
        </div>
      </div>
      <div class="balloon_03">
        <p class="mt-2 ml-5">{{this.comment.content}}</p>
      </div>
      <div
      v-if="commentuser.id === user.id">
        <button class="delete-btn"
          type="button"
          @click="deleteComment({ commentId: comment.id, authHead: authHead, userId: user.id, profileId: profileuser.id })"
        >
          X
        </button>
      </div>
    </div>
  </div>
</template>

<script>

import { mapActions, mapGetters } from 'vuex'
import axios from "axios";


const API_URL = "http://127.0.0.1:8000";
const accountsStore = 'accountsStore'
const commentsStore = 'commentsStore'

export default {
  name: 'CommentList',
  props: {
    comment: Object,
  },
  data() {
    return {
      commentuser: null
    }
  },
  computed: {
    ...mapGetters(accountsStore, ['authHead', 'user','profileuser']),
    ...mapGetters(commentsStore, ['profile']),
    
  },
  methods: {
    ...mapActions(commentsStore, ['deleteComment']),
    commentCreateUser() {
      axios({
        method: "get",
        url: `${API_URL}/accounts/profile/${this.comment.user}`,
        headers: this.authHead,
      })
        .then((res) => {
          console.log(res.data, '@@@');
          this.commentuser = res.data
        })
        .catch((err) => {
          console.log(err);
        });
    }
  },
  created() {
    console.log(this.comment)
    console.log(this.profileuser)
    this.commentCreateUser()

  },
  mounted() {

  },

}

</script>

<style>
*{
  color: black
}
.delete-btn{
  margin-top: 80%;
  margin-left: 20%;
  
}
.balloon_03 {
 position:relative;
 margin-left: 50px;
 margin-top: 6%;
 width:40%;
 height:80px;
  background:#ffadb6;
  border-radius: 10px;
}
.balloon_03:after {
 border-top:10px solid #ffadb6;
 border-left: 15px solid transparent;
 border-right: 0px solid transparent;
 border-bottom: 0px solid transparent;
 content:"";
 position:absolute;
 top:10px;
 left:-15px;
}
 

body{
    background-color: #fff;
}
.container{
    background-color: #eef2f5;
    width: 400px;
}
.addtxt{
    padding-top: 10px;
    padding-bottom: 10px;
    text-align: center;
    font-size: 13px;
    width: 350px;
    background-color: #e5e8ed;
    font-weight: 500;
}
.form-control: focus{
    color: #000;
}
.second{
    width: 350px;
    background-color: white;
    border-radius: 4px;
    box-shadow: 10px 10px 5px #aaaaaa;
}
.text1{
    font-size: 13px;
    font-weight: 500;
    color: #56575b;
}
.text2{
    font-size: 13px;
    font-weight: 500;
    margin-left: 6px;
    color: #56575b;
}
.text3{
    font-size: 13px;
    font-weight: 500;
    margin-right: 4px;
    color: #828386;
}
.text3o{
    color: #00a5f4;

}
.text4{
    font-size: 13px;
    font-weight: 500;
    color: #828386;
}
.text4i{
    color: #00a5f4;
}
.text4o{
    color: white;
}
.thumbup{
    font-size: 13px;
    font-weight: 500;
    margin-right: 5px;
}
.thumbupo{
    color: #17a2b8;
}

</style>