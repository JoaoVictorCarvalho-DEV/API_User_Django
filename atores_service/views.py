from django.shortcuts import render


# Create your views here.
def cadastrar_ator(request):
    return render(request, "atores/cadastrar_ator.html")

def ver_atores(request):
    return render(request, "atores/ver_atores.html")

def editar_ator(request):
    return render(request, "atores/editar_ator.html")