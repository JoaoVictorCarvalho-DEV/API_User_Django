from django.shortcuts import render

# Create your views here.
def cadastrar_projeto(request):
    return render(request, "projetos/cadastrar_projeto.html")

def ver_projetos(request):
    return render(request, "projetos/ver_projetos.html")

def editar_projeto(request, projeto_id):
    return render(request, "projetos/editar_projeto.html", {'projeto_id': projeto_id}) #Passamos o id que vem através da url

def ver_projeto(request, projeto_id):
    return render(request, "projetos/ver_projeto.html", {'projeto_id': projeto_id}) #Passamos o id que vem através da url
