<template>
  <div class="relative group w-96">
        <img class="object-cover w-full"
            src="https://www.kindacode.com/wp-content/uploads/2022/06/t-shirt-example.png" />
        <div
            class="absolute top-0 left-0 flex flex-col items-center justify-center w-full h-0 duration-500 bg-indigo-700 opacity-0 group-hover:h-full group-hover:opacity-100">
            <h1 class="text-2xl text-white">Fiction T-Shirt Store</h1>
            <a class="px-8 py-3 mt-5 duration-300 rounded-full bg-amber-400 hover:bg-amber-600" href="#">Continue Shopping</a>
        </div>
    </div>

</template>


<!-- <template>
  <div>

    <ReviewCandi1/>
  </div>
</template> -->

<script>
// import ReviewCandi1 from '@/components/ReviewCandi1.vue';

export default {
  name: 'TestView',

  data() {
    return {
      
    };
  },
  components: {
    // ReviewCandi1,
  },

  mounted() {
    
  },

  methods: {
    
  },
};
</script>

<style scoped>

</style>