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
        <button type="button" @click="editUserInfo({ nickname: nickname, profile_path: profile_path })">수정</button>
      </div>
      <div>
        <label for="old_password">현재 비밀번호</label>
        <input type="password" id="old_password" v-model="old_password">
      </div>
      <div>
        <label for="new_password">새 비밀번호</label>
        <input type="password" id="new_password1" v-model="new_password1">
      </div>
      <div>
        <label for="new_password_check">새 비밀번호 확인</label>
        <input type="password" id="new_password2" v-model="new_password2">
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
        old_password: '',
        new_password1: '',
        new_password2: '',
    };
  },
  methods: {
    ...mapActions(accountsStore, ['editUserInfo']),
    ...mapActions(accountsStore, ['editPassword']),
  },
};
</script>

<style scoped>

</style>