<template>
  <section class="banner">
    <!-- <h1>intro page</h1>
    <router-link to="/home">지금 바로 시작하기</router-link> -->
    
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
  background: url('https://images.unsplash.com/photo-1517436073-3b7b1b1d1e1c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80') no-repeat center center;
} 


</style>