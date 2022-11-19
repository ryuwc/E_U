<template>
  <section class="banner">
    <!-- <h1>intro page</h1>
    <router-link to="/home">지금 바로 시작하기</router-link> -->
    <img src="https://images.unsplash.com/photo-1595769816263-9b910be24d5f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1179&q=80" alt="">
  </section>
</template>

<script>
export default {
  name: 'IntroPage'
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.banner {
  position: absolute;
  width: 100%;
  height: 1024px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #0b061f;
} 


</style>