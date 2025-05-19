/**
 * Busca a sigla de um órgão a partir do seu ID.
 *
 * A função faz uma requisição assíncrona à API de órgãos utilizando o ID fornecido
 * e retorna a sigla correspondente ao órgão.
 *
 * @param {number} id - O ID do órgão a ser buscado.
 * @returns {Promise<string>} - Uma Promise que resolve com a sigla do órgão.
 */
async function carregarOrgao(id) {
    const response_entidade = await fetch(`/api/v1/orgaos/${id}`)
    const entidade = await response_entidade.json()
    let sigla = entidade.sigla
    if (sigla) {
        return sigla
    }
    return "Sem atribuição"
}


async function carregarDesenvolvedorForm() {
    const response_entidade = await fetch('/api/v1/atores')

    const entidades = await response_entidade.json()
    formEntidade = document.getElementById('selectUsuario')//TROCAR PELO ID DO FORM
    formEntidade.innerHTML = '<option value="" selected disabled>Selecione</option> '

    entidades.forEach(entidade => {
        let opcao = document.createElement('option')//criando uma nova tag <option>
        opcao.value = entidade.id
        opcao.textContent = entidade.username
        formEntidade.appendChild(opcao) // adiciona no final o orgão
    })
}



function esperar(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


function carregamento() {
const barra = document.getElementById('barraProgresso');
const preloader = document.getElementById('preloader');

// Faz a barra preencher de forma suave
barra.style.transition = 'width 300ms ease-in-out';
barra.style.width = '100%';

// Esconde o preloader após 300ms
setTimeout(() => {
    preloader.style.transition = 'opacity 300ms ease';
    preloader.style.opacity = 0;
    setTimeout(() => {
        preloader.style.display = 'none';
        preloader.style.position = 'relative'
    }, 300); // tempo para a transição de opacidade
}, 300);
}

function parseDateBr(dateStr) {
    if (!dateStr) return new Date(0); // Caso data seja null/undefined
    const [dia, mes, ano] = dateStr.split('/');
    return new Date(`${ano}-${mes}-${dia}`);
}