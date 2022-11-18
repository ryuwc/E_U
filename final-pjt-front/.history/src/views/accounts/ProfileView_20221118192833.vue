<template>
  <nav>
    <button
      id="dropdownUserAvatarButton"
      data-dropdown-toggle="dropdownAvatar"
      class="flex mx-3 text-sm bg-gray-800 rounded-full md:mr-0 focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600"
      type="button"
    >
      <span class="sr-only">Open user menu</span>
      <img
        class="w-8 h-8 rounded-full"
        src="/docs/images/people/profile-picture-3.jpg"
        alt="user photo"
      />
    </button>

    <!-- Dropdown menu -->
    <div
      id="dropdownAvatar"
      class="z-10 hidden bg-white divide-y divide-gray-100 rounded shadow w-44 dark:bg-gray-700 dark:divide-gray-600"
    >
      <div class="px-4 py-3 text-sm text-gray-900 dark:text-white">
        <div>Bonnie Green</div>
        <div class="font-medium truncate">name@flowbite.com</div>
      </div>
      <ul
        class="py-1 text-sm text-gray-700 dark:text-gray-200"
        aria-labelledby="dropdownUserAvatarButton"
      >
        <li>
          <a
            href="#"
            class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
            >Dashboard</a
          >
        </li>
        <li>
          <a
            href="#"
            class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
            >Settings</a
          >
        </li>
        <li>
          <a
            href="#"
            class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
            >Earnings</a
          >
        </li>
      </ul>
      <div class="py-1">
        <a
          href="#"
          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"
          >Sign out</a
        >
      </div>
    </div>
  </nav>
</template>

<script>
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
};
</script>

<style></style>
