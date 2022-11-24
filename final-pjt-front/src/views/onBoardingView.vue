<template>
  <!-- <div></div> -->
  <body>
    <section class="section">
      <div class="section_text section_header">
        <div>
          <h2 id="section_1_title">Welcome to Movie App</h2>
        </div>
      </div>
      <div class="img">
        <!-- <img src="https://images.unsplash.com/photo-1570483358100-6d222cdea6ff?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1965&q=80" alt="section_header_img" /> -->
        <!-- <img src="https://images.unsplash.com/photo-1514454529242-9e4677563e7b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="section_header_img" /> -->
        <!-- <img src="https://images.unsplash.com/photo-1597571063304-81f081944ee8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=736&q=80" alt="section_header_img" /> -->
        <img src="https://images.unsplash.com/photo-1533090161767-e6ffed986c88?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80" alt="section_header_img" />
        <!-- <img src="https://images.unsplash.com/photo-1570483358100-6d222cdea6ff?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1965&q=80" alt="section_header_img" /> -->
      </div>
    </section>

    <section class="section">
      <div class="section_text">
        <div>
          <h2 style="font-size: 100px;" id="section_2_title">액션</h2>
        </div>
      </div>
      <div class="img">
        <img src="https://www.themoviedb.org/t/p/original/vIPIyTJqcgOKgKcExCvTDpLpTYW.jpg" alt="section1_img" />
      </div>
    </section>

    <section class="section">
      <div class="section_text">
        <div>
          <h2 style="font-size: 100px;" id="section_3_title">범죄 / 스릴러</h2>
        </div>
      </div>
      <div class="img">
        <img src="https://www.themoviedb.org/t/p/original/v8P3MuHo46tDtbfwqkGz3ajtqxe.jpg" alt="section2_img" />
      </div>
    </section>

    <section class="section">
      <div class="section_text">
        <div>
          <h2 style="font-size: 100px;" id="section_4_title">애니메이션</h2>
        </div>
      </div>
      <div class="img">
        <img src="https://www.themoviedb.org/t/p/original/zNugnnR5KEmq9EzLcl0Me1UmHYk.jpg" alt="section3_img" />
      </div>
    </section>

    <section class="section">
      <div class="section_text">
        <div>
          <h2 style="font-size: 100px;" id="section_5_title">로맨스</h2>
        </div>
      </div>
      <div class="img">
        <img src="https://www.themoviedb.org/t/p/original/xGzoTqbOlCR4mAzeRs4PB53i8c7.jpg" alt="section4_img" />
      </div>
    </section>

    <section class="section">
      <div class="section_text">
        <div>
          <h2 id="section_6_title">코메디</h2>
        </div>
      </div>
      <a href="/home"><div id="section_6_btn" class="section_text more_btn">
        <div><button>Let's Go!</button></div>
      </div></a>
      <div class="img">
        <img src="https://www.themoviedb.org/t/p/original/4zsJyxF2UGSgvs53ikysuexjlpU.jpg" alt="section5_img" />
      </div>
    </section>
  </body>
</template>

<script>
// const lastPage = 6;

export default {
  name: 'OnBoardingView',

  data() {
    return {
      page: 1,
      scroll: true,
      positionTop: 0,
    };
  },
  computed: {
    section() {
      return document.getElementById(`section_${this.page}_title`);
    },
  },
  methods: {
    fullPageScroll() {
      const html = document.querySelector('html');
      const wheelEvent = 'onwheel' in document.createElement('div') ? 'wheel' : 'mousewheel';

      html.scrollTo({ top: this.positionTop, behavior: 'smooth' });
      if (this.page === 1) {
        this.section.style.opacity = 1;
        this.section.style.margin = 0;
      }

      const lastPage = 6;

      window.addEventListener(
        wheelEvent,
        (e) => {
          e.preventDefault();

          if (Math.floor(html.scrollTop) === this.positionTop && scroll) {
            this.scroll = false;

            let delta = e.deltaY;

            if (delta > 0) {
              if (this.page == lastPage) return;
              this.page++;
            } else if (delta < 0) {
              if (this.page == 1) return;
              this.page--;
            }

            this.positionTop = (this.page - 1) * window.innerHeight;
            html.scrollTo({ top: this.positionTop, behavior: 'smooth' });
            const sec = document.getElementById(`section_${this.page}_title`);
            sec.style.opacity = 1;
            sec.style.margin = 0;
            if (this.page === 6) {
              const btn = document.getElementById('section_6_btn');
              btn.style.opacity = 1;
              btn.style.transform = 'translateY(0)';
            }
            setTimeout(() => {
              this.scroll = true;
            }, 1500);
          }
        },
        { passive: false },
      );
    },
  },
  mounted() {
    // console.log(this.section);
    // console.log(this.test);
    this.fullPageScroll();
  },
  beforeUpdate() {},
};
</script>

<style scoped>
.section {
  position: relative;
  width: 100vw;
  height: 100vh;
  transition: all 700ms ease 0s;
}

.section_text {
  position: absolute;
  display: flex;
  justify-content: center;
  width: 100vw;
  z-index: 2;
  top: 150px;
}

.section_header {
  top: 200px;
}

.section_text div {
  width: 1280px;
}

.section_text h2 {
  font-size: 64px;
  text-shadow: 2px 2px 2px #000;
}

.img {
  position: absolute;
  width: 100%;
  height: 100vh;
}

.img img {
  width: 100%;
  height: 100vh;
}

.more_btn {
  top: unset;
  bottom: 100px;
}

.more_btn button {
  width: 200px;
  height: 40px;
  background-color: #eee;
  border: 1px solid #000;
  color: #000;
  border: none;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
}

#section_1_title,
#section_2_title,
#section_3_title,
#section_4_title,
#section_5_title,
#section_6_title {
  opacity: 0;
  transition: 0.5s ease-in-out;
  transition-delay: 0.5s;
  margin-left: 100px;
}

#section_6_btn {
  opacity: 0;
  transition: 0.5s ease-in-out;
  transition-delay: 0.5s;
  transform: translateY(100px);
}

#section_1_title {
  margin-left: 0;
}
</style>
