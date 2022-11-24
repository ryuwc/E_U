<template>
  <div id="container">
    <h1 style="margin-left: 25px;">장르별 영화</h1>
    <router-link to="/actionmovies"><div id="list">
      <div id="rank"><span><img style="width: 45px;" src="data:image/png;base64,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"></span></div>
      <div id="creator">
        <h4>액션</h4>
      </div>
    </div></router-link>
    <router-link to="/comedymovies"><div id="list">
      <div id="rank"><span><img style="width: 45px;" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAAFXklEQVRoge2YW2xUVRSGv33OTKcXWm5t0um0KgXLTUwwokWsVSRcauolhlY0hoCm8GJiND5qSHg20UQTSgwPooINYKIpJYZLhVA1GIkJiRdALi0zwJjSy0w7M51zlg+nLVM6dc45M8QY+z9Mzpy911r/v/daa+8ZmMY0/t9QuXQmL1U/g/AhkD/6KoGoPSjZCsqHmNtV26VvchkzJwKkaV4jStsFUpFh6gAwDERQ2utq/4XObGO7FiBN1Q1AKwovUACUOHdCD0q1qC8vdrjl4XFriEW+Mgt7LHtpBe5x60LLIniu6qdKmqt7ZNP89e5oOERK6mS3+pPRh6Y2qX0XjzgxcrMDd4M8wCxM+cSpkXMBuUuddAhIU3W3NM/fYNfAdhGPpw4E3DCzDYeF7WQH3KeOV4MCBw1P7O+yfQGKEfsMuE260AP1ldC80HrOMex7tK4EO/9xjlcDj2b1tscqoLJ44viqAHQFQQSGki7oToZ9AUpeS/s+TwfP6I6nI52KwAzYWGM9HzwPgwnb4aeCkz2VtG91BU0LnUdeFYAjl9KPOUhX+zUgak96Dy67annh1DUxVax04W0HvDOF8jEo8lpp4xarAlDktXxNjLXVrgsHRYxnvLnlY7LeozOrZsKUXW2/oYBtTYvSupg0PlYTfb/rdCRN4uMLapuXgx1QLSLSa5gi5lI9rZ0a/wDjzzhDu8IMtYYxLsUnjd8Jc4mmGWIaCGE01WKblm0BQLDBfxMo8wU8zKzNRy+vAS39Ggy1hpFB0wpSrFO4rTS9UzExgn/Q/0OMeDAJ0F1xOGT7eu3wLqQGAOLXktw8GCHZn30bTPYluHkoMkYeHC6qIwEibAbCY98ToUjKqAJ/PVSugbwSfGtLUMUaqljHt7YYfHOgai34n5jAMREcTA0xoJRsd8LJ0dke6AieDjb4o0AZQOx8L4VLRlOjoh4efMt6Tg6hVx6kcPEJ63vVOrjvedB9t52FTgIQu3ArNcSwv/16+10TcKdN/OoAiWuD5AWKwbTOHqPrJCPftuN7511UzasASDRCfOd7eGofx7O+EcTqmolghPjVgVTfjnPSsQAl0iJKtQJVAP0nrlDatFjUjS5F6Dv02jqMc78wvKUJvbbOEnW6E33ZcvS6pyDYCde7MBNJ6T9+OTXfuwHb3Wecj1ODMQQb/N1gXa/zKkuY01CNyvfBA29AYDVyPYjx8xlkZAR96TK0BQvh2lE49zFmPMGt9oskesZX31HnyYmA0IbyDaM7kQcUembnF5dtrLCKtfQhuLcRZo0eWH2/wpVv4K+zEOslfCBI8lZs7D+iBNBScTjk6Ldw1gJSEWzwvwh85H82VE5+GRSNCvEUWBOSwxDvhWgQYmFCX/t7lJLtTgs2HbL+heHdF11epVEPRD6PbqY5dgBi4SnnJ7vnMjNRFcNkXXRNZbDo6E9ns4nvege8+6MrTE3eR6gbe1cgw3wVbWbNyPG0NsaNmcRO3w/GhOPnlELeLjp25owbHs4FHBafPhj5AFQLaQ5CHYPN8c/YEv+UZeY5ihIxzP4CkpfLSF4uBUkb0hTF7hne3jdVx4X43RPwxUCprmsHgHq7Jv27V9t2L/C9Qr0w49iPN+za2L9KHBqY69G0Uzgg7xQKViJ09q9bOceujT0BIkpPantFkf6in0soWaQbxl6xmR22BOht0VcQbP9bljWEhujTK162MzWzgDbRQe3ImpRDKKV2yI7M/DJO8BjRJ0Hm54aWfYiwIHLq0Yz1lnkHFI05YeQCCvO5THMyChAlj+SGjnMo0R7ONMdGEat5uSDjBqIyp66dLjQ7B1zc4t+MPY1p/CfwN02kwBzu/tZqAAAAAElFTkSuQmCC"></span></div>
      <div id="creator">
        <h4>코미디</h4>
      </div>
    </div></router-link>
    <router-link to="/crimemovies"><div id="list">
      <div id="rank"><span><img style="width: 45px;" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAAE8ElEQVRoge2YXWxURRTHf2fvfhZKP7aVpuFLrKSCqKWEihGjoZSuiJhqmhrRB0LUYCQxkUQefPTBkEhiBCMhPBgSiBhCKbYhNhLASJq4NiggUExQoVhll+5Su4XuveND2XKBXe7Otoua9J80mT33P3P+Z87cOacXJjCBMUF0yLW1r3vcZX3HgYfypOdk8vLUmnB423C2E1w6q3uCfQvIn3iAeTd8ZA2tACxc5Xp69GGJKtPhawUAZlCPnwtEy4dWAC4X+Q9A6fnQy4DS252cIHkMQGnuTi5wkc8M3IsjpPkOuHXIJU0sdZdrlQ5tJP9U9RzMnq+XAQ8BTT3aEK/4dfh6t5BXPHpy9CFevDp8rQDEi6EnRx+6PkYPdN3yVWeAOeOuKD8433Ww9X6wZUBE3gBpBcx/TZYzksA+UGtShjuulLpQ0zSlki8LUo/iSaDgXipMg0HgKIpOl9fcdezAgYv2h3e9E0OhkC9qeZ5QyFKBuuKAqu9P5PcaLSmAK4N0KuhyiXSWyLVjHR0d1zLxtdSojpXq8t/wez/0xoTeGPxxFWJDEEtA/5AwcA2SJpgWDN7o6gs8YLjAbUChV1EUYOTPDxWFUFmkqCyCGSUQLAAJtWWtKyui2lk1DUM2U1z9kk7AOaP/zF4s4z155eceJ6pjACPiXceB0oYd5fwaye87Pr3EoHPtXwBRDB6R5rMX78Z3rgOGbAZKAZbM0aoxuA3Bp9WswOIHRmtlKSYfOfGdA1CyPDVc8qBeIf64pZC2t0vxGNm/aourbtmk5Zl4KTgHIKjUsG62N+sdrZ3pYelcHzPLDJoWZNfeiMDjs/WynE0r0ZkaBDzCwlnZOXi3cdLo+M2nC7LKQnWFQekkO0997TQniwy4NgKR1M/G+c4BLJvrZcGMm8etsthFyyLnLCybdwsnimFtdJrjGIC0nD6LwaPAFwAv1gZ4dXGASd47d9TvFhof9vFB05Q7nm1onEzLIn/aeQGP8EKNj7VLUkVffYlh1knzL+cc9TkR7FAdK5Uza+zQKWSan1X+e/jfB6BZZjIjEjfZ3h6lu2eIxHUrLSfgdfFYlZ/XGkqoDI6Pa83vQvSlM0fiJus/6eW7k4MZxQMkrlscOzXIhs8uEbmasSXp1ZGkF4CornTm7e1RBhKZhd+OgYTFjvZoBh8c1ZGkm4Ht6czdPUNaywD8cC7DHItPddbRO4gDgXYKh34C5tvNqWNTOyfAW6uCBKek/788EjfZsi9CuCfB4FDajB2WZ9sO60jS+yrRvMcE1gFp68HdxAMEpxisW1Wa6XESZL2OHsjhGpVQ27cgW9M9s4sPn02wZtMF1my6QLgnMWovK8qY9PcltP9HXT251YHyincQjtxu3vVN/+h4S2uESNwkEjfZ2hpNy7Ghlca2D3ORklMAsnDbMG5pRnECwLjRae4+FBsVGInfvCYvx5LAiPjdh2LY5yAcwe9fLZL+WOYlAACp39+HZT2F0FVuOzr2IOywiwcoHzlKh/H5V8gzewZy1TGmVkKe++oKPn/9rArvCbvdLjSTbXqZ+3uu+hvGIh40u9FMeL6mptLwWqdNUxVmwzdcEhfTXb03HL40Vt/j0szt7+7utYbVCgUZyustiCRNVoyHeGD8vjafudT3W/XUyp2IciPcB0y2rT8MnAc+dyvP6tZw96nx8juBCYwR/wDsMmyId+MyQAAAAABJRU5ErkJggg=="></span></div>
      <div id="creator">
        <h4>범죄 / 스릴러</h4>
      </div>
    </div></router-link>
    <router-link to="/romancemovies"><div id="list">
      <div id="rank"><span><img style="width: 45px;" src="data:image/png;base64,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"></span></div>
      <div id="creator">
        <h4>로맨스</h4>
      </div>
    </div></router-link>
    <router-link to="/animationmovies"><div id="list">
      <div id="rank"><span><img style="width: 45px;" src="data:image/png;base64,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"></span></div>
      <div id="creator">
        <h4>애니메이션</h4>
      </div>
    </div></router-link>
  </div>
</template>

<script>
export default {
  name: 'LeftBar',
  components: {},

  data() {
    return {};
  },

  mounted() {},

  methods: {},
};
</script>

<style scoped>

#container {
  position: relative;
  width: 350px;
  min-height: 500px;
  /* background: #2f363e; */
  border-radius: 30px;
  padding: 50px;
  /* box-shadow: 25px 25px 75px rgba(0, 0, 0, 0.25), 10px 10px 70px rgba(0, 0, 0, 0.25), inset 5px 5px 10px rgba(0, 0, 0, 0.5),
    inset 5px 5px 10px rgba(255, 255, 255, 0.2), inset -5px -5px 15px rgba(0, 0, 0, 0.75); */
}

#container h3 {
}

#container #list {
  position: relative;
  display: flex;
  align-items: center;
  margin: 20px 0;
  cursor: pointer;
}

#container #list #rank {
  position: relative;
  min-width: 45px;
  height: 45px;
  /* background: #fff; */
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  margin-right: 10px;
}

#container #list::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 0px;
  height: 45px;
  background: #891ff3;
  border-radius: 22.5px;
  box-shadow: 5px 5px 7px rgba(0, 0, 0, 0.25), inset 2px 2px 5px rgba(255, 255, 255, 0.25), inset -3px -3px 5px rgba(0, 0, 0, 0.5);
  transition: 0.5s;
}

#container #list:hover::before {
  width: 100%;
}

#container #list #rank::before {
  content: '';
  position: absolute;
  top: 6px;
  width: 30px;
  height: 30px;
  /* background: #2f363e; */
  border-radius: 30px;
  transform: scale(0);
  transition: 0.5s;
}

#container #list:hover #rank::before {
  transform: scale(1);
}

#container #list #rank span {

  position: relative;
  transition: 0.5s;
}

#container #list #creator {
  position: relative;
  line-height: 1.15em;
}

#container #list #creator h4 {
  color: black;
  transition: 0.5s;
  font-size: 24px;
}

#container #list #creator p {
}
</style>
