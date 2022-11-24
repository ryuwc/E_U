<template>
  <div>
    <div class="relative flex flex-col px-6 pt-4 bg-white border border-gray-200 group md:px-8 rounded-xl">
      <blockquote class="relative flex flex-col grow">
        <div class="flex items-center ml-3">
          <div class="flex items-center mr-3">
            <img :src="user.profile_path" alt="Avatar Photo" class="w-12 h-12" />
            <p style="margin-bottom: 0; margin-left: 10px; color: black;" class="text-lg">{{ user.nickname ? user.nickname : user.username }}</p>
            <form name="myform" id="myform" method="post" action="./save">
              <fieldset class="mb-1 ml-10">
                <legend></legend>
                <input type="radio" name="rating" value="5" id="rate1" /><label for="rate1"
                @click="rank=5"
                >⭐</label>
                <input type="radio" name="rating" value="4" id="rate2" /><label for="rate2"
                @click="rank=4"
                >⭐</label>
                <input type="radio" name="rating" value="3" id="rate3" /><label for="rate3"
                @click="rank=3"
                >⭐</label>
                <input type="radio" name="rating" value="2" id="rate4" /><label for="rate4"
                @click="rank=2"
                >⭐</label>
                <input type="radio" name="rating" value="1" id="rate5" /><label for="rate5"
                @click="rank=1"
                >⭐</label>
              </fieldset>
            </form>
          </div>
        </div>
        <div class="w-full mt-3">
          <textarea rows="1" class="w-full p-2 border rounded" required placeholder="리뷰를 남겨주세요!"
          v-model.trim="content"
          ></textarea>
        </div>
        <div class="flex justify-between">
          <div><button class="px-4 py-1 mb-1 font-light text-white bg-gray-800 rounded hover:bg-gray-700"
            @click="[createReview({ content: content, movieId: movieId, rank: rank, user: user.id, authHead: authHead  }), cleanData()]"
            >작성!</button></div>
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

<style scoped>
* {
  color: black;
  font-family: 'Jua', sans-serif;
}

#myform fieldset{
    display: inline-block; /* 하위 별점 이미지들이 있는 영역만 자리를 차지함.*/
    direction: rtl; /* 이모지 순서 반전 */
    border: 0; /* 필드셋 테두리 제거 */
}
#myform fieldset legend{
    text-align: left;
}
#myform input[type=radio]{
    display: none; /* 라디오박스 감춤 */
}
#myform label{
    font-size: 1.5rem; /* 이모지 크기 */
    color: transparent; /* 기존 이모지 컬러 제거 */
    text-shadow: 0 0 0 #f0f0f0; /* 새 이모지 색상 부여 */
}
#myform label:hover{
    text-shadow: 0 0 0 rgb(175, 211, 233); /* 마우스 호버 */
}
#myform label:hover ~ label{
    text-shadow: 0 0 0 rgb(175, 211, 233); /* 마우스 호버 뒤에오는 이모지들 */
}
#myform input[type=radio]:checked ~ label{
    text-shadow: 0 0 0 #3ba7ea; /* 마우스 클릭 체크 */
}


</style>
