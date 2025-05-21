/**
 * Configura os listeners de drag-and-drop para tarefas e seções de status após um delay de 2 segundos.
 * - Adiciona `dragstart` às tarefas.
 * - Adiciona `dragover` e `drop` às seções de status.
 */
esperar(2000).then(async () => {
    document.querySelectorAll('.tarefa').forEach(task => {
        task.addEventListener('dragstart', handleDragStart);
    });
});

document.querySelectorAll('.status-section').forEach(section => {
    section.addEventListener('dragover', handleDragOver);
    section.addEventListener('drop', handleDrop);
});

let draggedTask = null; // Armazena a tarefa sendo arrastada.

/**
 * Manipula o início do arrasto de uma tarefa.
 * @param {DragEvent} e - Evento de dragstart.
 */
function handleDragStart(e) {
    draggedTask = e.target;
    e.dataTransfer.setData('text/plain', draggedTask.dataset.taskId);
}

/**
 * Permite que uma tarefa seja solta em uma seção de status (previne o comportamento padrão).
 * @param {DragEvent} e - Evento de dragover.
 */
function handleDragOver(e) {
    e.preventDefault(); // Permite o drop.
    e.currentTarget.style.backgroundColor = '#f8f9fa'; // Feedback visual.
}

/**
 * Manipula o evento de soltar uma tarefa em uma seção de status.
 * - Atualiza o status no backend via API.
 * - Move a tarefa para a nova seção no DOM se a requisição for bem-sucedida.
 * @param {DragEvent} e - Evento de drop.
 * @throws {Error} Se a requisição API falhar.
 */
async function handleDrop(e) {
    e.preventDefault();
    const newStatusSection = e.currentTarget;
    const taskId = draggedTask.dataset.taskId;

    try {
        const response = await fetch(`../../../../api/v1/tarefas/${taskId}/`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ status: newStatusSection.id }),
        });

        if (response.ok) {
            newStatusSection.appendChild(draggedTask); // Move no DOM.
            draggedTask.dataset.status = newStatusSection.id; // Atualiza o atributo.
            window.location.reload(); // Recarrega a página para sincronizar.
        }
    } catch (error) {
        console.error('Erro ao atualizar o status:', error);
    }

    newStatusSection.style.backgroundColor = ''; // Remove o feedback visual.
}