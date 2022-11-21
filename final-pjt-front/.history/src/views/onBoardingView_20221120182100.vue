<template>
  <div>
    <header id="header">
      <div class="header">
        <div class="header_wrapper">
          <h1 class="logo">
            <!-- 로고 -->
            <!-- <img id="logo" src="./assets/logo_white.png" alt="logo" /> -->
          </h1>

          <nav>
            <ul>
              <li>
                <div class="list">
                  <h3 class="nav_text">nav1</h3>
                  <div class="hidden_nav_list">
                    <a href="">
                      <p class="hidden_nav_list_text">nav1-1</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav1-2</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav1-3</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav1-4</p>
                    </a>
                  </div>
                </div>
              </li>
              <li>
                <div class="list">
                  <h3 class="nav_text">nav2</h3>
                  <div class="hidden_nav_list">
                    <a href="">
                      <p class="hidden_nav_list_text">nav2-1</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav2-2</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav2-3</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav2-4</p>
                    </a>
                  </div>
                </div>
              </li>
              <li>
                <div class="list">
                  <h3 class="nav_text">nav3</h3>
                  <div class="hidden_nav_list">
                    <a href="">
                      <p class="hidden_nav_list_text">nav3-1</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav3-2</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav3-3</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav3-4</p>
                    </a>
                  </div>
                </div>
              </li>
              <li>
                <div class="list">
                  <h3 class="nav_text">nav4</h3>
                  <div class="hidden_nav_list">
                    <a href="">
                      <p class="hidden_nav_list_text">nav4-1</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav4-2</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav4-3</p>
                    </a>
                    <a href="">
                      <p class="hidden_nav_list_text">nav4-4</p>
                    </a>
                  </div>
                </div>
              </li>
            </ul>
          </nav>
        </div>

        <div class="header_button_group">
          <button class="header_button_signin">Sign in</button>
          <button class="header_button_signup">Sign up</button>
        </div>
      </div>
    </header>

    <section class="section">
      <div class="section_text section_header">
        <div>
          <h2 id="section_1_title">Welcome to Movie App</h2>
        </div>
      </div>
      <div class="img">
        <img
          src="https://img.freepik.com/free-vector/cinema-film-festival-movie-poster-background_1017-33461.jpg"
          alt="section_header_img"
        />
      </div>
    </section>

    <section class="section">
      <div class="section_text">
        <div>
          <h2 id="section_2_title">Fantasy</h2>
        </div>
      </div>
      <div class="img">
        <img
          src="https://www.sll.co.kr/jtbcstudio/images/introduction/mainVisual/2022/05/447cdb68-fd27-4eb9-ae0b-6c153a6ceff9.jpg"
          alt="section1_img"
        />
      </div>
    </section>

    <section class="section">
      <div class="section_text">
        <div>
          <h2 id="section_3_title">Horror / thriller</h2>
        </div>
      </div>
      <div class="img">
        <img
          src="https://www.sll.co.kr/jtbcstudio/images/introduction/mainVisual/2022/04/a52b5eb3-b8e6-4535-9073-464c98e79543.jpg"
          alt="section2_img"
        />
      </div>
    </section>

    <section class="section">
      <div class="section_text">
        <div>
          <h2 id="section_4_title">Action</h2>
        </div>
      </div>
      <div class="img">
        <img
          src="https://www.sll.co.kr/jtbcstudio/images/introduction/mainVisual/2022/04/5861ccc7-cfd4-4ec8-b632-3730f80a563f.jpg"
          alt="section3_img"
        />
      </div>
    </section>

    <section class="section">
      <div class="section_text">
        <div>
          <h2 id="section_5_title">Romance</h2>
        </div>
      </div>
      <div class="img">
        <img
          src="https://www.sll.co.kr/jtbcstudio/images/introduction/mainVisual/2020/04/main_visual_img5.jpg"
          alt="section4_img"
        />
      </div>
    </section>

    <section class="section">
      <div class="section_text">
        <div>
          <h2 id="section_6_title">Drama</h2>
        </div>
      </div>

      <div id="section_6_btn" class="section_text more_btn">
        <div><button>더 많은 영화 보러가기</button></div>
      </div>
      <div class="img">
        <img
          src="https://www.sll.co.kr/jtbcstudio/images/introduction/mainVisual/2020/04/main_visual_img3.jpg"
          alt="section5_img"
        />
      </div>
    </section>
  </div>
</template>

<script>
const getId = (id) => {
  return document.getElementById(id);
};

const getClass = (className) => {
  return document.getElementsByClassName(className);
};

const header = getId('header');
const logo = getId('logo');
const navText = getClass('nav_text');
const hiddenNavText = getClass('hidden_nav_list_text');
const headerBtnSignin = getClass('header_button_signin');

const handleHoverHeader = () => {
  header.style.backgroundColor = '#fff';
  header.style.height = '250px';
  headerBtnSignin[0].style.color = '#000';
  logo.src = './assets/logo_black.png';
  Object.values(navText).map((text) => (text.style.color = '#000'));
  Object.values(hiddenNavText).map((text) => {
    text.style.display = 'block';
    text.style.color = '#000';
  });
};

const handleLeaveHeader = () => {
  header.style.backgroundColor = 'rgba(0,0,0,0.5)';
  header.style.height = '100px';
  headerBtnSignin[0].style.color = '#fff';
  logo.src = './assets/logo_white.png';
  Object.values(navText).map((text) => (text.style.color = '#fff'));
  Object.values(hiddenNavText).map((text) => {
    text.style.display = 'none';
    text.style.color = '#000';
  });
};

const main = () => {
  header.addEventListener('mouseover', handleHoverHeader);
  header.addEventListener('mouseleave', handleLeaveHeader);
};

main();

window.addEventListener(
  'wheel',
  function (e) {
    e.preventDefault();
  },
  { passive: false },
);

const mHtml = $('html');
let page = 1;
let scroll = true;

const lastPage = $('.section').length;

mHtml.animate({ scrollTop: 0 }, 10);

$(window).on('wheel', function (e) {
  if (mHtml.is(':animated')) return;
  console.log(page);
  $(`#section_${page}_title`).css('opacity', 1);
  $(`#section_${page}_title`).css('margin', 0);
  if (page === 6) {
    $(`#section_6_btn`).css('opacity', 1);
    $(`#section_6_btn`).css({ transform: 'translateY(0)' });
  }

  if (scroll) {
    scroll = false;
    if (e.originalEvent.deltaY > 0) {
      if (page == lastPage) return;
      page++;
    } else if (e.originalEvent.deltaY < 0) {
      if (page == 1) return;
      page--;
    }
    let posTop = (page - 1) * $(window).height();

    mHtml.animate({ scrollTop: posTop });

    setTimeout(() => {
      scroll = true;
    }, 1300);
  }
});

$(function () {
  $('#section_1_title').css('opacity', 1);
  // $('#section_1_title').css('margin', 0);
});



export default {
  name: "OnBoardingView",

  data() {
    return {};
  },

  mounted() {},

  methods: {},
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
  margin-left: 100px;
}

#section_6_btn {
  opacity: 0;
  transition: 0.5s ease-in-out;
  transform: translateY(100px);
}

#section_1_title {
  margin-left: 0;
}

html,
body {
  margin: 0;
  padding: 0;
  width: 100vw;
  height: 100%;
  background-color: black;
  color: white;
  font-family: 'Noto Sans KR', sans-serif;
}

h1,
h2,
h3,
h4,
h5,
h6,
ul,
li,
p {
  margin: 0;
  padding: 0;
}

ul {
  display: flex;
  height: 100%;
  list-style-type: none;
  color: inherit;
}

li {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 120px;
  height: 100%;
  text-align: center;
  margin-right: 80px;
}

a {
  text-decoration: none;
  color: inherit;
}

button {
  background-color: #000;
  padding: 8px 12px;
  border: 1px solid #000;
  cursor: pointer;
  border-radius: 3px;
  color: white;
  height: fit-content;
}

button:hover {
  transform: scale(1.05);
}

button:active {
  transform: scale(0.97);
}

header {
  position: fixed;
  width: 100%;
  /* height: 300px; */
  height: 100px;
  transition: 0.2s ease-in-out;
  z-index: 3;
  background-color: rgba(0, 0, 0, 0.5);
  overflow: hidden;
}

.header {
  display: flex;
  justify-content: center;
  width: 100%;
  height: 100px;
}

.header_wrapper {
  display: flex;
  justify-content: space-between;
  width: 1280px;
}

.logo {
  display: flex;
  align-items: center;
  width: 100px;
  height: 100px;
}

.logo img {
  width: 100%;
}

.header_button_group {
  display: flex;
  align-items: center;
  height: 100%;
}

.header_button_signin {
  margin-right: 15px;
  background-color: transparent;
}

.list {
  position: relative;
}

.hidden_nav_list {
  position: absolute;
  top: 60px;
  left: 0;
  width: 120px;
  text-align: left;
}

.hidden_nav_list p {
  margin-bottom: 12px;
  cursor: pointer;
}



</style>
