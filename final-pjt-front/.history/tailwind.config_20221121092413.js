/** @type {import('tailwindcss').Config} */
module.exports = {
  corePlugins: {
    preflight: false,
  },
  content: [
      './src/views/accounts/*.{vue,js,ts,jsx,tsx}',
      './src/views/movies/MovieDetailInfoView.vue',
      './src/views/NotPound404View.vue',
      './src/components/ReviewCandi1.vue',
      // './src/components/MoviveCard.vue',
    ],
  theme: {
    extend: {},
  },
  plugins: [],
}
