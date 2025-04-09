from django.shortcuts import render

# Create your views here.
def cadastrar_tarefa(request):
    return render(request, template_name="tarefas/cadastrar_tarefa.html")

def ver_tarefas(request):
    return render(request, template_name="tarefas/ver_tarefas.html")

def editar_tarefa(request, tarefa_id):
    return render(request, "tarefas/editar_tarefa.html", {'tarefa_id': tarefa_id}) #Passamos o id que vem através da url

