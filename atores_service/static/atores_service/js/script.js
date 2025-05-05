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


async function carregarPapel(id) {
    const response_entidade = await fetch(`/api/v1/papel/${id}`)
    const entidade = await response_entidade.json()
    let papel = entidade.papel
    if (papel) {
        return papel
    }
    return "Sem atribuição"
}


/**
 * Função para exibir mensagem de feedback
 * @param {string} mensagem - Texto da mensagem
 * @param {boolean} sucesso - Indica se é uma mensagem de sucesso
 */
function exibirMensagem(mensagem, sucesso = true) {
    const elemento = document.getElementById('message');
    elemento.textContent = mensagem;
    elemento.classList.remove('d-none', 'alert-success', 'alert-danger');
    elemento.classList.add(sucesso ? 'alert-success' : 'alert-danger');

    // Remove a mensagem após 5 segundos
    setTimeout(() => {
        elemento.classList.add('d-none');
    }, 5000);
}


async function carregarPapelForm(ator) {
    const response_entidade = await fetch('/api/v1/papel')

    const entidades = await response_entidade.json()
    formEntidade = document.getElementById('papel')//TROCAR PELO ID DO FORM
    formEntidade.innerHTML = '<option value="" selected disabled>Selecione</option> '

    entidades.forEach(entidade => {
            let opcao = document.createElement('option')//criando uma nova tag <option>
            opcao.value = entidade.id
            opcao.textContent = entidade.papel
            formEntidade.appendChild(opcao) // adiciona no final o orgão

        }
    )
    formEntidade.value = ator.atores_id

}




//Função para carregar os dados do Ator
async function carregarDadosAtor(ator_id) {
    try {
        const response = await fetch(`../../../../api/v1/atores/${ ator_id }/`);

        if (!response.ok) {
            throw new Error('Erro ao carregar dados do Ator');
        }
        const ator = await response.json();

        document.getElementById("nome").textContent = ator.username
        document.getElementById("email").textContent = ator.email
        document.getElementById("orgao").textContent = await carregarOrgao(ator.orgao_id)
        document.getElementById("telefone").textContent = ator.telefone
        document.getElementById("papel").textContent = await carregarPapel(ator.atores_id)

        await carregarPapelForm(ator)

    } catch (error) {
        console.error('Erro: ', error);
        exibirMensagem('Erro ao carregar os dados do Ator', false);
    }
}




