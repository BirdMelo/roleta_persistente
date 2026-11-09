const btn = document.getElementById('btn-dark-mode');
const html = document.documentElement;
const img = btn.querySelector('img');
btn.addEventListener('click', () => {
    if(html.dataset.theme === 'dark') {
        html.dataset.theme = 'light';
        img.src = img.dataset.dark;
        img.alt = 'dark mode'
    } else {
        html.dataset.theme = 'dark';
        img.src = img.dataset.light;
        img.alt = 'light mode'
    }
    
})