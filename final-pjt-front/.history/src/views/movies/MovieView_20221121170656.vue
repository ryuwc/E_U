<template>
  <div>
    <h4>Movie View</h4>
    <div>
      <!-- <NowMovie 
      v-for="(nowmovie, index) in nowmovies" 
      :key="index"
      :nowmovie='nowmovie'/> -->

      <div>
        <h1>video</h1>
        <div id='area'>
        <iframe id='video' :src=videoURL
         frameborder="0" allow="autoplay">
         </iframe>
        </div>
      </div>

      <div class="border border-primary d-flex row col-12 justify-content-evenly">

      <MovieCard
        v-for="(movie, index) in movies" 
        :key="index"
        :movie="movie"
      />
      </div>
    </div>
    <hr>
    

  </div>
</template>

<script>
import MovieCard from '@/components/MoviveCard.vue'
import _ from 'lodash'
// import NowMovie from '@/components/NowMovie.vue'
import { mapGetters, mapActions } from 'vuex';


const moviesStore = 'moviesStore'

export default {
  name: 'MovieView',
  components: {
    MovieCard,
    // NowMovie,
  },
  data() {
    return {
      playMovieUrl: '',
      // selectedMovie: []

    }
  },
  computed: {
    ...mapGetters(moviesStore, ['movies', 'nowmovies', 'loading',]),
    // ...mapGetters(moviesStore, ['genre12', 'genre14', 'genre16', 'genre18', 'genre27', 'genre28', 'genre35', 'genre36', 'genre37', 'genre53', 'genre80']),
      videoURL() {
      return `https://www.youtube.com/embed/${this.playMovie}?autoplay=1&mute=1`
    },
  },
  

  methods: {
    // ...mapActions(moviesStore, ['getMovies']),
    ...mapActions(moviesStore, ['playMovie']),
    
    // ...mapActions(moviesStore, ['getNowMovies']),
    // test() {
    //   console.log(this.loading)
    // }

    // getSelectMovie() {
    //   const rm12 = _.sampleSize(this.genre12 , 10)
    //   this.selectedMovie.push(...rm12)
    //   const rm14 = _.sampleSize(this.genre14 , 10)
    //   this.selectedMovie.push(...rm14)
    //   const rm16 = _.sampleSize(this.genre16 , 10)
    //   this.selectedMovie.push(...rm16)
    //   const rm18 = _.sampleSize(this.genre18 , 10)
    //   this.selectedMovie.push(...rm18)
    //   const rm27 = _.sampleSize(this.genre27 , 10)
    //   this.selectedMovie.push(...rm27)
    //   const rm28 = _.sampleSize(this.genre28 , 10)
    //   this.selectedMovie.push(...rm28)
    //   const rm35 = _.sampleSize(this.genre35 , 10)
    //   this.selectedMovie.push(...rm35)
    //   const rm36 = _.sampleSize(this.genre36 , 10)
    //   this.selectedMovie.push(...rm36)
    //   const rm37 = _.sampleSize(this.genre37 , 10)
    //   this.selectedMovie.push(...rm37)
    //   const rm53 = _.sampleSize(this.genre53 , 10)
    //   this.selectedMovie.push(...rm53)
    //   const rm80 = _.sampleSize(this.genre80 , 10)
    //   this.selectedMovie.push(...rm80)
    //   console.log(this.selectedMovie)
      // const rm99 = _.sampleSize(genre99 , 10)
      // const rm878 = _.sampleSize(genre878 , 10)
      // const rm9648 = _.sampleSize(genre9648 , 10)
      // const rm10402 = _.sampleSize(genre10402 , 10)
    // },


    pickPlayMovie() {
      const play = _.sample(this.nowmovies)
      console.log('@@@@@@@@@@@@@', play)
      this.playMovie = play.youtube_key
    },


  },

  created() {
    // this.getMovies(),
    // this.getNowMovies()
    this.pickPlayMovie()
    // this.getSelectMovie()
    
  },
};
</script>

<style scoped>

#area {
  position: relative; /* absolute는 부모가 relative일 때 부모를 따라간다. */
  width: 100%;
  padding-bottom: 56.25%;
  padding-left: 10%; /* 16:9 비율 */
  justify-content: center;
}

#video {
  position: absolute;
  width: 80%; /* 부모에 맞게 꽉 채운다. */
  height: 80%;
  margin: auto;
}
</style>