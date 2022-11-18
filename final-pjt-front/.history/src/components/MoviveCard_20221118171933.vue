<template>
  <div>
    <router-link :to="{ name:'MovieDetailInfoView', params: { id: movie.id } }">
        <div id="card-div" class="m-3 card" style="width: 18rem;" data-toggle="tab-hover">
            <img :src="`https://image.tmdb.org/t/p/w185${movie.poster_path}`" class="mt-2 h-100 card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title text-truncate">{{ movie.title }}</h5>
              <p class="card-text">평점: {{ movie.vote_average }}</p>
            </div>
        </div>
    </router-link>  
  </div>
  </template>
  
  <script>
  export default {
    name: 'MovieCard',
    props: {
      movie: Object
    }
  }
  </script>
  
  <style>
  
  </style>