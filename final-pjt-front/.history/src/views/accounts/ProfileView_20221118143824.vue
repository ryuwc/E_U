<template>
  <div>
    <h1>profile</h1>
    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path
        x-show="isEmail(formData.email)"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M5 13l4 4L19 7"
      />
      <path
        x-show="!isEmail(formData.email)"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M6 18L18 6M6 6l12 12"
      />
    </svg>
  </div>
</template>

<script>
export default {
  name: "ProfileView",
};
</script>

<style></style>
