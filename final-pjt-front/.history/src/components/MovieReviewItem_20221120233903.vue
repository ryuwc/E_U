<template>
  <div id='personal_review'>
      <div>평점: {{ review.rank }}</div>
      <div>작성시간 : {{ review.created_at }}</div>
      <div>사용자: {{ review.user }}</div>
      <div>{{ review.content }}</div>
      <div>좋아요한 사용자 수 : {{ review.good_user.length }} | 싫어요 한 사용자 수 : {{review.bad_user.length }}</div>
       <button type="button" class="btn btn-sm" @click="deleteReview({ reviewId : review.id, authHead : authHead, user:user.id, movieId: movieId })">x</button>
  </div>
</template>

<script>
import {  mapActions, mapGetters } from 'vuex';
const moviesStore = 'moviesStore'
const accountsStore = 'accountsStore'

export default {
    name: 'MovieReviewItem',
    props: {
        review: Object
    },
    computed: {
      ...mapGetters(moviesStore, ['movieId']),
      ...mapGetters(accountsStore, ['authHead', 'user'])
    },

    methods:{
      ...mapActions(moviesStore, ["deleteReview"]),
    }
}
</script>

<style>
#personal_review {
  border: black 1px solid;
  border-radius: 10%;
}
</style>