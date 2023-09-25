


// NavbarToggle

const nevLogo = document.querySelector('.NavbarLogo');
const menu = document.querySelector('#NavbarToggle');
const menuItems = document.querySelector('.NavbarMenu');
const overlay = document.querySelector('.overlay');

const mobileMenu = () => {
        menu.classList.toggle('is-active');
        menuItems.classList.toggle('active');
        overlay.classList.toggle('active');
};
const hideMobileMenu = () => {
        const activeMenuBar = document.querySelector('.is-active')
        if(window.innerWidth <= 576 && activeMenuBar){
            menu.classList.toggle('is-active');
            menuItems.classList.remove('active');
            overlay.classList.remove('active');
        };
};

menu.addEventListener('click', mobileMenu);
nevLogo.addEventListener('click', hideMobileMenu);
// menuItems.addEventListener('click', hideMobileMenu);
overlay.addEventListener('click', hideMobileMenu);


const link1 = document.querySelector('.link1');
link1.addEventListener('click', hideMobileMenu);
const link2 = document.querySelector('.link2');
link2.addEventListener('click', hideMobileMenu);
const link3 = document.querySelector('.link3');
link3.addEventListener('click', hideMobileMenu);

console.log('No Error; header is Successfully working');


