<template>
  <div>
    <div 
    style="width: 492px; height: 151px; border: 1px solid gray;"
    class="rounded-lg"
    >
      <a href="https://i.ytimg.com/vi/FZkIlAEbHi4/hqdefault.jpg"
      class="block w-full h-full"
      ></a>
    </div>
  </div>
  <!-- 유튜브 iframe사용 예시 -->
    <!-- <iframe
            id="ytplayer"
            type="text/html"
            width="720"
            height="405"
            src="https://www.youtube.com/embed/6JnN1DmbqoU"
            frameborder="0"
            allowfullscreen="allowfullscreen"></iframe> -->
</template>

<script>
import { mapGetters } from 'vuex';

const moviesStore = 'moviesStore';
export default {
    name: 'MovieClip',
    computed: {
        ...mapGetters(moviesStore, ['nowMovieVideo']),
        videos() {
          return JSON.parse(JSON.stringify(this.nowMovieVideo))
        },
    },
}
</script>

<style>

</style>