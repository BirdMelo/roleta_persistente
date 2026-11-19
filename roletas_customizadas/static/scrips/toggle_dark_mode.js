const btn = document.getElementById('btn-dark-mode');
const html = document.documentElement;
const img = btn.querySelector('img');

const temaUsuario = html.dataset.theme;
const temaArmazenado = localStorage.getItem('theme');

if (html.dataset.authenticated === 'true') {
    localStorage.setItem('theme', temaUsuario);
} else if (temaArmazenado === 'dark' || temaArmazenado === 'light') {
    html.dataset.theme = temaArmazenado;
}

function atualizarIcone() {
    if (html.dataset.theme === 'dark') {
        img.src = img.dataset.light;
        img.alt = 'modo claro';
    } else {
        img.src = img.dataset.dark;
        img.alt = 'modo escuro';
    }
}

function obterCookie(nome) {
    const cookie = document.cookie
        .split('; ')
        .find((item) => item.startsWith(`${nome}=`));

    return cookie ? decodeURIComponent(cookie.split('=')[1]) : '';
}

atualizarIcone();

btn.addEventListener('click', () => {
    const novoTema = html.dataset.theme === 'dark' ? 'light' : 'dark';

    html.dataset.theme = novoTema;
    localStorage.setItem('theme', novoTema);
    atualizarIcone();

    if (html.dataset.authenticated === 'true') {
        fetch('/accounts/tema/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': obterCookie('csrftoken'),
            },
            body: JSON.stringify({
                dark_mode: novoTema === 'dark',
            }),
        });
    }
});