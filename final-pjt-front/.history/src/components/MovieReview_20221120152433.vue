<template>
  <div>
    <h1>movie review</h1>
      <CreateReview/>
      <MovieReviewItem
      v-for="(review, index) in reviews" 
      :key="index"
      :review="review"
      />
    <div>
  
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import MovieReviewItem from '@/components/MovieReviewItem.vue'
import CreateReview from '@/components/CreateReview.vue'
const moviesStore = 'moviesStore'

export default {
  name: 'MovieReview',
  components:{
    MovieReviewItem,
    CreateReview,
  },
  computed: {
    ...mapGetters(moviesStore, ['reviews'])
  },
  methods: {
    ...mapActions(moviesStore, ['getReview']),
  },
  created() {
    const movieId = this.$route.params.id
    this.getReview(movieId)
  }
}
</script>

<style>

</style>