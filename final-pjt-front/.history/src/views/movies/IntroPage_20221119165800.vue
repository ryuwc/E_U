<template>
  <section class="banner">
    <!-- <h1>intro page</h1>
    <router-link to="/home">지금 바로 시작하기</router-link> -->
    <h2 class="text">Welcome</h2>
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
  /* background: url('https://images.unsplash.com/photo-1595769816263-9b910be24d5f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1179&q=80') */
  background: url('photo-1620055155785-2fc4acd747cb.avif')
    no-repeat center center;
  background-size: cover;
} 

.text{
  position: absolute;
  top: 165px;
  right: 545px;
  color: rgba(255, 255, 255, 0.1);
  font-size: 12vw;
  font-family: 'Pacifico', cursive;
  font-weight: 100;
  animation: animateText 5s linear infinite;
}
@keyframes animateText
{
  0%{
    color: rgba(255, 255, 255, 0.1);
    text-shadow: none;
  }
  100%{
    color: rgba(255, 255, 255, 1);
    text-shadow: 0 0 10px #b01558, 0 0 20px #fff, 0 0 40px #b01558, 0 0 80px #b01558, 0 0 90px #b01558, 0 0 100px #b01558, 0 0 150px #b01558;
  }
  
}

</style>