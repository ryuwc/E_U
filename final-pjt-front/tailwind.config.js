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
      './src/views/TestTwoView.vue',
      // './src/components/MoviveCard.vue',
      './src/components/PosterSlider.vue',
      './src/components/MovieClip.vue',
      './src/components/MovieDetailR.vue',
      './src/Views/movies/NowMoviesView.vue',
      // '/src/Views/testThreeView.vue',
      './src/components/FooTer.vue',
      './src/Vies/AllMovieView.vue',
      // './src/App.vue',
    ],
  theme: {
    extend: {},
  },
  plugins: [],
}
