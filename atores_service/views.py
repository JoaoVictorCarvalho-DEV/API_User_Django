from django.shortcuts import render


# Create your views here.
def cadastrar_ator(request):
    return render(request, "atores/cadastrar_ator.html")

def ver_atores(request):
    return render(request, "atores/ver_atores.html")

def editar_ator(request, ator_id):
    return render(request, "atores/editar_ator.html",{'ator_id': ator_id})

def ver_ator(request, user_id):
    return render(request, "atores/ver_ator.html", {'user_id': user_id})