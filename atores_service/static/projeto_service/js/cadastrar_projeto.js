async function carregarOrgaoForm(){
    const response_orgaos = await fetch('/api/v1/orgaos')
    const orgaos = await response_orgaos.json()

    formOrgao = document.getElementById('orgaoId')
    formOrgao.innerHTML = '<option value="" selected disabled>Selecione</option> '

    orgaos.forEach(orgao => {
        let opcao = document.createElement('option')//criando uma nova tag <option>
        opcao.value = orgao.id
        opcao.textContent = orgao.sigla
        formOrgao.appendChild(opcao) // adiciona no final o orgão
    })
    }

    async function carregarAnalistaForm(){
        const response_entidade = await fetch('/api/v1/atores')

        const entidades = await response_entidade.json()
        formEntidade = document.getElementById('analista')//TROCAR PELO ID DO FORM
        formEntidade.innerHTML = '<option value="" selected disabled>Selecione</option> '

        entidades.forEach(entidade => {
            let opcao = document.createElement('option')//criando uma nova tag <option>
            opcao.value = entidade.id
            opcao.textContent = entidade.username
            formEntidade.appendChild(opcao) // adiciona no final o orgão
        })
    }


    async function carregarDesenvolvedorForm(){
        const response_entidade = await fetch('/api/v1/atores')

        const entidades = await response_entidade.json()
        formEntidade = document.getElementById('desenvolvedor')//TROCAR PELO ID DO FORM
        formEntidade.innerHTML = '<option value="" selected disabled>Selecione</option> '

        entidades.forEach(entidade => {
            let opcao = document.createElement('option')//criando uma nova tag <option>
            opcao.value = entidade.id
            opcao.textContent = entidade.username
            formEntidade.appendChild(opcao) // adiciona no final o orgão
        })
    }


    // Contador de caracteres para o nome do projeto
    document.getElementById('inputName').addEventListener('input', function() {
        const counter = document.getElementById('nomeCounter');
        const currentLength = this.value.length;
        counter.textContent = currentLength;

        // Altera a cor se aproximar do limite
        if (currentLength > 45) {
            counter.classList.add('text-warning');
            if (currentLength >= 50) {
                counter.classList.remove('text-warning');
                counter.classList.add('text-danger');
            }
        } else {
            counter.classList.remove('text-warning', 'text-danger');
        }
    });

    // Validação do tamanho do nome antes do envio
    document.getElementById('formProjeto').addEventListener('submit', function(event) {
        const nomeProjeto = document.getElementById('inputName').value;

        if (nomeProjeto.length > 50) {
            event.preventDefault();
            const input = document.getElementById('inputName');
            input.classList.add('is-invalid');

            exibirMensagem('O nome do projeto não pode exceder 50 caracteres.', false);
            return;
        }

        // Restante da lógica de submit permanece igual...
    });

    /**
     * Função para formatar a data de YYYY-MM-DD para DD/MM/YYYY
     * @param {string} data - Data no formato YYYY-MM-DD
     * @returns {string} Data formatada ou string vazia se inválida
     */
    function formatarData(data) {
        if (!data) return "";
        const partes = data.split("-");
        if (partes.length !== 3) return data; // Retorna original se formato inválido
        return `${partes[2]}/${partes[1]}/${partes[0]}`;
    }

    /**
     * Função para validar se a data final é maior que a data inicial
     * @param {string} inicio - Data inicial no formato YYYY-MM-DD
     * @param {string} fim - Data final no formato YYYY-MM-DD
     * @returns {boolean} Verdadeiro se a data final é válida
     */
    function validarDatas(inicio, fim) {
        if (!inicio || !fim) return true; // Validação básica já feita pelo required
        return new Date(fim) >= new Date(inicio);
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

    // Evento de submissão do formulário
    document.getElementById('formProjeto').addEventListener('submit', async function(event) {
        event.preventDefault();

        // Validação do formulário
        const form = this;
        if (!form.checkValidity()) {
            event.stopPropagation();
            form.classList.add('was-validated');
            return;
        }

        // Validação das datas
        const dataInicio = document.getElementById('dataInicio').value;
        const dataFinal = document.getElementById('dataFinal').value;

        if (!validarDatas(dataInicio, dataFinal)) {
            exibirMensagem('A data final deve ser maior ou igual à data inicial.', false);
            return;
        }

        // Preparação dos dados
        const formData = new FormData(form);

        try {
            // Envio dos dados para a API
            const response = await fetch('/api/v1/projetos/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    nome: formData.get('inputName'),
                    descricao: formData.get('descricao'),
                    data_inicio: formatarData(dataInicio),
                    data_final: formatarData(dataFinal),
                    orgao_id: formData.get('orgaoId'),
                    analista_id: formData.get('analista'),
                    desenvolvedor_id: formData.get('desenvolvedor')
                }),
            });

            const data = await response.json();

            if (response.ok) {
                exibirMensagem('Projeto cadastrado com sucesso!');
                form.reset();
                form.classList.remove('was-validated');
            } else {
                // Exibe mensagem de erro da API ou padrão
                const erro = data.error || data.message || 'Erro no cadastro do projeto';
                exibirMensagem(erro, false);
            }
        } catch (error) {
            console.error('Erro:', error);
            exibirMensagem('Erro ao conectar com o servidor.', false);
        }
    });
