<template>
  <div>
   <h1>임시 임시</h1>
  
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
const commentsStore = "commentsStore";
const accountsStore = "accountsStore";


export default {
  name: 'TestThree',

  data() {
    return {};
  },

  computed: {
    ...mapGetters(accountsStore, ["user", 'authHead']),
  },

  methods: {
    ...mapActions(commentsStore, ['createProfileUser'])
  },

  created() {
    console.log(this.user)
    this.createProfileUser({ usernumber: this.user.id,  authHead: this.authHead})
  },

};
</script>

<style scoped>
*{
  color: black
}
</style>
