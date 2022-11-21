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

console.log(header);

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
