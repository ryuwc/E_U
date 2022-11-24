<script setup></script>
<template >
  <div class="pt-5 mt-5">

    <!-- 프로필-->
    <div class="justify-center mt-5 mb-5 d-flex">
      <h2>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-500 via-pink-500 to-rose-500">Hello, {{ profileuser.nickname }}'s profile</span>
      </h2>
    </div>


    
    <!-- 하단 바 / 찜 & 댓글 -->
    <div class="flex justify-center clickbar">
      <a href="#_" @click.prevent="currentTab = 'PickMovie'" class="px-5 py-2.5 text-black font-medium mx-2 bg-blue-50 hover:bg-blue-100 hover:text-blue-600 text-blue-500 rounded-lg text-sm">찜</a>
      <a href="#_" @click.prevent="currentTab = 'ProfileComment'" class="px-5 py-2.5 text-black font-medium mx-2 bg-blue-50 hover:bg-blue-100 hover:text-blue-600 text-blue-500 rounded-lg text-sm">방명록</a>
    </div>

    <div class="choiceCP">
      <component :is="currentTabComponent"></component>
    </div>
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

.choiceCP {

  margin-left: 10%;
  margin-right: 10%;

}
.clickbar{
  margin-top: 10%;
  margin-bottom: 10%;
}

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



</style>
