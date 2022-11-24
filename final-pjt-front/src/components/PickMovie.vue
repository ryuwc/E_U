<template>
  <div>
    <div class="flex justify-center">
      <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4 md:gap-16">
        <div class="relative overflow-hidden rounded-lg shadow-lg group"
        v-for="(movie, index) in nowUserWishList"
        :key="index"
        :movie="movie"
        >
          <router-link :to="{ name:'MovieDetailInfoView', params: { id: movie.id } }">
            <div class="absolute inset-0 flex items-end justify-center p-4 bg-gradient-to-t from-black/90 via-transparent z-1">
              <div class="text-center">
                <h4 id="h4Tag" class="mb-1 text-xl font-semibold">
                  {{ movie.title }}
                </h4>
              </div>
            </div>
            <img class="transition duration-150 ease-out aspect-w-3 aspect-h-4 group-hover:scale-110" style="width: 100%; height: 20vw;" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`">
          </router-link>
        </div>  
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
const moviesStore = 'moviesStore'
const accountsStore = 'accountsStore'

export default {
  name: 'PickMovie',
  computed: {
  ...mapGetters(moviesStore, ['nowUserWishList']),
  ...mapGetters(accountsStore, ['profileuser', 'authHead', 'user'])
  },

  methods: {
    ...mapActions(moviesStore, ['getNowUserWishList'])
  },

  created() {
    this.getNowUserWishList({userId: this.profileuser.id, authHead: this.authHead})
  }

}
</script>

<style>

#h4Tag {
  color:white
}

.h1Tag {
 justify-content: center; 
}

</style>