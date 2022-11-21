<template>
  <div class="relative flex flex-col px-6 pt-4 bg-white border border-gray-200 group md:px-8 rounded-xl">
    <blockquote class="relative flex flex-col grow">
      <div class="mb-2">
        <div
          class="inline-flex items-center px-2 py-1 text-blue-600 transition ease-out origin-top-left border border-blue-100 rounded-lg bg-blue-50 group-hover:scale-110"
        >
          <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="inline-block w-5 h-5 hi-solid hi-star"
          v-for="n in review.rank" :key="n">
            <path fill-rule="evenodd" d="M10 2.5l2.928 5.364 6.072.866-4.428 4.286 1.072 6.07L10 14.93 4.5 18l1.072-6.07L0 7.23l6.072-.866L10 2.5z" clip-rule="evenodd"></path>
          >
            <path
              d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
            ></path>
          </svg>
        </div>
      </div>
      <p class="mb-3 text-sm font-medium leading-relaxed text-gray-700 grow">
        {{ review.content }}
      </p>
      <footer class="flex items-center flex-none space-x-4">
        <!-- 여기에 유저 프로필로 이동하는 링크를 넣어야 함 -->
        <a
          href="#"
          class="flex-none w-12 h-12 overflow-hidden transition duration-150 ease-out transform border-2 rounded-full border-gray-50 hover:border-white hover:shadow-md hover:scale-125 active:border-gray-50 active:shadow-sm active:scale-110"
        >
          <img :src="reviewUser.profile_path" alt="Avatar Photo"
          class="object-cover w-full h-full">
          />
        </a>
        <div class="flex">
          <a href="#" class="font-semibold text-blue-600 hover:text-blue-400"> {{ reviewUser.nickname ? reviewUser.nickname : reviewUser.username }} </a>
        </div>
        <img src="data:image/png;base64,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">
      </footer>
      <button @click="test">ㅇㅇㅇ</button>
    </blockquote>
  </div>

  <!-- 기존 스켈레톤 코드 -->
  <!-- <div id='personal_review'>
      <div>평점: {{ review.rank }}</div>
      <div>작성시간 : {{ review.created_at }}</div>
      <div>사용자: {{ review.user }}</div>
      <div>{{ review.content }}</div>
      <div>좋아요한 사용자 수 : {{ review.good_user.length }} | 싫어요 한 사용자 수 : {{review.bad_user.length }}</div>
       <button type="button" class="btn btn-sm" @click="deleteReview({ reviewId : review.id, authHead : authHead, user:user.id, movieId: movieId })">x</button>
  </div> -->
</template>

<script>
import axios from 'axios';
import { mapActions, mapGetters } from 'vuex';
const moviesStore = 'moviesStore';
const accountsStore = 'accountsStore';

export default {
  name: 'MovieReviewItem',
  data() {
    return {
      reviewUser : {},
    };
  },
  props: {
    review: Object,
  },
  computed: {
    ...mapGetters(moviesStore, ['movieId']),
    ...mapGetters(accountsStore, ['authHead', 'user']),
  },
  methods: {
    ...mapActions(moviesStore, ['deleteReview']),
    test() {
      window.prompt('삭제하시겠습니까?');

    },
  },
  mounted() {
    axios({
      method: 'get',
      url: `http://localhost:8000/accounts/profile/${this.review.user}/`,
      headers: this.authHead,
    })
      .then((res) => {
        this.reviewUser = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
    console.log(this.reviewUser);
  },
};
</script>

<style>
#personal_review {
  border: black 1px solid;
  border-radius: 10%;
}
</style>
