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
        <div class="flex">
          <img
              v-if="!isLiked"
              style="width: 24px; height: 24px; position: absolute; right: 10px; top: 2px; hover: scale-110; cursor: pointer;"  
              class="inline-block w-6 h-6 ml-20 rounded-full hover:scale-105"
              src="data:image/png;base64,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"
              @click="toggleLike">
              
          <img src="data:image/png;base64,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"
              v-if="isLiked"
              style="width: 24px; height: 24px; position: absolute; right: 10px; top: 2px; hover: scale-110; cursor: pointer;"  
              class="inline-block w-6 h-6 ml-20 rounded-full hover:scale-105"
              @click="toggleLike">
        </div>  
      </div>
      <p class="mb-3 text-sm font-medium leading-relaxed text-gray-700 grow">
        {{ review.content }}
      </p>
      <footer class="flex items-center justify-between flex-none space-x-4">
        <!-- 여기에 유저 프로필로 이동하는 링크를 넣어야 함 -->
        <router-link :to="{ name:'ProfileView', params: { id: reviewUser.id } }">
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
        </router-link>
        <img
          v-if="review.user === user.id"
          data-bs-toggle="modal"
          data-bs-target="#exampleModal"
          style="cursor: pointer"
          class="ml-48"
          src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABmJLR0QA/wD/AP+gvaeTAAAC9klEQVRYhe2WT2gUZxiHn3fcmIChIkZMBAnMN4VAZA/GnCRS00BFRPQQpFAoiHrRBEERLyYb0UsP1j+1h9KWFgRpC1VEggVJCtJTG5EoNbgzgyDEIIo5uLIxyf48ZJPWaLJ/jLWH/C4fA+/7PQ/vzHwzsJjFvOdYMUW+7y8Hmj3PW1Em50Uul4vjOL5dkkBjY+PSbDZ7EugAKsuEz0TSLWBvHMd/FSOwxDn3K7AdyEkaNLN0mexqYAOwCngObIqiaAAgMVeHc+50Hv7YzNqjKPq9TDgAyWRyWSaT+Q7YBXwDNMEcE3DOdQJngCzQFkXRH28DnyVxH6gxs8YwDP/2Zhf5vr8NOAVI0u6FggMMDg5mgD/zlx/CrFvgnFsHXACWAF1xHF9cKPi/8iy/Ln1FoL6+vg7oBZYDP0VRdGKuHVL9j6qlyWPKce14W10/AJJ19Y8c9mRPUx/XflusjQcQBEFlIpG4CqwFbpjZ54Dm7MpNrEccMaM3dX14C5Kl+kfOmfhCqLtY+IyApE5gPRBWVFTsDMNwbL6mVGvdDeAroEpml7r7Ri5L7AeyMu0pWQDYmhc5ODQ09KRgl5l6Wms7kc4CVcB2w8ZN1n68dc1v5QhMj7uoo3nGw7OZepXYO1ugF8DMvmxoaFhZsEuy7r6RsxIdQBbsCigh0y9dfcOflCxgZueAm0AwPj5+KQiCec/9VN/DFuAAkDVpZ0/r6h1mnAeqTPZDyQJhGI5NTExsAx4ALZJ+ZL6RjlXeQnwtsTXVtuYaZkptru0QHDU4WYrAK3HOrXPOjTrn5Jw7VvZG8zN+ds4pCIJ2+OcZACCKojuSPgMmgR7f9z99Bw7V+XXsNQGAOI6vSjoEmJl975zbuFDkZDK5DGhmavP0GwXyEmcknWfqHb8cBMFHCwHPf45rgIF0On0X/tsfkmagRlLG87xNYRjeLCRAU1NTxejo6Amgk6lpvG0GzGzfNLygwHSCIPhA0gYzK3xIvTkvzOze9NgXs5j/VV4C1B0iTKygwlAAAAAASUVORK5CYII="
        />

        <!-- Button trigger modal -->
        <!-- @click="deleteReview({ reviewId: review.id, authHead: authHead, user: user.id, movieId: movieId })" -->
        
        <!-- Modal -->
        <div
          class="fixed top-0 left-0 hidden w-full h-full overflow-x-hidden overflow-y-auto outline-none modal fade"
          id="exampleModal"
          tabindex="-1"
          aria-labelledby="exampleModalLabel"
          aria-hidden="true"
        >
          <div class="relative w-auto pointer-events-none modal-dialog">
            <div
              
              class="relative flex flex-col w-full text-current bg-white border-none rounded-md shadow-lg outline-none pointer-events-auto modal-content bg-clip-padding"
            >
              <div style="padding-top: 50px; padding-bottom: 50px;" class="relative text-2xl text-center modal-body">정말로 삭제할까요?</div>
              <div class="flex flex-wrap items-center justify-end flex-shrink-0 p-4 border-t modal-footer rounded-b-md">
                <button
                  type="button"
                  class="px-6 py-2.5 text-black border-none font-semibold text-base leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out ml-1"
                  data-bs-dismiss="modal"
                >
                  아니요!
                </button>
                <button
                  id="back_red"
                  type="button"
                  class="px-6 py-2.5 text-black border-none font-semibold text-base leading-tight uppercase rounded shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out ml-1"
                  style=""
                  @click="deleteReview({ reviewId: review.id, authHead: authHead, user: user.id, movieId: movieId })"
                  data-bs-dismiss="modal"
                >
                  네!
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
      isLiked: false,
      reviewUser: {},
    };
  },
  props: {
    review: Object,
  },
  computed: {
    ...mapGetters(moviesStore, ['movieId']),
    ...mapGetters(accountsStore, ['authHead', 'user']),
    nowUser() {
      return JSON.parse(JSON.stringify(this.user))
    },
  },
  methods: {
    toggleLike() {
      console.log('toggleLike 시작');
      this.isLiked = !this.isLiked;
    },
    ...mapActions(moviesStore, ['getReview']),
    ...mapActions(moviesStore, ['deleteReview']),
  },
  created() {
  },
  mounted() {
    axios({
      method: 'get',
      url: `http://localhost:8000/accounts/profile/${this.review.user}/`,
      headers: this.authHead,
    })
      .then((res) => {
        this.reviewUser = JSON.parse(JSON.stringify(res.data))
      })
      .catch((err) => {
        console.log(err);
      });
    this.isLike = false
    console.log(this.isLike);
    // console.log(this.reviewUser);
  },
};
</script>

<style>
#back_red:hover {
  background-color: crimson;
}



#exampleModal {
  z-index: 9999;
}

#personal_review {
  border: black 1px solid;
  border-radius: 10%;
}
</style>
