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
              <div style="padding-top: 20px; padding-right: 20px;" class="relative text-lg modal-body">정말로 삭제할까요?</div>
              <div class="flex flex-wrap items-center justify-end flex-shrink-0 p-4 border-t border-gray-200 modal-footer rounded-b-md">
                <button
                  type="button"
                  class="px-6 py-2.5 bg-purple-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-purple-700 hover:shadow-lg focus:bg-purple-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-purple-800 active:shadow-lg transition duration-150 ease-in-out"
                  data-bs-dismiss="modal"
                >
                  Close
                </button>
                <button
                  type="button"
                  class="px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out ml-1"
                >
                  Save changes
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
#exampleModal {
  z-index: 9999;
}

#personal_review {
  border: black 1px solid;
  border-radius: 10%;
}
</style>
