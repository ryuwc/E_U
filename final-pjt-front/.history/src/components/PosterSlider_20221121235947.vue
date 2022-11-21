<template>
  <div class="container relative w-auto mx-auto">
      <div class="relative inset-0 flex justify-between top-80">
          <button @click="showPrev" role="button" aria-label="slide forward" class="z-30 ml-10 hover:scale-125" id="next">
              <svg width='24px' height='24px' viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M7 1L1 7L7 13" stroke="white" stroke-width='2' stroke-linecap="round" stroke-linejoin="round" />
              </svg>
          </button>
          <button @click="showNext" role="button" aria-label="slide forward" class="z-30 mr-16 hover:scale-125" id="next">
              <svg width='24px' height='24px' viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M1 1L7 7L1 13" stroke="white" stroke-width='2' stroke-linecap="round" stroke-linejoin="round" />
              </svg>
          </button>
      </div>
      <div class="flex items-center justify-center py-24 mt-20 sm:py-8">
          <div class="slider">
              <div class="slide-ana">
                  <VueSlickCarousel v-bind="settings" ref="carousel">
                      <div class="px-1">
                          <div class="relative flex flex-shrink-0 w-full sm:w-auto">
                              <img :src="`https://image.tmdb.org/t/p/original${moviePosters[0].file_path}`" alt="black chair and white table" class="object-cover object-center w-full" />
                          </div>
                      </div>
                      <div class="px-1">
                          <div class="relative flex flex-shrink-0 w-full sm:w-auto">
                              <img :src="`https://image.tmdb.org/t/p/original${moviePosters[1].file_path}`" alt="black chair and white table" class="object-cover object-center w-full" />
                          </div>
                      </div>
                      <div class="px-1">
                          <div class="relative flex flex-shrink-0 w-full sm:w-auto">
                              <img :src="`https://image.tmdb.org/t/p/original${moviePosters[2].file_path}`" alt="black chair and white table" class="object-cover object-center w-full" />
                          </div>
                      </div>
                      <div class="px-1">
                          <div class="relative flex flex-shrink-0 w-full sm:w-auto">
                              <img :src="`https://image.tmdb.org/t/p/original${moviePosters[3].file_path}`" alt="black chair and white table" class="object-cover object-center w-full" />
                          </div>
                      </div>
                      <div class="px-1">
                          <div class="relative flex flex-shrink-0 w-full sm:w-auto">
                              <img :src="`https://image.tmdb.org/t/p/original${moviePosters[4].file_path}`" alt="black chair and white table" class="object-cover object-center w-full" />
                          </div>
                      </div>
                      <div class="px-1">
                          <div class="relative flex flex-shrink-0 w-full sm:w-auto">
                              <img :src="`https://image.tmdb.org/t/p/original${moviePosters[5].file_path}`" alt="black chair and white table" class="object-cover object-center w-full" />
                          </div>
                      </div>
                      <div class="px-1">
                          <div class="relative flex flex-shrink-0 w-full sm:w-auto">
                              <img :src="`https://image.tmdb.org/t/p/original${moviePosters[6].file_path}`" alt="black chair and white table" class="object-cover object-center w-full" />
                          </div>
                      </div>
                      <div class="px-1">
                          <div class="relative flex flex-shrink-0 w-full sm:w-auto">
                              <img :src="`https://image.tmdb.org/t/p/original${moviePosters[7].file_path}`" alt="black chair and white table" class="object-cover object-center w-full" />
                          </div>
                      </div>
                      <div class="px-1">
                          <div class="relative flex flex-shrink-0 w-full sm:w-auto">
                              <img :src="`https://image.tmdb.org/t/p/original${moviePosters[8].file_path}`" alt="black chair and white table" class="object-cover object-center w-full" />
                          </div>
                      </div>
                      <div class="px-1">
                          <div class="relative flex flex-shrink-0 w-full sm:w-auto">
                              <img :src="`https://image.tmdb.org/t/p/original${moviePosters[9].file_path}`" alt="black chair and white table" class="object-cover object-center w-full" />
                          </div>
                      </div>
                  </VueSlickCarousel>
  
              </div>
          </div>
         
      </div>
  </div>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
export default {
  name: "PosterSlider",
  components: { VueSlickCarousel },
  data() {
      return {
          settings: {
              dots: false,
              infinite: true,
              arrows: false,
              speed: 500,
              slidesToShow: 0,
              slidesToScroll: 1,
              touchThreshold: 5
          },
          windowWidth: window.innerWidth,
      }
  },
  props: {
    moviePosters: Array,
  },
  methods: {
      showNext() {
          this.$refs.carousel.next();
      },
      showPrev() {
          this.$refs.carousel.prev();
      },
  },
  mounted(){
      if(this.windowWidth>1339){
          this.settings.slidesToShow = 4.5
      }else if(this.windowWidth>1079){
          this.settings.slidesToShow = 3.1
      }else if(this.windowWidth>767){
          this.settings.slidesToShow = 2.2
      }else{
          this.settings.slidesToShow = 1
      }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;0,900;1,400&display=swap');
@import url('https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css');
.slider {
  width: 100%;
  height: 300px;
  position: relative;
  overflow: hidden;
}
.slide-ana {
  height: 300px;
}
.slide-ana>div {
  width: 50vw;
  height: 100%;
  position: absolute;
  transition: all 1s;
}
/* @media (min-width: 300px) and (max-width: 884px) {
  .slider {
      height: 550px;
  }
}
@media (min-width: 768px) and (max-width: 1023px) {
  .slider {
      height: 581px;
  }
}
@media (min-width: 1024px) and (max-width: 1280px) {
  .slider {
      height: 379px;
  }
} */
.slider2 {
  width: 100%;
  height: 395px;
  position: relative;
  overflow: hidden;
}
.slide-ana2 {
  height: 100%;
}
.slide-ana2>div {
  width: 100%;
  height: 100%;
  position: absolute;
  transition: all 1s;
}
@media (min-width: 300px) and (max-width: 1023px) {
  .slider2 {
      height: 378px;
  }
}
</style>
