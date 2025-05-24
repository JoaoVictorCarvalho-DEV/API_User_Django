
document.addEventListener("DOMContentLoaded", async () => {
    const token = localStorage.getItem("token");

    const headers = {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`
    };

    const atualizarValor = (id, valor) => {
        const el = document.getElementById(id);
        if (el) el.textContent = valor;
    };

    // ---------- PROJETOS ----------
    try {
        const resProj = await fetch("/api/v1/projetos/statistics/", { headers });
        const dadosProj = await resProj.json();
        atualizarValor("projetos-ativos", dadosProj.em_andamento || 0);
    } catch (err) {
        console.error("Erro ao carregar estatísticas de projetos:", err);
    }

    // ---------- TAREFAS ----------
    try {
        const resTarefas = await fetch("/api/v1/tarefas/statistics/");
        const dadosTarefas = await resTarefas.json();

        atualizarValor("tarefas-pendentes", dadosTarefas.cancelada || 0);

        graficoTarefas.data.datasets[0].data = [
            dadosTarefas.cancelada || 0,
            dadosTarefas.em_andamento || 0,
            dadosTarefas.concluida || 0
        ];
        graficoTarefas.update();
    } catch (err) {
        console.error("Erro ao carregar estatísticas de tarefas:", err);
    }

    // ---------- ÓRGÃOS ----------
    try {
        const resOrgaos = await fetch("/api/v1/orgaos/statistics/");
        const dadosOrgaos = await resOrgaos.json();

        atualizarValor("orgaos-vinculados", dadosOrgaos.length || 0);

        graficoProjetos.data.labels = dadosOrgaos.map(o => o.nome);
        graficoProjetos.data.datasets[0].data = dadosOrgaos.map(o => o.total_projetos || 0);
        graficoProjetos.update();
    } catch (err) {
        console.error("Erro ao carregar estatísticas de órgãos:", err);
    }
});

