<script setup></script>

<template>
  <div>
    <div class="dropdown">
      <a
        class="btn btn-secondary dropdown-toggle"
        href="#"
        role="button"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        Dropdown link
      </a>

      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Action</a></li>
        <li><a class="dropdown-item" href="#">Another action</a></li>
        <li><a class="dropdown-item" href="#">Something else here</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

const accountsStore = "accountsStore";

export default {
  name: "ProfileView",
  data() {
    return {
      showMenu: false,
    };
  },
  methods: {
    toggleNavbar() {
      this.showMenu = !this.showMenu;
    },
  },
  components: {},
  computed: {
    // 유저 정보 가져오기
    ...mapGetters(accountsStore, ["user"]),
    // 로그인 여부 가져오기
    ...mapGetters(accountsStore, ["isLogin"]),
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
