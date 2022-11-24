<template>
  <div id="card">
    <div id="imgBx">
      <img id="img" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" alt="">
    </div>
    <div id="details">
      <h3>Nike Air Max<br><span>Men's Shoe</span></h3>
      <h4>Product Details</h4>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse, voluptatem!</p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'MovieCard2',
  components: {
  },
  props:{
    movie: Object
  },

  data() {
    return {};
  },

  mounted() {},

  methods: {},
};
</script>

<style scoped>

#card {
  position: relative;
  width: 300px; 
  height: 380px;
  background: #000;
  box-shadow: 0 15px 45px rgba(0, 0, 0, 0.1);
  display: flex;
  overflow: hidden;
  transition: 0.5s ease-in-out;
}

#card:hover {
  width: 600px; 
}

#imgBx {
  position: relative; 
  min-width: 300px; height: 
  100%; background: #fff; 
  display: flex; 
  justify-content: center; 
  align-items: center;
  overflow: hidden;
  z-index: 0;
}

#img {
  max-width: 300px;
}

#details {
  position: relative;
  width: 300px;
  height: 100%;
  background: #4ba9e9;
  display: flex;
  justify-content: center;
  /* align-items: center; */
  padding: 20px;
  flex-direction: column;
  z-index: 1;
}

#details::before {
  content: '';
  position: absolute;
  left: 0;
  width: 0;
  height: 0;
  border-top: 10px solid transparent;
  border-bottom: 10px solid transparent;
  border-left: 10px solid #fff;
}

#details h3 {
  text-transform: uppercase;
  font-weight: 600;
  font-size: 1.5em;
  line-height: 1em;
}
</style>
