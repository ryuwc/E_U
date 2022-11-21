<template>
  <div>
    <div class="relative flex flex-col px-6 pt-4 bg-white border border-gray-200 group md:px-8 rounded-xl">
      <blockquote class="relative flex flex-col grow">
        <div class="mb-2">
          <div
            class="inline-flex items-center px-2 py-1 text-blue-600 transition ease-out origin-top-left border border-blue-100 rounded-lg bg-blue-50 group-hover:scale-110"
          >
            <svg
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
              class="inline-block w-5 h-5 hi-solid hi-star"
            >
              <path
                fill-rule="evenodd"
                d="M10 2.5l2.928 5.364 6.072.866-4.428 4.286 1.072 6.07L10 14.93 4.5 18l1.072-6.07L0 7.23l6.072-.866L10 2.5z"
                clip-rule="evenodd"
              ></path>
              >
              <path
                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
              ></path>
            </svg>
          </div>
        </div>
        
      </blockquote>
    </div>

    <div class="relative flex flex-col mb-2 bg-white border border-gray-200 group md:px-8 rounded-xl">
      <div class="w-full rounded shadow-lg">
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
          <textarea rows="3" class="w-full p-2 border rounded" placeholder="리뷰를 남겨주세요!"></textarea>
        </div>
        <div class="flex justify-between mx-3">
          <div><button class="px-4 py-1 font-light text-white bg-gray-800 rounded hover:bg-gray-700">Submit</button></div>
        </div>
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
