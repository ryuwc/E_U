<template>
  <div class="flex items-center justify-center h-screen bg-gray-800">
    <div class="w-1/2 p-2 pt-4 bg-white rounded shadow-lg">
      <div class="flex ml-3">
        <div class="mr-3">
          <img src="http://picsum.photos/50" alt="" class="rounded-full" />
        </div>
        <div>
          <h1 class="font-semibold">Itay Buyoy</h1>
          <p class="text-xs text-gray-500">2 seconds ago</p>
        </div>
      </div>
      <div class="w-full p-3 mt-3">
        <textarea rows="3" class="w-full p-2 border rounded" placeholder="Write something..."></textarea>
      </div>
      <div class="flex justify-between mx-3">
        <div><button class="px-4 py-1 font-light text-white bg-gray-800 rounded hover:bg-gray-700">Submit</button></div>
      </div>
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
