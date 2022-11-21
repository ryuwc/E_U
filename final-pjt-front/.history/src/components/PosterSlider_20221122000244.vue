<template>
  <div class="container relative w-auto mx-auto">
      <div class="relative inset-0 flex justify-between top-80">
          <button @click="showPrev" role="button" aria-label="slide forward" class="z-30 ml-10 hover:scale-125" id="next">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAAEz0lEQVRoge2ZW2wUVRjHf2dmWxIBG4RGS0sUwXZtYgm0aPTJkvBASOWirhcaMUJtYmsMRfQBSJbE+Gq0aYFwSYgYdcM1td5IaInEB9IthBfYRRFLdxuN5aFUdMvufD5QIuzM7O6Z2fBC/4/fOef7fv89Z2fOnANTmtL9LVWMJBEi5vVg4GkwGsWSegwVRKgAZkx2GUdIgsQwjAFRqi9xYfBMmLDlt7YvA/sXHJtnBWgTaFZQqTl8WCkOWulMV8svLw57ZfBkYP/CSLkY0z4SJW8CpV6LT2oC1L4Sldm+/uLaUd3B2gb2Bo+9jtAJPKQ7No9GRWhria/+WmdQwQZ21+8uMccf7gY2aqNpSGBXoqLs3XB/Y7qQ/gUZ2F3f84A5bh0CWeEPr0ApejPTzVBrtOlGvq5Gvg63fvl7CA8grDT/zkTCz/cF8nXNa+DWsrmH8LclrKwaGfssX7ecS2hfzfF1ghwsHpW+FPLKhtiaiHu7iw4Ej8y+KcZFYI5OwUeXVzBr4UzO7YzrDMul0YyYwdZ4019Oja5rLG2ZH6NEC/6x5RU0ftKAETBQSnG2O6YL66TZASMTBtqdGh1nYM/Cw1XKNH9F4yV1J/xtRT+9UKyZSJWIuWB9vCmR3eD4J1am2Y7mG3b+isq74AHq33uSRW8/oZPGTdNukm5zarAZCBM2gHW6Ffq3RLnca/uBaOioZVFrtW46m0SpNyJEzOy4zcC8YN0zQJV2gYzQ/4GLiU3+Z0JB5Vh1SX123GEJGY1ei+Q00VFLXYs/E4Jalh2zGbCgwVeRHCaWbq6lbqN3E4Yi/wwoC98LNp+J2ubHPeW1oCY7Zl9CigpP2bMkGeHUh4P8fmIkOz/Pbn2K2nXztXMq7GxOj9EZDjFPstIWJzcNOJvYVufFxMzsQN7NnF9ZaYtrl8bsDQpmVT/oO7+TgXHfWe/QkvYgi9+xLV3ih4f4ecd53XTXswN2A8KILeZRS9qDLG53gD8yxOnt5xBLtPIJdjaHGZCi7MDc4C8du8rpbfrwAAouZsfsj1FDRbUzZ8kN/vK3CX7aetYT/KRsbPYXmTJOes0O7vC/fZfg1JYokvEMjyV2NpuBxIXBM8BVLwVc4b9P0v9+FMsHPDCUjA/mn4EwYUspvtDN7gr/Q5L+zQN+4RHhoNNRpON7wEpnuoAJnQLpVMYWu/Jjkv4O//BAqhSz26nBtr8G6LkWGXthzmtzgaWFVvhj8BqZlEXlc+UAXDkxQl+H72UDgAg734qvcvywdz93CaS2kZ72Ekh5oYXO77kEQHndLPo2DWClfR8+A4yWGtYOt8acxyp7q4+/ipIvdSsqQ/l5VN4lgZdbYqsPubXn3AttjK/6SmCXdtFiwQudueChgM1cWWyiXRRHi0KkISXqm8Tcso58/fIaCBHKWNPNZhS9xUErSD0zb6RChZxQF7Sdbo023Rh+pGw1qJ3+2XJLhM7hirK1oeHQP4X0177g2FdzNCSoLjSPHAsA+dOCtnxrPlvaHzQbYmsiBCZqlKILSOmOd9C/InSmSgNBXXjwecl3oLqn8ibpNpRqBuZpDh8CPleo7g2xVUmvDEW5Zg0TNqqqFzUIapmhqLegZvLW8v9rVhhWEBcYsMQ4mYwPRotxzTqlKd3v+g8ynsUJO26gFAAAAABJRU5ErkJggg==">
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
