/** @type {import('tailwindcss').Config} */
module.exports = {
  corePlugins: {
    preflight: false,
  },
  content: ['./src/views/accounts/*.{vue,js,ts,jsx,tsx}', './src/views/movies/MovieDetailInfoView.vue'],
  theme: {
    extend: {},
  },
  plugins: [],
}
