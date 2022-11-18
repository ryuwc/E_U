<template>
  <div>

    <div
      id="carouselExampleCrossfade"
      class="relative carousel slide carousel-fade"
      data-bs-ride="carousel"
    >
      <div class="absolute bottom-0 left-0 right-0 flex justify-center p-0 mb-4 carousel-indicators">
        <button
          type="button"
          data-bs-target="#carouselExampleCrossfade"
          data-bs-slide-to="0"
          class="active"
          aria-current="true"
          aria-label="Slide 1"
        ></button>
        <button
          type="button"
          data-bs-target="#carouselExampleCrossfade"
          data-bs-slide-to="1"
          aria-label="Slide 2"
        ></button>
        <button
          type="button"
          data-bs-target="#carouselExampleCrossfade"
          data-bs-slide-to="2"
          aria-label="Slide 3"
        ></button>
    </div>


    <div class="relative w-full overflow-hidden carousel-inner">
      <div class="float-left w-full carousel-item active">
        <img
          :src="`https://image.tmdb.org/t/p/w185${nowmovie.poster_path}`"
          class="block w-full"
          alt="Wild Landscape"
        />
      </div>
      
    </div>

    <button
      class="absolute top-0 bottom-0 left-0 flex items-center justify-center p-0 text-center border-0 carousel-control-prev hover:outline-none hover:no-underline focus:outline-none focus:no-underline"
      type="button"
      data-bs-target="#carouselExampleCrossfade"
      data-bs-slide="prev"
    >
      <span class="inline-block bg-no-repeat carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>

    <button
      class="absolute top-0 bottom-0 right-0 flex items-center justify-center p-0 text-center border-0 carousel-control-next hover:outline-none hover:no-underline focus:outline-none focus:no-underline"
      type="button"
      data-bs-target="#carouselExampleCrossfade"
      data-bs-slide="next"
    >
      <span class="inline-block bg-no-repeat carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
    
  </div>
  
  </div>
</template>

<script>
export default {
  name: 'NowMovive',
    props: {
    nowmovie: Object
  }
}
</script>

<style>

</style>