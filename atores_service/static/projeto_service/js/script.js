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