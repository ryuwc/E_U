<template>
  <div>
     <div>
      <input type="text" v-model.trim="content" placeholder="리뷰를 작성하세요">
    </div>
    <div>
      <input type="text" v-model.trim="rank" @keyup.enter="createReview" placeholder="1부터 5까지 평점을 입력하세요">
    </div>
    <button type="button" class="btn" @click="createReview">등록하기</button>
  </div>
</template>

<script>
export default {
    name: 'CreateReview',
    methods: {
      createReview() {

      },
    }
}
</script>

<style>

</style>