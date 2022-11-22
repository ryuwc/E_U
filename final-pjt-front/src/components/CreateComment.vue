<template>
  <div>
    <div>
      <input 
      type="text" 
      v-model.trim="content" 
      placeholder="방명록을 작성하세요">
    </div>
    <button type="button" class="btn" @click="createComment({ content: content, profileUserId: profileUserId, rank: rank, user: user.id, authHead: authHead  })">등록하기</button>
  </div>
</template>

<script>


export default {
  name: 'CreateComment',

}
</script>

<style>

</style>