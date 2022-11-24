<template>
  <div class="container relative w-auto mx-auto">
      <div class="relative inset-0 flex justify-between top-80">
          <button @click="showPrev" role="button" aria-label="slide forward" class="z-30 ml-10 border-none hover:scale-125" id="next">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAAEgElEQVRoge2ZTUxcVRiGn3PvAIn9wYC1IrCiZSYuaipVNy6kO9MQaI1jYxtrQglGcGG7tMYxMY0bN6VgsaWxaRN1rC0NdmGIlESNWmHqT7XMtNWWDpCoxIQiOjBzPxeg4tx7Z+bcGdiUdzfnO+f7nnfOmXvO3AMrWtGdLVWIJGHC5u2A7xEw6sWSOgwVQKgAVi90mUYYB4liGEOi1IWxK5GLIUJWvrXzMnC8prfa8tEmsFtBpebwuFKcspKpzpZrT8a9MngycHxDeJ0YJa+LkueAYq/FFzQLqqdIpV7ZM7JjUnewtoFjgd5nEDqAMt2xWTQpQltLrOl9nUE5G+iu6y4yp9d3AXu10TQkcGSsovTF0GB9Mpf+ORnoruu7y5y2ToM8kR9ejlKcT60yg63DDTPZuhrZOsx/88sIDyBsM/9IhUOPX/Bl65rVwPyyWUb4fyRsq5qYOpStW8Yl1OM/t0uQU4Wj0pdCnm6Obg+7x110InCmfE6MEeCeQoA81B7ALDH4+s0fdYdOpsQMtMYafnMKuq6xpGUeREnB4De3+//9rGmi3GekQkC7U9BxBo5u+LBKmeZ18t+kbPAA3x29qmsiUSRmzZ5Yw1h6wPFHrEyznSWCB0jNaR+BSuZItjkFbAZChAxgl26FdLnBX37nOpFDI9r5RKlnw4TN9HabgerApkeBKu0Ki+QG/8PJn/jqjcueciqonKotqktvd1hCRr2nCgtyg49+cJMvD36fT2oEtTW9zWbAgi1eC7jBx86M8vmr34J4zTwvQ5F9BpRFrZfkbvDXem/x2YFvECtPesACWwH7ElJU6CZ2g//543E+fflSQeDn0exsTo/R1Q5trnKDv9E/weC+IaxUYeAXtCa9IethLpOUqSjzr3WM/X51qtDwjnIyMJ3rYEkJAy8NcbN/whbb/IKfh/c/kA+bk26nN9gNCHaaDLKSlquJTS0bC2pCsLM5zIBEdRMvlwkFti3c/hg11LCX5MtkwsZm38iUMeA1+1KbsMTOZjMwdiVyEbjlucjSmRgdj0VsM2A73Q0yKI3rdt4LPOa1kljCjf4Jyjau5e6a/z+619eV4ysxGf/iV72cQuf+yec/SW933AesZKoTmNWqYMvhPhPJREo3XaIYs8sp4Ghg/l2l6tGtki4nE5HDI1w6rPegE+Ftp39jkGkn9iUOgNKbZwctNuEFHpgsNqzX3IIZX6scqz23EyXv6lZ0LGQoT4c6gadaok2n3eIZz0J7Y43vCRzRruoE4gVe6MgEDzkc5kqjs+2iOKtdPU8pUR+N3V+6L1u/rAaCBFPWKnM3ivOFQctJfWtmEsFc3lDndJxuHW6Yid9X2gTqrfzZMkuEjnhF6Y5gPPhnLv21Lzh6/GeDguqkQK8cF4H8YkFbtjWfLu0/NM3R7WF8s36l6AQSuuMd9JcIHYliX0AXHvK85DtR21c5R7INpXYD1ZrDR4GTCtXVHG0c98pQkGvWECGjqvbBLYLaaijqLPAv3Fr+d80KcQUxgSFLjIHxWGS4ENesK1rRna6/AfBPxFyraaOYAAAAAElFTkSuQmCC">
          </button>
          <button @click="showNext" role="button" aria-label="slide forward" class="z-30 mr-16 border-none hover:scale-125" id="next">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAAEz0lEQVRoge2ZW2wUVRjHf2dmWxIBG4RGS0sUwXZtYgm0aPTJkvBASOWirhcaMUJtYmsMRfQBSJbE+Gq0aYFwSYgYdcM1td5IaInEB9IthBfYRRFLdxuN5aFUdMvufD5QIuzM7O6Z2fBC/4/fOef7fv89Z2fOnANTmtL9LVWMJBEi5vVg4GkwGsWSegwVRKgAZkx2GUdIgsQwjAFRqi9xYfBMmLDlt7YvA/sXHJtnBWgTaFZQqTl8WCkOWulMV8svLw57ZfBkYP/CSLkY0z4SJW8CpV6LT2oC1L4Sldm+/uLaUd3B2gb2Bo+9jtAJPKQ7No9GRWhria/+WmdQwQZ21+8uMccf7gY2aqNpSGBXoqLs3XB/Y7qQ/gUZ2F3f84A5bh0CWeEPr0ApejPTzVBrtOlGvq5Gvg63fvl7CA8grDT/zkTCz/cF8nXNa+DWsrmH8LclrKwaGfssX7ecS2hfzfF1ghwsHpW+FPLKhtiaiHu7iw4Ej8y+KcZFYI5OwUeXVzBr4UzO7YzrDMul0YyYwdZ4019Oja5rLG2ZH6NEC/6x5RU0ftKAETBQSnG2O6YL66TZASMTBtqdGh1nYM/Cw1XKNH9F4yV1J/xtRT+9UKyZSJWIuWB9vCmR3eD4J1am2Y7mG3b+isq74AHq33uSRW8/oZPGTdNukm5zarAZCBM2gHW6Ffq3RLnca/uBaOioZVFrtW46m0SpNyJEzOy4zcC8YN0zQJV2gYzQ/4GLiU3+Z0JB5Vh1SX123GEJGY1ei+Q00VFLXYs/E4Jalh2zGbCgwVeRHCaWbq6lbqN3E4Yi/wwoC98LNp+J2ubHPeW1oCY7Zl9CigpP2bMkGeHUh4P8fmIkOz/Pbn2K2nXztXMq7GxOj9EZDjFPstIWJzcNOJvYVufFxMzsQN7NnF9ZaYtrl8bsDQpmVT/oO7+TgXHfWe/QkvYgi9+xLV3ih4f4ecd53XTXswN2A8KILeZRS9qDLG53gD8yxOnt5xBLtPIJdjaHGZCi7MDc4C8du8rpbfrwAAouZsfsj1FDRbUzZ8kN/vK3CX7aetYT/KRsbPYXmTJOes0O7vC/fZfg1JYokvEMjyV2NpuBxIXBM8BVLwVc4b9P0v9+FMsHPDCUjA/mn4EwYUspvtDN7gr/Q5L+zQN+4RHhoNNRpON7wEpnuoAJnQLpVMYWu/Jjkv4O//BAqhSz26nBtr8G6LkWGXthzmtzgaWFVvhj8BqZlEXlc+UAXDkxQl+H72UDgAg734qvcvywdz93CaS2kZ72Ekh5oYXO77kEQHndLPo2DWClfR8+A4yWGtYOt8acxyp7q4+/ipIvdSsqQ/l5VN4lgZdbYqsPubXn3AttjK/6SmCXdtFiwQudueChgM1cWWyiXRRHi0KkISXqm8Tcso58/fIaCBHKWNPNZhS9xUErSD0zb6RChZxQF7Sdbo023Rh+pGw1qJ3+2XJLhM7hirK1oeHQP4X0177g2FdzNCSoLjSPHAsA+dOCtnxrPlvaHzQbYmsiBCZqlKILSOmOd9C/InSmSgNBXXjwecl3oLqn8ibpNpRqBuZpDh8CPleo7g2xVUmvDEW5Zg0TNqqqFzUIapmhqLegZvLW8v9rVhhWEBcYsMQ4mYwPRotxzTqlKd3v+g8ynsUJO26gFAAAAABJRU5ErkJggg==">
          </button>
      </div>
      <div class="flex items-center justify-center py-24 mt-20 sm:py-8">
          <div class="slider">
              <div class="slide-ana">
                  <VueSlickCarousel v-bind="settings" ref="carousel">
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
