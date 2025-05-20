// Seleciona todas as tarefas e seções
esperar(2000).then(async () => {
    document.querySelectorAll('.tarefa').forEach(task => {
        task.addEventListener('dragstart', handleDragStart);

    });
})

document.querySelectorAll('.status-section').forEach(section => {
    section.addEventListener('dragover', handleDragOver);
    section.addEventListener('drop', handleDrop);
});

let draggedTask = null;

// Função para iniciar o arrasto
function handleDragStart(e) {
    draggedTask = e.target;
    e.dataTransfer.setData('text/plain', draggedTask.dataset.taskId);
}

// Função para permitir soltar
function handleDragOver(e) {
    e.preventDefault(); // Permite o drop
    e.currentTarget.style.backgroundColor = '#f8f9fa'; // Feedback visual
}

// Função para soltar a tarefa
async function handleDrop(e) {
    e.preventDefault();
    const newStatusSection = e.currentTarget;
    const taskId = draggedTask.dataset.taskId;
    // Atualiza o status no backend (ex.: via API)
    try {
        const response = await fetch(`../../../../api/v1/tarefas/${taskId}/`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({status: newStatusSection.id}),
        });

        if (response.ok) {
            // Move a tarefa para a nova seção
            newStatusSection.appendChild(draggedTask);
            draggedTask.dataset.status = newStatusSection.id; // Atualiza o status no HTML
            window.location.reload()
        }
    } catch (error) {
        console.error('Erro ao atualizar o status:', error);
    }

    newStatusSection.style.backgroundColor = ''; // Remove o feedback visual
}