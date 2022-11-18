<template>
  <div>
    <h1>movie review</h1>
      
      <div>
      <p>user_id: {{ review.user }}</p>
      <p>평점:{{ review.rank }}</p>
      <p>내용: {{ review.content }}</p>
      <p>작성시간: {{ review.created_at }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieReviewView',
  props: {
    review: Object
  },
}
</script>

<style>

</style>