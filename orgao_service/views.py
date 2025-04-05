from django.shortcuts import render

# Create your views here.
def cadastrar_orgao(request):
    return render(request, "orgaos/cadastrar_orgao.html")

def ver_orgaos(request):
    return render(request, "orgaos/ver_orgaos.html")


def editar_orgao(request, projeto_id):
    return render(request, "projetos/editar_projeto.html", {'projeto_id': projeto_id}) #Passamos o id que vem através da url