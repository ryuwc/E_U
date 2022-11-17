<template>
  <div>
    <h4>회원정보수정</h4>
    <form>
      <div>
        <label for="nickname">닉네임</label>
        <input type="text" id="nickname" v-model="nickname">
      </div>
      <div>
        <label for="profile_path">프로필 이미지</label>
        <input type="text" id="profile_path" v-model="profile_path">
      </div>
      <div>
        <button type="button" @click="editUser({ nickname: nickname, profile_path: profile_path })">수정</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

const accountsStore = 'accountsStore'

export default {
  name: 'EditUserView',
  data() {
    return {
        nickname: '',
        profile_path: '',
    };
  },
  methods: {
    ...mapActions(accountsStore, ['editUser']),
  },
};
</script>

<style scoped>

</style>