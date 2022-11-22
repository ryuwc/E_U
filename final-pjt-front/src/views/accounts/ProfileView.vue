<script setup></script>
<template>
  <div>

    <!-- 프로필-->
    <div>
      <h1>{{ profileuser.username }} 의 프로필 페이지 입니다</h1>
      
      <!-- 프로필 이미지 -->
      <div>
        <img class="w-22 h-22" :src="profile_path">    
      </div>
      
      <!-- 계정 정보 -->
      <div>
        
      </div>
    
    </div>
    
    <!-- 찜한 영화 목록 -->
    <div>
      <div>
        <h1>{{ profileuser.username }} 의 찜한 영화 목록
          
        </h1>
        <PickMovie/>
      </div>
    </div>
    
    <!-- 방명록 -->
    <div>
      <CreateComment/>
      <CommentList/>
    </div>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import CreateComment from '@/components/CreateComment.vue'
import CommentList from '@/components/CommentList.vue'
const accountsStore = "accountsStore";

export default {
  name: "ProfileView",
  components: {
    CreateComment,
    CommentList,
  },
  data() {
    return {
        uername: '',
        nickname: '',
        profile_path: '',
    };
  },
  computed: {
    // 유저 정보 가져오기
    ...mapGetters(accountsStore, ["user", 'username', 'profileuser']),
    
    // 로그인 여부 가져오기
    // ...mapGetters(accountsStore, ["isLogin"]),
  },
  
  methods: {
    // 프로필 페이지 유저 정보 갖고오기
    ...mapActions(accountsStore, ['getProfileUser'])
  },

  created() {
    // 프로필 페이지 유저 id
    const profileuserId = this.$route.params.id;
    this.getProfileUser(profileuserId)
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
</style>
