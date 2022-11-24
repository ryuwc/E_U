<script setup></script>

<template>
  <!-- Team Section: Vertical Photos with Asymmetrical Alignment -->
  <div class="bg-white">
    <div class="container w-full px-4 py-16 mx-auto space-y-16 lg:px-8 lg:py-32">
      <!-- Heading -->
      <div class="text-center">
        <h2 class="mb-4 text-3xl font-extrabold md:text-4xl">
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-500 via-pink-500 to-rose-500">이:유에서 최신 영화를 살펴봐요!</span>
        </h2>
        <h3 class="mx-auto text-lg font-medium text-gray-600 md:text-xl md:leading-relaxed lg:w-2/3"></h3>
      </div>
      <!-- END Heading -->

      <VueSlickCarousel v-bind="settings" ref="carousel">
        <!-- 이거 하나씩 시작 -->
        <div style="width: 20vw; height: 20vw" class="relative overflow-hidden rounded-lg shadow-lg group rotate-1">
          <div class="absolute inset-0 flex items-end justify-center p-4 text-white bg-gradient-to-t from-black/90 via-transparent z-1">
            <div class="text-center">
              <h4 class="mb-1 text-xl font-semibold">Irma Norton</h4>
              <p class="mb-3 font-medium text-gray-300">Founder &amp; CEO</p>
            </div>
          </div>
          <div style="width: 20vw; height: 20vw" class="w-64 transition duration-150 ease-out bg-cover h-60 group-hover:scale-110">
            <img class="w-full h-auto" src="https://source.unsplash.com/nHoaFkrJEx4/600x800" alt="User Avatar" />
          </div>
        </div>
        <div style="width: 20vw; height: 20vw" class="relative overflow-hidden rounded-lg shadow-lg group rotate-1">
          <div class="absolute inset-0 flex items-end justify-center p-4 text-white bg-gradient-to-t from-black/90 via-transparent z-1">
            <div class="text-center">
              <h4 class="mb-1 text-xl font-semibold">Irma Norton</h4>
              <p class="mb-3 font-medium text-gray-300">Founder &amp; CEO</p>
            </div>
          </div>
          <div style="width: 20vw; height: 20vw" class="w-64 transition duration-150 ease-out bg-cover h-60 group-hover:scale-110">
            <img class="w-full h-auto" src="https://source.unsplash.com/nHoaFkrJEx4/600x800" alt="User Avatar" />
          </div>
        </div>
        <div style="width: 20vw; height: 20vw" class="relative overflow-hidden rounded-lg shadow-lg group rotate-1">
          <div class="absolute inset-0 flex items-end justify-center p-4 text-white bg-gradient-to-t from-black/90 via-transparent z-1">
            <div class="text-center">
              <h4 class="mb-1 text-xl font-semibold">Irma Norton</h4>
              <p class="mb-3 font-medium text-gray-300">Founder &amp; CEO</p>
            </div>
          </div>
          <div style="width: 20vw; height: 20vw" class="w-64 transition duration-150 ease-out bg-cover h-60 group-hover:scale-110">
            <img class="w-full h-auto" src="https://source.unsplash.com/nHoaFkrJEx4/600x800" alt="User Avatar" />
          </div>
        </div>
        <div style="width: 20vw; height: 20vw" class="relative overflow-hidden rounded-lg shadow-lg group rotate-1">
          <div class="absolute inset-0 flex items-end justify-center p-4 text-white bg-gradient-to-t from-black/90 via-transparent z-1">
            <div class="text-center">
              <h4 class="mb-1 text-xl font-semibold">Irma Norton</h4>
              <p class="mb-3 font-medium text-gray-300">Founder &amp; CEO</p>
            </div>
          </div>
          <div style="width: 20vw; height: 20vw" class="w-64 transition duration-150 ease-out bg-cover h-60 group-hover:scale-110">
            <img class="w-full h-auto" src="https://source.unsplash.com/nHoaFkrJEx4/600x800" alt="User Avatar" />
          </div>
        </div>
        <!-- 이거 하나씩 끝 -->
      </VueSlickCarousel>
      <div class="relative inset-0 flex justify-between top-80">
          <button @click="showPrev" role="button" aria-label="slide forward" class="z-30 ml-10 border-none hover:scale-125" id="next">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAAEgElEQVRoge2ZTUxcVRiGn3PvAIn9wYC1IrCiZSYuaipVNy6kO9MQaI1jYxtrQglGcGG7tMYxMY0bN6VgsaWxaRN1rC0NdmGIlESNWmHqT7XMtNWWDpCoxIQiOjBzPxeg4tx7Z+bcGdiUdzfnO+f7nnfOmXvO3AMrWtGdLVWIJGHC5u2A7xEw6sWSOgwVQKgAVi90mUYYB4liGEOi1IWxK5GLIUJWvrXzMnC8prfa8tEmsFtBpebwuFKcspKpzpZrT8a9MngycHxDeJ0YJa+LkueAYq/FFzQLqqdIpV7ZM7JjUnewtoFjgd5nEDqAMt2xWTQpQltLrOl9nUE5G+iu6y4yp9d3AXu10TQkcGSsovTF0GB9Mpf+ORnoruu7y5y2ToM8kR9ejlKcT60yg63DDTPZuhrZOsx/88sIDyBsM/9IhUOPX/Bl65rVwPyyWUb4fyRsq5qYOpStW8Yl1OM/t0uQU4Wj0pdCnm6Obg+7x110InCmfE6MEeCeQoA81B7ALDH4+s0fdYdOpsQMtMYafnMKuq6xpGUeREnB4De3+//9rGmi3GekQkC7U9BxBo5u+LBKmeZ18t+kbPAA3x29qmsiUSRmzZ5Yw1h6wPFHrEyznSWCB0jNaR+BSuZItjkFbAZChAxgl26FdLnBX37nOpFDI9r5RKlnw4TN9HabgerApkeBKu0Ki+QG/8PJn/jqjcueciqonKotqktvd1hCRr2nCgtyg49+cJMvD36fT2oEtTW9zWbAgi1eC7jBx86M8vmr34J4zTwvQ5F9BpRFrZfkbvDXem/x2YFvECtPesACWwH7ElJU6CZ2g//543E+fflSQeDn0exsTo/R1Q5trnKDv9E/weC+IaxUYeAXtCa9IethLpOUqSjzr3WM/X51qtDwjnIyMJ3rYEkJAy8NcbN/whbb/IKfh/c/kA+bk26nN9gNCHaaDLKSlquJTS0bC2pCsLM5zIBEdRMvlwkFti3c/hg11LCX5MtkwsZm38iUMeA1+1KbsMTOZjMwdiVyEbjlucjSmRgdj0VsM2A73Q0yKI3rdt4LPOa1kljCjf4Jyjau5e6a/z+619eV4ysxGf/iV72cQuf+yec/SW933AesZKoTmNWqYMvhPhPJREo3XaIYs8sp4Ghg/l2l6tGtki4nE5HDI1w6rPegE+Ftp39jkGkn9iUOgNKbZwctNuEFHpgsNqzX3IIZX6scqz23EyXv6lZ0LGQoT4c6gadaok2n3eIZz0J7Y43vCRzRruoE4gVe6MgEDzkc5kqjs+2iOKtdPU8pUR+N3V+6L1u/rAaCBFPWKnM3ivOFQctJfWtmEsFc3lDndJxuHW6Yid9X2gTqrfzZMkuEjnhF6Y5gPPhnLv21Lzh6/GeDguqkQK8cF4H8YkFbtjWfLu0/NM3R7WF8s36l6AQSuuMd9JcIHYliX0AXHvK85DtR21c5R7INpXYD1ZrDR4GTCtXVHG0c98pQkGvWECGjqvbBLYLaaijqLPAv3Fr+d80KcQUxgSFLjIHxWGS4ENesK1rRna6/AfBPxFyraaOYAAAAAElFTkSuQmCC">
          </button>
          <button @click="showNext" role="button" aria-label="slide forward" class="z-30 mr-16 border-none hover:scale-125" id="next">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAAEz0lEQVRoge2ZW2wUVRjHf2dmWxIBG4RGS0sUwXZtYgm0aPTJkvBASOWirhcaMUJtYmsMRfQBSJbE+Gq0aYFwSYgYdcM1td5IaInEB9IthBfYRRFLdxuN5aFUdMvufD5QIuzM7O6Z2fBC/4/fOef7fv89Z2fOnANTmtL9LVWMJBEi5vVg4GkwGsWSegwVRKgAZkx2GUdIgsQwjAFRqi9xYfBMmLDlt7YvA/sXHJtnBWgTaFZQqTl8WCkOWulMV8svLw57ZfBkYP/CSLkY0z4SJW8CpV6LT2oC1L4Sldm+/uLaUd3B2gb2Bo+9jtAJPKQ7No9GRWhria/+WmdQwQZ21+8uMccf7gY2aqNpSGBXoqLs3XB/Y7qQ/gUZ2F3f84A5bh0CWeEPr0ApejPTzVBrtOlGvq5Gvg63fvl7CA8grDT/zkTCz/cF8nXNa+DWsrmH8LclrKwaGfssX7ecS2hfzfF1ghwsHpW+FPLKhtiaiHu7iw4Ej8y+KcZFYI5OwUeXVzBr4UzO7YzrDMul0YyYwdZ4019Oja5rLG2ZH6NEC/6x5RU0ftKAETBQSnG2O6YL66TZASMTBtqdGh1nYM/Cw1XKNH9F4yV1J/xtRT+9UKyZSJWIuWB9vCmR3eD4J1am2Y7mG3b+isq74AHq33uSRW8/oZPGTdNukm5zarAZCBM2gHW6Ffq3RLnca/uBaOioZVFrtW46m0SpNyJEzOy4zcC8YN0zQJV2gYzQ/4GLiU3+Z0JB5Vh1SX123GEJGY1ei+Q00VFLXYs/E4Jalh2zGbCgwVeRHCaWbq6lbqN3E4Yi/wwoC98LNp+J2ubHPeW1oCY7Zl9CigpP2bMkGeHUh4P8fmIkOz/Pbn2K2nXztXMq7GxOj9EZDjFPstIWJzcNOJvYVufFxMzsQN7NnF9ZaYtrl8bsDQpmVT/oO7+TgXHfWe/QkvYgi9+xLV3ih4f4ecd53XTXswN2A8KILeZRS9qDLG53gD8yxOnt5xBLtPIJdjaHGZCi7MDc4C8du8rpbfrwAAouZsfsj1FDRbUzZ8kN/vK3CX7aetYT/KRsbPYXmTJOes0O7vC/fZfg1JYokvEMjyV2NpuBxIXBM8BVLwVc4b9P0v9+FMsHPDCUjA/mn4EwYUspvtDN7gr/Q5L+zQN+4RHhoNNRpON7wEpnuoAJnQLpVMYWu/Jjkv4O//BAqhSz26nBtr8G6LkWGXthzmtzgaWFVvhj8BqZlEXlc+UAXDkxQl+H72UDgAg734qvcvywdz93CaS2kZ72Ekh5oYXO77kEQHndLPo2DWClfR8+A4yWGtYOt8acxyp7q4+/ipIvdSsqQ/l5VN4lgZdbYqsPubXn3AttjK/6SmCXdtFiwQudueChgM1cWWyiXRRHi0KkISXqm8Tcso58/fIaCBHKWNPNZhS9xUErSD0zb6RChZxQF7Sdbo023Rh+pGw1qJ3+2XJLhM7hirK1oeHQP4X0177g2FdzNCSoLjSPHAsA+dOCtnxrPlvaHzQbYmsiBCZqlKILSOmOd9C/InSmSgNBXXjwecl3oLqn8ibpNpRqBuZpDh8CPleo7g2xVUmvDEW5Zg0TNqqqFzUIapmhqLegZvLW8v9rVhhWEBcYsMQ4mYwPRotxzTqlKd3v+g8ynsUJO26gFAAAAABJRU5ErkJggg==">
          </button>
      </div>
      <div class="text-center">
        <a
          href="#"
          class="inline-flex items-center justify-center px-4 py-3 space-x-2 font-semibold leading-6 text-white bg-gray-700 border border-gray-700 rounded focus:outline-none hover:text-white hover:bg-gray-800 hover:border-gray-800 focus:ring focus:ring-gray-500 focus:ring-opacity-50 active:bg-gray-700 active:border-gray-700"
        >
          Join our team today
        </a>
      </div>
    </div>
  </div>
  <!-- END Team Section: Vertical Photos with Asymmetrical Alignment -->
</template>

<script>
import VueSlickCarousel from 'vue-slick-carousel';
import 'vue-slick-carousel/dist/vue-slick-carousel.css';

import { mapGetters } from 'vuex';
const moviesStore = 'moviesStore';

export default {
  name: 'NowMoviesView',
  components: {
    VueSlickCarousel,
  },
  data() {
    return {
      settings: {
        "dots": true,
        "focusOnSelect": true,
        "infinite": true,
        "speed": 500,
        "slidesToShow": 3,
        "slidesToScroll": 3,
        "touchThreshold": 5
      },
      windowWidth: window.innerWidth,
    };
  },
  computed: {
    ...mapGetters(moviesStore, ['nowmovies']),
  },

  mounted() {},

  methods: {
    showNext() {
          this.$refs.carousel.next();
      },
      showPrev() {
          this.$refs.carousel.prev();
      },
  },
};
</script>

<style scoped>
button.slick-prev:before, button.slick-next:before {
      background-color: red !important;
}
</style>
