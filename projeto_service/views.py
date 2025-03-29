from django.shortcuts import render

# Create your views here.
def cadastrar_projeto(request):
    return render(request, "projetos/cadastrar_projeto.html")

def ver_projetos(request):
    return render(request, "projetos/ver_projetos.html")