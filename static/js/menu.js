const menuToggle = document.getElementById('menu-toggle');
const nav = document.getElementById('mobile-nav');
const hamburgerIcon = document.getElementById('hamburger-icon');
const closeIcon = document.getElementById('close-icon');

menuToggle.addEventListener('click', () => {
    nav.classList.toggle('hidden');
    hamburgerIcon.classList.toggle('hidden');
    closeIcon.classList.toggle('hidden');
});