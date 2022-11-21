<template>
  <div>
    <div class="relative flex flex-col px-6 pt-4 bg-white border border-gray-200 group md:px-8 rounded-xl">
      <blockquote class="relative flex flex-col grow">
        <div class="flex items-center ml-3">
          <div class="mr-3">
            <img :src="user.profile_path" alt="Avatar Photo" class="w-12 h-12" />
            <p>{{ user.nickname ? user.nickname : user.username }}</p>
          </div>
          
        </div>
        <div class="w-full mt-3">
          <textarea rows="3" class="w-full p-2 border rounded" placeholder="리뷰를 남겨주세요!"></textarea>
        </div>
        <div class="flex justify-between mx-3">
          <div><button class="px-4 py-1 font-light text-white bg-gray-800 rounded hover:bg-gray-700">Submit</button></div>
        </div>
        
      </blockquote>
    </div>
  </div>
    
  <!-- <div>
    <div>
      <input type="text" v-model.trim="content" placeholder="리뷰를 작성하세요">
    </div>
    <div>
      <input type="text" v-model.trim="rank" @keyup.enter="createReview" placeholder="1부터 5까지 평점을 입력하세요">
    </div>
    <button type="button" class="btn" @click="[createReview({ content: content, movieId: movieId, rank: rank, user: user.id, authHead: authHead  }), cleanData()]">등록하기</button>
  </div> -->
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
const moviesStore = 'moviesStore';
const accountsStore = 'accountsStore';

export default {
  name: 'CreateReview',
  computed: {
    ...mapGetters(moviesStore, ['movieId']),
    ...mapGetters(accountsStore, ['authHead', 'user']),
  },
  data() {
    return {
      content: null,
      rank: null,
    };
  },
  methods: {
    cleanData() {
      this.content = null;
      this.rank = null;
    },
    ...mapActions(moviesStore, ['createReview']),
  },
  created() {
    this.movieID = this.movieId;
  },
};
</script>

<style></style>
