<template>
  <body style="margin-top: 7rem; top: 0;">
    <div class="menu">
      <div class="toggle"></div>
    </div>
  </body>
</template>

<script>
export default {
  name: 'FeelingMovieView',

  data() {
    return {
      
    };
  },

  mounted() {
    
  },

  methods: {
    
  },
};
</script>

<style scoped>
.menu {
  position: relative;
  width: 280px;
  height: 280px;
  background: rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: center;
  align-items: center;
}

.menu .toggle {
  position: relative;
  width: 60px;
  height: 60px;
  background: #fff;
  border-radius: 50%;
  box-shadow: 0 3px 4px rgba(0, 0, 0, 0.15);
}

</style>