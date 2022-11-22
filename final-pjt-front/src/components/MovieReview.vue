<template>
  <div>
      <CreateReview
      style="margin-bottom: 8px;"
      v-if="user.username"
      />
      <MovieReviewItem
      class="mb-2"
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
const accountsStore = 'accountsStore'

export default {
  name: 'MovieReview',
  components:{
    MovieReviewItem,
    CreateReview,
  },
  computed: {
    ...mapGetters(moviesStore, ['reviews']),
    ...mapGetters(accountsStore, ['user']),
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