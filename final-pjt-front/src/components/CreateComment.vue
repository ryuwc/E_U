<template>
  <div class="ml-5">
    <div class="flex">
      <input 
      style="margin-top:5%; margin-left:5%;"
      type="text" 
      v-model.trim="content" 
      placeholder="방명록을 작성하세요">
      <button style="margin-top:5.5%" type="button" class="btn-hover color-11" @click="[createComment({ content: content, profile: profileuser , user: user.id, authHead: authHead  }), cleanData()]">등록하기</button>
    </div>
  </div>
</template>

<script>
import {  mapActions, mapGetters } from 'vuex';
// const moviesStore = 'moviesStore';
const accountsStore = 'accountsStore'
const commentsStore = 'commentsStore'

export default {
  name: 'CreateComment',
  data() {
    return { 
      content: null,
    };
  },
  computed: {
    ...mapGetters(accountsStore, ['authHead', 'user']),
    ...mapGetters(accountsStore, ['profileuser']),

  },
  methods: {
    cleanData() {
      this.content = null;
    },
    ...mapActions(commentsStore, ['createComment'])
  },

  created() {
    // console.log(this.profileuser)
  },
}
</script>

<style>
input {
  width:80%;
  height: 180px;
  border-radius: 20px;
  font-size: 20px;
}
* {
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
}

.buttons {
    margin: 10%;
    text-align: center;
}

.btn-hover {
    width: 200px;
    font-size: 16px;
    font-weight: 600;
    color: #fff;
    cursor: pointer;
    margin: 20px;
    height: 55px;
    text-align:center;
    border: none;
    background-size: 300% 100%;

    border-radius: 50px;
    moz-transition: all .4s ease-in-out;
    -o-transition: all .4s ease-in-out;
    -webkit-transition: all .4s ease-in-out;
    transition: all .4s ease-in-out;
}

.btn-hover:hover {
    background-position: 100% 0;
    moz-transition: all .4s ease-in-out;
    -o-transition: all .4s ease-in-out;
    -webkit-transition: all .4s ease-in-out;
    transition: all .4s ease-in-out;
}

.btn-hover:focus {
    outline: none;
}

.btn-hover.color-11 {
       background-image: linear-gradient(to right, #eb3941, #f15e64, #e14e53, #e2373f);  box-shadow: 0 5px 15px rgba(242, 97, 103, .4);
}
</style>