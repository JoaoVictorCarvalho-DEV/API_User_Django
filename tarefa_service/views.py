from django.shortcuts import render

# Create your views here.
def cadastrar_tarefa(request):
    return render(request, template_name="tarefas/cadastrar_tarefa.html")

def ver_tarefas(request):
    return render(request, template_name="tarefas/ver_tarefas.html")

