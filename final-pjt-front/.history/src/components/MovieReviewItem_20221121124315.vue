<template>
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
            v-for="n in review.rank"
            :key="n"
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
      <p class="mb-3 text-sm font-medium leading-relaxed text-gray-700 grow">
        {{ review.content }}
      </p>
      <footer class="flex items-center justify-between flex-none space-x-4">
        <!-- 여기에 유저 프로필로 이동하는 링크를 넣어야 함 -->
        <div class="flex items-center">
          <a
            href="#"
            class="flex-none w-12 h-12 overflow-hidden transition duration-150 ease-out transform border-2 rounded-full border-gray-50 hover:border-white hover:shadow-md hover:scale-125 active:border-gray-50 active:shadow-sm active:scale-110"
          >
            <img :src="reviewUser.profile_path" alt="Avatar Photo" class="object-cover w-full h-full" />
            />
          </a>
          <div class="flex ml-5">
            <a href="#" class="font-semibold text-blue-600 hover:text-blue-400"> {{ reviewUser.nickname ? reviewUser.nickname : reviewUser.username }} </a>
          </div>
        </div>
        <img
          v-if="review.user === user.id"
          @click="deleteReview({ reviewId: review.id, authHead: authHead, user: user.id, movieId: movieId })"
          style="cursor: pointer"
          class="ml-48"
          src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABmJLR0QA/wD/AP+gvaeTAAAC9klEQVRYhe2WT2gUZxiHn3fcmIChIkZMBAnMN4VAZA/GnCRS00BFRPQQpFAoiHrRBEERLyYb0UsP1j+1h9KWFgRpC1VEggVJCtJTG5EoNbgzgyDEIIo5uLIxyf48ZJPWaLJ/jLWH/C4fA+/7PQ/vzHwzsJjFvOdYMUW+7y8Hmj3PW1Em50Uul4vjOL5dkkBjY+PSbDZ7EugAKsuEz0TSLWBvHMd/FSOwxDn3K7AdyEkaNLN0mexqYAOwCngObIqiaAAgMVeHc+50Hv7YzNqjKPq9TDgAyWRyWSaT+Q7YBXwDNMEcE3DOdQJngCzQFkXRH28DnyVxH6gxs8YwDP/2Zhf5vr8NOAVI0u6FggMMDg5mgD/zlx/CrFvgnFsHXACWAF1xHF9cKPi/8iy/Ln1FoL6+vg7oBZYDP0VRdGKuHVL9j6qlyWPKce14W10/AJJ19Y8c9mRPUx/XflusjQcQBEFlIpG4CqwFbpjZ54Dm7MpNrEccMaM3dX14C5Kl+kfOmfhCqLtY+IyApE5gPRBWVFTsDMNwbL6mVGvdDeAroEpml7r7Ri5L7AeyMu0pWQDYmhc5ODQ09KRgl5l6Wms7kc4CVcB2w8ZN1n68dc1v5QhMj7uoo3nGw7OZepXYO1ugF8DMvmxoaFhZsEuy7r6RsxIdQBbsCigh0y9dfcOflCxgZueAm0AwPj5+KQiCec/9VN/DFuAAkDVpZ0/r6h1mnAeqTPZDyQJhGI5NTExsAx4ALZJ+ZL6RjlXeQnwtsTXVtuYaZkptru0QHDU4WYrAK3HOrXPOjTrn5Jw7VvZG8zN+ds4pCIJ2+OcZACCKojuSPgMmgR7f9z99Bw7V+XXsNQGAOI6vSjoEmJl975zbuFDkZDK5DGhmavP0GwXyEmcknWfqHb8cBMFHCwHPf45rgIF0On0X/tsfkmagRlLG87xNYRjeLCRAU1NTxejo6Amgk6lpvG0GzGzfNLygwHSCIPhA0gYzK3xIvTkvzOze9NgXs5j/VV4C1B0iTKygwlAAAAAASUVORK5CYII="
        />
        <button
          class="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          type="button"
          data-modal-toggle="popup-modal"
        >
          Toggle modal
        </button>

        <div id="popup-modal" tabindex="-1" class="fixed top-0 left-0 right-0 z-50 hidden p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-modal md:h-full">
          <div class="relative w-full h-full max-w-md md:h-auto">
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
              <button
                type="button"
                class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-800 dark:hover:text-white"
                data-modal-toggle="popup-modal"
              >
                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path
                    fill-rule="evenodd"
                    d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
                <span class="sr-only">Close modal</span>
              </button>
              <div class="p-6 text-center">
                <svg
                  aria-hidden="true"
                  class="mx-auto mb-4 text-gray-400 w-14 h-14 dark:text-gray-200"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <h3 class="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400">Are you sure you want to delete this product?</h3>
                <button
                  data-modal-toggle="popup-modal"
                  type="button"
                  class="text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 font-medium rounded-lg text-sm inline-flex items-center px-5 py-2.5 text-center mr-2"
                >
                  Yes, I'm sure
                </button>
                <button
                  data-modal-toggle="popup-modal"
                  type="button"
                  class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-200 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600"
                >
                  No, cancel
                </button>
              </div>
            </div>
          </div>
        </div>
      </footer>
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
      reviewUser: {},
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
