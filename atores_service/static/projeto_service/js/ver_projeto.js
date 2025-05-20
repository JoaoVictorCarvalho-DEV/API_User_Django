let tarefas;

// Função de ordenação
function ordenarTarefas(tipo) {
    const parseDateBr = (dateStr) => {
        if (!dateStr) return new Date(0); // Se data_final/data_inicio for null/undefined
        const [dia, mes, ano] = dateStr.split('/');
        return new Date(`${ano}-${mes}-${dia}`);
    };

    let tarefasOrdenadas = [...tarefas];

    switch (tipo) {
        case "mais_recente":
            tarefasOrdenadas.sort((a, b) => parseDateBr(b.data_inicio) - parseDateBr(a.data_inicio));
            break;
        case "mais_antiga":
            tarefasOrdenadas.sort((a, b) => parseDateBr(a.data_inicio) - parseDateBr(b.data_inicio));
            break;
        case "expiracao_proxima":
            tarefasOrdenadas.sort((a, b) => parseDateBr(a.data_final) - parseDateBr(b.data_final));
            break;
        case "expiracao_distante":
            tarefasOrdenadas.sort((a, b) => parseDateBr(b.data_final) - parseDateBr(a.data_final));
            break;
        default:
            console.warn("Tipo de ordenação desconhecido:", tipo);
    }
    return tarefasOrdenadas;
}


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


/**
 * Busca a sigla de um órgão a partir do seu ID.
 *
 * A função faz uma requisição assíncrona à API de órgãos utilizando o ID fornecido
 * e retorna a sigla correspondente ao órgão.
 *
 * @returns {Promise<string>} - Uma Promise que resolve com a sigla do órgão.
 * @param tarefas
 */
async function carregarTarefasProjeto(tarefas) {
    document.querySelectorAll('.status-section').forEach(task => {
        task.innerHTML = ''
    })

    esperar(500).then(async () => {
        tarefas.forEach(tarefa => {
                const card = document.createElement("div");
                card.innerHTML = `
                <a href="/site/tarefas/editar-tarefa/${tarefa.id}/" data-task-id="${tarefa.id}" draggable="true" class="card tarefa shadow-sm hover-grow text-decoration-none text-dark mb-2 ">
                    <div class="card-body">
                        <h6 class="card-title fw-bold">${tarefa.nome}</h6>
                        <p class="card-text text-muted mb-2">
                            ${tarefa.descricao || "Sem descrição"}
                        </p>
                        <div class="d-flex justify-content-between text-muted small">
                            <span class="d-flex align-items-center">
                                <i class="bi bi-play-circle me-1"></i>
                                Início: ${formatarData(tarefa.data_inicio)}
                            </span>
                            <span class="d-flex align-items-center">
                                <i class="bi bi-flag-fill me-1"></i>
                                Entrega: ${formatarData(tarefa.data_final)}
                            </span>
                        </div>
                    </div>
                </a>
            `;

                if (tarefa.status === "Concluída") {
                    document.getElementById("Concluída").appendChild(card);

                } else if (tarefa.status === "Cancelada") {
                    document.getElementById("Cancelada").appendChild(card);
                } else {
                    document.getElementById("Em andamento").appendChild(card);
                }
            }
        );
    })
}

/**
 * Preenche a tabela de tarefas de um projeto na interface HTML.
 *
 * Para cada tarefa recebida, cria uma linha (<tr>) com as seguintes informações:
 * nome, descrição, status fixo ("Em andamento"), data de início, data final e responsável.
 * Cada linha é adicionada na tabela com id 'listaTarefas'.
 *
 * @param {Array} tarefas - Lista de objetos de tarefas, onde cada tarefa deve conter:
 *  - nome {string}
 *  - descricao {string}
 *  - data_inicio {string}
 *  - data_final {string}
 *  - responsavel_id {number}
 *
 * @returns {void}
 */

async function carregarProjeto(projeto_id) {
    const response = await fetch(`../../../../api/v1/projetos/${projeto_id}`, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,  // envia o token no header Authorization
        }
    })//Nesse caso passamos o id do projeto, por conta do router, ele vai fazer um get naquele projeto.
    const projeto = await response.json()
    esperar(300).then(async () => {
        //Aqui passamos o id do input no form e falo que o valor dele é o nome/descricao/data... do projeto
        document.getElementById("nome").textContent = projeto.nome
        document.getElementById("descricao").textContent = projeto.descricao
        document.getElementById("dataInicio").innerHTML = `<strong>Data de Início:</strong> ${projeto.data_inicio}`
        document.getElementById("dataFinal").innerHTML = `<strong>Data de Início:</strong> ${projeto.data_final}`

        document.getElementById("desenvolvedor").innerHTML = "<strong>Desenvolvedor: </strong>" + (await carregarResponsavel(projeto.desenvolvedor_id))
        document.getElementById("analista").innerHTML = "<strong>Analista: </strong>" + (await carregarResponsavel(projeto.analista_id))
        document.getElementById("orgao").innerHTML = "<strong>Órgão: </strong>" + (await carregarOrgao(projeto.orgao_id))
        document.getElementById("status").innerHTML = "<strong>Status:</strong> " + projeto.status

        tarefas = projeto.tarefas

        await carregarTarefasProjeto(ordenarTarefas("mais_recente"))

    })

}


const form = document.getElementById('chatForm');
const formData = new FormData(form);

document.getElementById('chatForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const msg = document.getElementById('mensagemInput').value;
    if (!msg) return;

    const response = await fetch(`../../../../api/v1/projetos/{{ projeto_id }}/mensagens/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,  // envia o token no header Authorization
        },
        credentials: 'include',
        body: JSON.stringify({conteudo: msg, user_id: usuario.id})
    });
    document.getElementById('mensagemInput').value = '';
    await carregarMensagens(); // Recarrega as mensagens

    if (response.status === 403) {
        const data = await response.json();
        exibirMensagem(data.detail)
    } else {
        exibirMensagem('Mensagem enviada');
    }
});


async function carregarMensagens(projeto_id) {
    const res = await fetch(`../../../../api/v1/projetos/${projeto_id}/mensagens/`,
        {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`,  // envia o token no header Authorization
            }
        }
    );
    const mensagens = await res.json();

    const chatBox = document.getElementById('chatBox');
    chatBox.innerHTML = '';
    for (const msg of mensagens) {
        var autor = await carregarResponsavel(msg.user_id)
        const p = document.createElement('p');
        p.innerHTML = `<strong> ${autor}:</strong> ${msg.conteudo}`;
        chatBox.appendChild(p);
    }

    chatBox.scrollTop = chatBox.scrollHeight; // Scroll automático
}

/**
 * Busca o nome de usuário (username) de um responsável pelo seu ID.
 *
 * A função faz uma requisição assíncrona à API de atores, utilizando o ID fornecido,
 * e retorna o nome de usuário (username) associado ao responsável.
 *
 * @param {number} id - O ID do responsável a ser buscado.
 * @returns {Promise<string>} - Uma Promise que resolve com o nome de usuário do responsável.
 */
async function carregarResponsavel(id) {
    const response_entidade = await fetch(`/api/v1/atores/${id}`)
    const entidade = await response_entidade.json()
    let nome = entidade.username

    if (nome) {
        return nome
    }
    return "Sem atribuição"
}

function mostrarFormulario() {
    const form = document.getElementById("formulario-membro");
    form.style.display = form.style.display === "none" ? "block" : "none";
}

async function adicionarMembro(projetoId) {
    const userId = document.getElementById("selectUsuario").value;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const response = await fetch(`/api/v1/projetos/${projetoId}/adicionar_membro/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
            'Authorization': `Token ${token}`
        },
        body: JSON.stringify({user_id: userId}),
        credentials: 'include'
    });

    const mensagem = document.getElementById("mensagem-resposta");

    if (response.ok) {
        mensagem.innerText = "Membro adicionado com sucesso!";
        mensagem.style.color = "green";
    } else {
        const erro = await response.json();
        mensagem.innerText = erro.detail || "Erro ao adicionar membro.";
        mensagem.style.color = "red";
    }
}


// Detecta mudanças no select
document.getElementById("ordenarTarefas").addEventListener("change", async function () {
    var tipo = document.getElementById('ordenarTarefas').value
    await carregarTarefasProjeto(ordenarTarefas(tipo));
});

function formatarData(dataStr) {
    if (!dataStr) return "Sem data";
    const [dia, mes, ano] = dataStr.split('/');
    const meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"];
    return `${dia} de ${meses[parseInt(mes) - 1]} de ${ano}`;
}