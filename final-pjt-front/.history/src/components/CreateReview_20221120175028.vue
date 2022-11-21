<template>
  <div>
     <div>
      <input type="text" v-model.trim="content" placeholder="리뷰를 작성하세요">
    </div>
    <div>
      <input type="text" v-model.trim="rank" @keyup.enter="createReview" placeholder="1부터 5까지 평점을 입력하세요">
    </div>
    <button type="button" class="btn" @click="createReview({ content: content, movieId: movieId, rank: rank, user: user.id, authHead: authHead  })">등록하기</button>
  </div>
</template>

<script>
import {  mapActions, mapGetters } from 'vuex';
const moviesStore = 'moviesStore'
const accountsStore = 'accountsStore'

export default {
    name: 'CreateReview',
    computed: {
      ...mapGetters(moviesStore, ['movieId']),
      ...mapGetters(accountsStore, ['authHead', 'user'])
    },
    data() {
      return {
        content: null,
        rank: null,
      }
    },
    methods: {
      ...mapActions(moviesStore, ["createReview"]),
    },
    created() {
      this.movieID = this.movieId
    }
}
</script>

<style>

</style>