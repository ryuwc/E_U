<template>
  <div class="justify-center m-5 d-flex profile-box">
    <div class="mt-5">
      <CreateComment/>
      <CommentList
      class="mb-2"
      v-for="(comment, index) in comments" 
      :key="index"
      :comment="comment"
      />
    </div>  
  </div>
</template>

<script>
import CreateComment from '@/components/CreateComment.vue'
import CommentList from '@/components/CommentList.vue'

import { mapActions, mapGetters } from 'vuex';

const accountsStore = 'accountsStore'
const commentsStore = 'commentsStore'

export default {
  name: 'ProfileComment',
  components: {
    CreateComment,
    CommentList,
  },
  computed: {
    ...mapGetters(accountsStore, ['profileuser', 'authHead']),
    ...mapGetters(commentsStore, ['comments', ])
  },

  methods: {
    ...mapActions(commentsStore, ['getComments']),

  },

  created() {
    this.getComments({id: this.profileuser, token: this.authHead})
    // console.log(this.comments) => profile: profile_user_id , user: user_id
  }
}
</script>

<style>
.profile-box{
  border-radius: 20px;
  background-color: rgb(239 246 255);
}
</style>