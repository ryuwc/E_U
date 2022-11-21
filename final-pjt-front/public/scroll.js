const html = document.querySelector('html');

let page = 1;
let scroll = true;
let currentPage = 0;
let lastY = 0;
let windowHeight = 0;

const section = document.getElementById(`section_${page}_title`);

const lastPage = 6;
let positionTop = 0;

const fullPageScroll = () => {
  const wheelEvent = 'onwheel' in document.createElement('div') ? 'wheel' : 'mousewheel';

  html.scrollTo({ top: positionTop, behavior: 'smooth' });
  if (page === 1) {
    section.style.opacity = 1;
    section.style.margin = 0;
  }

  window.addEventListener(
    wheelEvent,
    (e) => {
      e.preventDefault();

      if (Math.floor(html.scrollTop) === positionTop && scroll) {
        scroll = false;

        let delta = e.deltaY;

        if (delta > 0) {
          if (page == lastPage) return;
          page++;
        } else if (delta < 0) {
          if (page == 1) return;
          page--;
        }

        positionTop = (page - 1) * window.innerHeight;
        html.scrollTo({ top: positionTop, behavior: 'smooth' });
        const sec = document.getElementById(`section_${page}_title`);
        sec.style.opacity = 1;
        sec.style.margin = 0;
        if (page === 6) {
          const btn = document.getElementById('section_6_btn');
          btn.style.opacity = 1;
          btn.style.transform = 'translateY(0)';
        }
        setTimeout(() => {
          scroll = true;
        }, 1500);
      }
    },
    { passive: false },
  );
};

fullPageScroll();
