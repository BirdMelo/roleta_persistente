const itensFieldset = document.querySelector('.items-fieldset');
const template = document.querySelector('#item-form-template');
const totalForms = document.querySelector('input[name$="-TOTAL_FORMS"]');
const minimoItens = 2;

function adicionarItem() {
    const indice = Number(totalForms.value);
    const novoHtml = template.innerHTML
        .replaceAll('__prefix__', String(indice))
        .replace('__numero__', String(indice + 1));

    const wrapper = document.createElement('div');
    wrapper.innerHTML = novoHtml;

    const novoItem = wrapper.firstElementChild;
    itensFieldset.append(novoItem);
    totalForms.value = indice + 1;
    renumerarItens();

    novoItem.open = true;
    novoItem.scrollIntoView({
        behavior: 'smooth',
        block: 'center'
    });
}

function removerItem() {
    const itens = itensFieldset.querySelectorAll('.item-form');

    if (itens.length <= minimoItens) {
        return;
    }

    itens[itens.length - 1].remove();
    totalForms.value = Number(totalForms.value) - 1;
    renumerarItens();
}

function renumerarItens() {
    const itens = itensFieldset.querySelectorAll('.item-form');

    itens.forEach((item, indice) => {
        item.querySelector('summary').textContent = `Item ${indice + 1}`;
    });
}
