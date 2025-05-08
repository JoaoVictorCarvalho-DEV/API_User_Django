from django.shortcuts import render

# Create your views here.
def cadastrar_projeto(request):
    return render(request, "projetos/cadastrar_projeto.html")

def ver_projetos(request, user_id = None):
    if user_id is None:
        return render(request, "projetos/ver_projetos.html")
    return render(request, "projetos/ver_projetos.html", context={'user_id': user_id})

def editar_projeto(request, projeto_id):
    return render(request, "projetos/editar_projeto.html", {'projeto_id': projeto_id}) #Passamos o id que vem através da url

def ver_projeto(request, projeto_id):
    return render(request, "projetos/ver_projeto.html", {'projeto_id': projeto_id}) #Passamos o id que vem através da url
