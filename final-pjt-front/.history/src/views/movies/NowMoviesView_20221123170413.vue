<script setup></script>

<template>
  <!-- Team Section: Vertical Photos with Asymmetrical Alignment -->
  <div class="bg-white">
    <div class="container px-4 py-16 mx-auto space-y-16 xl:max-w-7xl lg:px-8 lg:py-32">
      <!-- Heading -->
      <div class="text-center">
        <h2 class="mb-4 text-3xl font-extrabold md:text-4xl">
          Meet our <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-500 via-pink-500 to-rose-500">passionate</span> team
        </h2>
        <h3 class="mx-auto text-lg font-medium text-gray-600 md:text-xl md:leading-relaxed lg:w-2/3">
          We will help you build amazing web applications and websites. Bring your product live months sooner with our specialized team.
        </h3>
      </div>
      <!-- END Heading -->
  
      <!-- Team -->
      <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4 md:gap-16">
        <div class="relative overflow-hidden rounded-lg shadow-lg group rotate-1">
          <div class="absolute inset-0 flex items-end justify-center p-4 text-white bg-gradient-to-t from-black/90 via-transparent z-1">
            <div class="text-center">
              <h4 class="mb-1 text-xl font-semibold">
                Irma Norton
              </h4>
              <p class="mb-3 font-medium text-gray-300">
                Founder &amp; CEO
              </p>
            </div>
          </div>
          <div class="transition duration-150 ease-out aspect-w-3 aspect-h-4 group-hover:scale-110">
            <img src="https://source.unsplash.com/nHoaFkrJEx4/600x800" alt="User Avatar">
          </div>
        </div>
        <div class="relative overflow-hidden rounded-lg shadow-lg group -rotate-1">
          <div class="absolute inset-0 flex items-end justify-center p-4 text-white bg-gradient-to-t from-black/90 via-transparent z-1">
            <div class="text-center">
              <h4 class="mb-1 text-xl font-semibold">
                Alejandro Lee
              </h4>
              <p class="mb-3 font-medium text-gray-300">
                Product Design
              </p>
            </div>
          </div>
          <div class="transition duration-150 ease-out aspect-w-3 aspect-h-4 group-hover:scale-110">
            <img src="https://source.unsplash.com/euZ2n8dGUcQ/600x800" alt="User Avatar">
          </div>
        </div>
        <div class="relative overflow-hidden rounded-lg shadow-lg group rotate-1">
          <div class="absolute inset-0 flex items-end justify-center p-4 text-white bg-gradient-to-t from-black/90 via-transparent z-1">
            <div class="text-center">
              <h4 class="mb-1 text-xl font-semibold">
                John Smith
              </h4>
              <p class="mb-3 font-medium text-gray-300">
                Web Designer
              </p>
            </div>
          </div>
          <div class="transition duration-150 ease-out aspect-w-3 aspect-h-4 group-hover:scale-110">
            <img src="https://source.unsplash.com/d2MSDujJl2g/600x800" alt="User Avatar">
          </div>
        </div>
        <div class="relative overflow-hidden rounded-lg shadow-lg group -rotate-1">
          <div class="absolute inset-0 flex items-end justify-center p-4 text-white bg-gradient-to-t from-black/90 via-transparent z-1">
            <div class="text-center">
              <h4 class="mb-1 text-xl font-semibold">
                Alex Saunders
              </h4>
              <p class="mb-3 font-medium text-gray-300">
                Marketing
              </p>
            </div>
          </div>
          <div class="transition duration-150 ease-out aspect-w-3 aspect-h-4 group-hover:scale-110">
            <img src="https://source.unsplash.com/ZGa9d1a_4tA/600x800" alt="User Avatar">
          </div>
        </div>
      </div>
      <!-- END Team -->
  
      <!-- Action -->
      <div class="text-center">
        <a href="#" class="inline-flex items-center justify-center px-4 py-3 space-x-2 font-semibold leading-6 text-white bg-gray-700 border border-gray-700 rounded focus:outline-none hover:text-white hover:bg-gray-800 hover:border-gray-800 focus:ring focus:ring-gray-500 focus:ring-opacity-50 active:bg-gray-700 active:border-gray-700">
          Join our team today
        </a>
      </div>
      <!-- END Action -->
    </div>
  </div>
  <!-- END Team Section: Vertical Photos with Asymmetrical Alignment -->
</template>

<script>
// import VueSlickCarousel from 'vue-slick-carousel';
import 'vue-slick-carousel/dist/vue-slick-carousel.css';

import { mapGetters } from 'vuex';
const moviesStore = 'moviesStore';

export default {
  name: 'NowMoviesView',
  components: {
    // VueSlickCarousel,
  },
  data() {
    return {
      settings: {
        dots: false,
        focusOnSelect: true,
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 3,
        touchThreshold: 5,
        centerPadding: '10%'
      },
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
.slick-slide {
  margin: 0 20px;
}
</style>
