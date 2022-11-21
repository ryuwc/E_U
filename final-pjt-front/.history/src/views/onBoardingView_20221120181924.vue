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

<script src="http://code.jquery.com/jquery-latest.js"></script>
<script>
export default {
  name: "OnBoardingView",

  data() {
    return {};
  },

  mounted() {},

  methods: {},
};
</script>

<style scoped></style>
