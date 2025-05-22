function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();

            // Verifica se o cookie começa com o nome que queremos
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

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


async function carregarProjetos(user_id = null) {
    token = localStorage.getItem('token');
    let url;
    if (user_id !== null) {
        url = `/api/v1/projetos/?user_id=${user_id}`;
    } else {
        url = '/api/v1/projetos';
    }

    const response = await fetch(url, {
        headers: {
            'Authorization': `Token ${token}`,  // envia o token no header Authorization
        },
        credentials: 'include' // se você também usa sessão + CSRF
    });

    if (!response.ok) {
        console.error('Erro ao carregar projetos:', response.statusText);
        return;
    }

    const projetos = await response.json();

    let listaProjetos = document.getElementById("listaProjetos")

    // Algo como "Para cada projeto em projetos, execute... é uma arrow function, é interessante aprender
    projetos.forEach(projeto => {
        let item = document.createElement('div')
        item.classList.add('col-6', 'col')
        item.innerHTML = ` <div class=" card p-2 rounded-2 hover-grow" style="min-height: 11.1rem">
                                <a href="../ver-projeto/${projeto.id}/" class="text-decoration-none" ><h5 class="card-header mb-2">${projeto.nome}</h5></a>
                                <p class="card-subtitle mb-2">${projeto.descricao}</p>
                                <div class="row my-2">
                                    <div class="col d-flex justify-content-evenly align-items-center">
                                        <a href="../editar-projeto/${projeto.id}/" class="text-decoration-none"><button class="btn btn-primary"> <i class="bi bi-pencil-fill"></i> Editar</button></a>
                                        <button class="btn btn-danger" onclick="deletarItemPorID(${projeto.id})"> <i class="bi bi-x"></i>  Excluir</button>
                                    </div>
                                    <div class="col align-items-center">
                                        <p class="card-text text-center" > Data inicial: ${projeto.data_inicio} </p> <p class="card-text text-center"> Data final: ${projeto.data_final}</p>
                                    </div>
                                </div>
                            </div>
                          `
        listaProjetos.appendChild(item)
    })
}


async function deletarItemPorID(id) {
    const response = await fetch(`/api/v1/projetos/${id}/`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')  // Se necessário
        }
    });

    if (response.ok) {
        exibirMensagem("Projeto deletado com sucesso!", true)

        setTimeout(() => {
            window.location.reload();
        }, 1500);
        // Atualize a lista ou redirecione
    } else {
        exibirMensagem("Erro ao deletar o projeto!", false)
    }
}

