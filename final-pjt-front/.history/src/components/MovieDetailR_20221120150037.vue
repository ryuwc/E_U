<template>
  <div>
    <h1>MovieDetailR</h1>
    <div>
        <button @click="currentTab = 'MovieReview'">리뷰 및 평점</button>
        <button @click="currentTab = 'MovieClip'">무비 클립</button>
        <component :is="currentTabComponent"></component>
    </div>
  </div>
</template>

<script>
import MovieReview from '@/components/MovieReview.vue'
import MovieClip from '@/components/MovieClip'
export default {
    name: 'MovieDetailR',
    components: {
        MovieReview,
        MovieClip
    },
    data() {
        return {
            currentTab: 'MovieReview'
        }
    },
    computed: {
        currentTabComponent() {
            return this.currentTab
        }
    }
}
</script>

<style>

</style>