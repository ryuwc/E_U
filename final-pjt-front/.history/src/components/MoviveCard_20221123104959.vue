<template>
  
  <!-- 추천 영화 페이지 라인에서 가로 스크로 적용 할 테그 -->
  <div style="height: 500px; width: 500px;" class="col-2">
  <!-- normal -->
    <div class="card-item effect11 left_to_right">
      <a href="#">
        <div class="img w-100">
          <img 
          :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" 
          alt="img">
        </div>
        <div class="info">
            <h3>{{ movie.title }}</h3>
            <p>출연: {{ }}</p>
            <p>감독: {{  }}</p>
        </div>
      </a>
    </div>
  </div>

</template>

<script>
export default {
  name: "MovieCard",
  props: {
    movie: Object,
  },
  methods: {
    goToDetail(id) {
      this.$router.push({ name: "MovieDetailInfoView", params: { id: id } });
    },
  }
};
</script>

<style>

@charset "UTF-8";
.row {
    display: flex;
    flex-direction: row;

}
.card-item {
    position: relative;
    -webkit-transition: all 0.35s ease-in-out;
    -moz-transition: all 0.35s ease-in-out;
    transition: all 0.35s ease-in-out;
  }
  .card-item img {
    width: 500px;
    height: 500px;
  }
  
  .card-item{
    position: relative;
    width: 220px;
    height: 220px;
    border-radius: 50%;
  }
  .card-item .img {
    position: relative;
    width: 220px;
    height: 220px;
    border-radius: 50%;
  }
  .card-item .img:before {
    position: absolute;
    display: block;
    content: '';
    width: 100%;
    height: 100%;
    /* box-shadow: inset 0 0 0 16px rgba(255, 255, 255, 0.6), 0 1px 2px rgba(0, 0, 0, 0.3); */
    -webkit-transition: all 0.35s ease-in-out;
    -moz-transition: all 0.35s ease-in-out;
    transition: all 0.35s ease-in-out;
  }
  .card-item .info {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    text-align: center;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
  }
.effect11 {
    -webkit-perspective: 900px;
    -moz-perspective: 900px;
    perspective: 900px;
  }
.effect11 .img {
    opacity: 1;
    -webkit-transform-origin: 50% 50%;
    -moz-transform-origin: 50% 50%;
    -ms-transform-origin: 50% 50%;
    -o-transform-origin: 50% 50%;
    transform-origin: 50% 50%;
    -webkit-transition: all 0.35s ease-in-out;
    -moz-transition: all 0.35s ease-in-out;
    transition: all 0.35s ease-in-out;
  }
.effect11.colored .info {
    background: #1a4a72;
  }
.effect11 .info {
    background: #333333;
    opacity: 0;
    visibility: hidden;
    -webkit-transition: all 0.35s ease 0.35s;
    -moz-transition: all 0.35s ease 0.35s;
    transition: all 0.35s ease 0.35s;
  }
.effect11 .info h3 {
    color: #fff;
    text-transform: uppercase;
    position: relative;
    letter-spacing: 2px;
    font-size: 22px;
    margin: 0 30px;
    padding: 55px 0 0 0;
    height: 110px;
    text-shadow: 0 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.3);
  }
.effect11 .info p {
    color: #bbb;
    padding: 10px 5px;
    font-style: italic;
    margin: 0 30px;
    font-size: 12px;
    border-top: 1px solid rgba(255, 255, 255, 0.5);
  }
.effect11 a:hover .img {
    opacity: 0;
  }
.effect11 a:hover .info {
    visibility: visible;
    opacity: 1;
  }
  
.effect11.left_to_right .img {
    -webkit-transform: translateZ(0) rotateY(0);
    -moz-transform: translateZ(0) rotateY(0);
    -ms-transform: translateZ(0) rotateY(0);
    -o-transform: translateZ(0) rotateY(0);
    transform: translateZ(0) rotateY(0);
  }
.effect11.left_to_right .info {
    -webkit-transform: translateZ(-1000px) rotateY(-90deg);
    -moz-transform: translateZ(-1000px) rotateY(-90deg);
    -ms-transform: translateZ(-1000px) rotateY(-90deg);
    -o-transform: translateZ(-1000px) rotateY(-90deg);
    transform: translateZ(-1000px) rotateY(-90deg);
  }
.effect11.left_to_right a:hover .img {
    -webkit-transform: translateZ(-1000px) rotateY(90deg);
    -moz-transform: translateZ(-1000px) rotateY(90deg);
    -ms-transform: translateZ(-1000px) rotateY(90deg);
    -o-transform: translateZ(-1000px) rotateY(90deg);
    transform: translateZ(-1000px) rotateY(90deg);
  }
.effect11.left_to_right a:hover .info {
    -webkit-transform: translateZ(0) rotateY(0);
    -moz-transform: translateZ(0) rotateY(0);
    -ms-transform: translateZ(0) rotateY(0);
    -o-transform: translateZ(0) rotateY(0);
    transform: translateZ(0) rotateY(0);
  }
  
.effect11.right_to_left .img {
    -webkit-transform: translateZ(0) rotateY(0);
    -moz-transform: translateZ(0) rotateY(0);
    -ms-transform: translateZ(0) rotateY(0);
    -o-transform: translateZ(0) rotateY(0);
    transform: translateZ(0) rotateY(0);
  }
.effect11.right_to_left .info {
    -webkit-transform: translateZ(-1000px) rotateY(90deg);
    -moz-transform: translateZ(-1000px) rotateY(90deg);
    -ms-transform: translateZ(-1000px) rotateY(90deg);
    -o-transform: translateZ(-1000px) rotateY(90deg);
    transform: translateZ(-1000px) rotateY(90deg);
  }
.effect11.right_to_left a:hover .img {
    -webkit-transform: translateZ(-1000px) rotateY(-90deg);
    -moz-transform: translateZ(-1000px) rotateY(-90deg);
    -ms-transform: translateZ(-1000px) rotateY(-90deg);
    -o-transform: translateZ(-1000px) rotateY(-90deg);
    transform: translateZ(-1000px) rotateY(-90deg);
  }
.effect11.right_to_left a:hover .info {
    -webkit-transform: translateZ(0) rotateY(0);
    -moz-transform: translateZ(0) rotateY(0);
    -ms-transform: translateZ(0) rotateY(0);
    -o-transform: translateZ(0) rotateY(0);
    transform: translateZ(0) rotateY(0);
  }
  
.effect11.top_to_bottom .img {
    -webkit-transform: translateZ(0) rotateX(0);
    -moz-transform: translateZ(0) rotateX(0);
    -ms-transform: translateZ(0) rotateX(0);
    -o-transform: translateZ(0) rotateX(0);
    transform: translateZ(0) rotateX(0);
  }
.effect11.top_to_bottom .info {
    -webkit-transform: translateZ(-1000px) rotateX(90deg);
    -moz-transform: translateZ(-1000px) rotateX(90deg);
    -ms-transform: translateZ(-1000px) rotateX(90deg);
    -o-transform: translateZ(-1000px) rotateX(90deg);
    transform: translateZ(-1000px) rotateX(90deg);
  }
.effect11.top_to_bottom a:hover .img {
    -webkit-transform: translateZ(-1000px) rotateX(-90deg);
    -moz-transform: translateZ(-1000px) rotateX(-90deg);
    -ms-transform: translateZ(-1000px) rotateX(-90deg);
    -o-transform: translateZ(-1000px) rotateX(-90deg);
    transform: translateZ(-1000px) rotateX(-90deg);
  }
.effect11.top_to_bottom a:hover .info {
    -webkit-transform: translateZ(0) rotateX(0);
    -moz-transform: translateZ(0) rotateX(0);
    -ms-transform: translateZ(0) rotateX(0);
    -o-transform: translateZ(0) rotateX(0);
    transform: translateZ(0) rotateX(0);
  }
  
.effect11.bottom_to_top .img {
    -webkit-transform: translateZ(0) rotateX(0);
    -moz-transform: translateZ(0) rotateX(0);
    -ms-transform: translateZ(0) rotateX(0);
    -o-transform: translateZ(0) rotateX(0);
    transform: translateZ(0) rotateX(0);
  }
.effect11.bottom_to_top .info {
    -webkit-transform: translateZ(-1000px) rotateX(-90deg);
    -moz-transform: translateZ(-1000px) rotateX(-90deg);
    -ms-transform: translateZ(-1000px) rotateX(-90deg);
    -o-transform: translateZ(-1000px) rotateX(-90deg);
    transform: translateZ(-1000px) rotateX(-90deg);
  }
.effect11.bottom_to_top a:hover .img {
    -webkit-transform: translateZ(-1000px) rotateX(90deg);
    -moz-transform: translateZ(-1000px) rotateX(90deg);
    -ms-transform: translateZ(-1000px) rotateX(90deg);
    -o-transform: translateZ(-1000px) rotateX(90deg);
    transform: translateZ(-1000px) rotateX(90deg);
  }
.effect11.bottom_to_top a:hover .info {
    -webkit-transform: translateZ(0) rotateX(0);
    -moz-transform: translateZ(0) rotateX(0);
    -ms-transform: translateZ(0) rotateX(0);
    -o-transform: translateZ(0) rotateX(0);
    transform: translateZ(0) rotateX(0);
  }
</style>
