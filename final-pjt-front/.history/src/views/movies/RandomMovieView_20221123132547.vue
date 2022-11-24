<template>
  <div class="random" style="margin-top: 7rem; top: 0;">
    <div id="for_nav"></div>
    <br>
      <div class="text-box"
      style="margin-left: 45vw;"
      >
      <a href="#" 
      class="btn btn-white btn-animate"
       style="font-size: x-large;"
       @click.prevent="goToRandomMovie"
       >랜덤 영화로 이동!</a>
    </div>

    <div class="font-bold text-white balls"
    style="margin-left: 47.5vw; margin-top: 110px;"
    >
      <div class="text-center fw-bold"><span style="font-size:x-large">P</span></div>
      <div class="text-center fw-bold"><span style="font-size:x-large">I</span></div>
      <div class="text-center fw-bold"><span style="font-size:x-large">C</span></div>
      <div class="text-center fw-bold"><span style="font-size:x-large">K</span></div>
    </div>
    <br>
    <br>
    <br>
    <MoviveCard
    v-if="movie"
    :movie="movie"
    style="margin-left: auto; margin-right: auto;"
   
    />
    
  </div>
</template>

<script>
import _ from 'lodash'
import { mapGetters } from 'vuex';
import MoviveCard from '@/components/MoviveCard.vue';


export default {
  name: "RandomMovieView",
  data() {
    return {
      movie: null,
    }
  },
  components:{
    MoviveCard
  },
  computed: {
    ...mapGetters('moviesStore', ['movies']),
    randomMovie() {
      return _.sample(this.movies);
    },
  },
  methods: {
    pickMovie() {
      
      // console.log(randomMovie.title)
    },
    goToRandomMovie() {
      this.$router.push({ name: "MovieDetailInfoView", params: { id: this.randomMovie.id } });
    },
  },
  mounted() {
    console.log(this.randomMovie)
  },
}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Dongle:wght@300;400&family=Jua&display=swap');

* {
  font-family: 'Jua', sans-serif;
}


#for_nav{
  position: absolute;
    top: 0;
    height: 100px;
    width: 100%;
    /* background-color: rgba(0, 0, 0, 0.2); */
    background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0));
}

.balls {
  width: 10em;
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
  justify-content: space-between;
}

.balls div {
  width: 3em;
  height: 3em;
  border-radius: 50%;
  background-color: #fc2f70;
  transform: translateY(-100%);
  animation: wave 0.8s ease-in-out alternate infinite;
}

.balls div:nth-of-type(1) {
  animation-delay: -0.4s;
}

.balls div:nth-of-type(2) {
  animation-delay: -0.2s;
}
.balls div:nth-of-type(3) {
  animation-delay: -0.1s;
}

@keyframes wave {
  from {
    transform: translateY(-50%);
  }
  to {
    transform: translateY(50%);
  }
}
.text-box{
  margin-left: 0vw;
}


.btn:link,
.btn:visited {
    text-transform: uppercase;
    text-decoration: none;
    padding: 15px 40px;
    display: inline-block;
    border-radius: 100px;
    transition: all .2s;
    position: absolute;
}

.btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.btn:active {
    transform: translateY(-1px);
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}

.btn-white {
    background-color: #fff;
    color: #777;
}

.btn::after {
    content: "";
    display: inline-block;
    height: 100%;
    width: 100%;
    border-radius: 100px;
    position: absolute;
    top: 0;
    left: 0;
    z-index: -1;
    transition: all .4s;
}

.btn-white::after {
    background-color: #fff;
}

.btn:hover::after {
    transform: scaleX(1.4) scaleY(1.6);
    opacity: 0;
}

.btn-animated {
    animation: moveInBottom 5s ease-out;
    animation-fill-mode: backwards;
}

@keyframes moveInBottom {
    0% {
        opacity: 0;
        transform: translateY(30px);
    }

    100% {
        opacity: 1;
        transform: translateY(0px);
    }
}
</style>
