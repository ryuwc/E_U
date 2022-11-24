<script setup></script>
<template>
  <div class="pt-5 mt-5">

    <!-- 프로필-->
    <div class="justify-center mt-5 mb-5 d-flex">
      <div class="neon">Hello</div>
      <div class="flux">{{ profileuser.nickname }}'s Profile Page</div>
    </div>
      <!-- 프로필 이미지 -->
    <!-- <div class="mt-5 profile-info-box">
      <div class="mt-5 mb-5 profile-info-box-2">
        <img class="w-30 h-30" :src="profileuser.profile_path">    
        <div class="ml-5">
          <h1>{{ profileuser.nickname }}</h1>
        </div>
      </div>
    </div> -->

    
    <!-- 하단 바 / 찜 & 댓글 -->
    <div class="flex justify-center mt-5">
      <a href="#_" @click.prevent="currentTab = 'PickMovie'" class="px-5 py-2.5 text-black font-medium mx-2 bg-blue-50 hover:bg-blue-100 hover:text-blue-600 text-blue-500 rounded-lg text-sm">찜</a>
      <a href="#_" @click.prevent="currentTab = 'ProfileComment'" class="px-5 py-2.5 text-black font-medium mx-2 bg-blue-50 hover:bg-blue-100 hover:text-blue-600 text-blue-500 rounded-lg text-sm">방명록</a>
    </div>

    <component :is="currentTabComponent"></component>

    <!-- 찜한 영화 목록 -->


  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import ProfileComment from '@/components/ProfileComment.vue'
import PickMovie from '@/components/PickMovie.vue'
const accountsStore = "accountsStore";

export default {
  name: "ProfileView",
  components: {
    ProfileComment,
    PickMovie,
  },

  data() {
    return {
        uername: '',
        nickname: '',
        profile_path: '',
        currentTab: 'PickMovie',
    };

  },
  computed: {
    // 유저 정보 가져오기
    ...mapGetters(accountsStore, ["user", 'username', 'profileuser', 'isLogin']),
      currentTabComponent() {
        return this.currentTab;
      },

    // 로그인 여부 가져오기
    // ...mapGetters(accountsStore, ["isLogin"]),
  },
  
  methods: {
    // 프로필 페이지 유저 정보 갖고오기
    ...mapActions(accountsStore, ['getProfileUser', ]),

  },

  created() {
    // 프로필 페이지 유저 id
    const profileuserId = this.$route.params.id;
    // 현재 프로필 페이지 유저 id getters 에 저장
    this.getProfileUser({ user: profileuserId})

  },

  

};

</script>

<style scoped>

#_body {
  height: 2500px;
}

.dropdown:focus-within .dropdown-menu {
  opacity: 1;
  transform: translate(0) scale(1);
  visibility: visible;
}

.profile-info-box{
  margin-left: 20%;
  margin-right: 70%;
  border-radius: 10px;
}
.profile-info-box-2{
  margin-left: 30%;
}
html,
body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  display: table;
  background-color: black;
}

@font-face {
  font-family: neon;
  src: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/707108/neon.ttf);
}

.container {
  display: table-cell;
  text-align: center;
  vertical-align: middle;
}

.neon {
  font-family: neon;
  color: #FB4264;
  font-size: 40px;
  line-height: 40px;
  text-shadow: 0 0 1vw #F40A35;
}

.flux {
  font-family: neon;
  color: #426DFB;
  font-size: 40px;
  line-height: 40px;
  text-shadow: 0 0 1vw #2356FF;
}

.neon {
  animation: neon 1s ease infinite;
  -moz-animation: neon 1s ease infinite;
  -webkit-animation: neon 1s ease infinite;
}

@keyframes neon {
  0%,
  100% {
    text-shadow: 0 0 1vw #FA1C16, 0 0 3vw #FA1C16, 0 0 10vw #FA1C16, 0 0 10vw #FA1C16, 0 0 .4vw #FED128, .5vw .5vw .1vw #d7b128;
    color: #FED128;
  }
  50% {
    text-shadow: 0 0 .5vw #800E0B, 0 0 1.5vw #800E0B, 0 0 5vw #800E0B, 0 0 5vw #800E0B, 0 0 .2vw #800E0B, .5vw .5vw .1vw #40340A;
    color: #806914;
  }
}

.flux {
  animation: flux 2s linear infinite;
  -moz-animation: flux 2s linear infinite;
  -webkit-animation: flux 2s linear infinite;
  -o-animation: flux 2s linear infinite;
}

@keyframes flux {
  0%,
  100% {
    text-shadow: 0 0 1vw #1041FF, 0 0 3vw #1041FF, 0 0 10vw #1041FF, 0 0 10vw #1041FF, 0 0 .4vw #8BFDFE, .5vw .5vw .1vw #67cede;
    color: #28D7FE;
  }
  50% {
    text-shadow: 0 0 .5vw #082180, 0 0 1.5vw #082180, 0 0 5vw #082180, 0 0 5vw #082180, 0 0 .2vw #082180, .5vw .5vw .1vw #0A3940;
    color: #146C80;
  }
}
</style>
