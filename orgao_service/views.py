from django.shortcuts import render

# Create your views here.
def cadastrar_orgao(request):
    return render(request, "orgaos/cadastrar_orgao.html")

def ver_orgaos(request):
    return render(request, "orgaos/ver_orgaos.html")


def editar_orgao(request, orgao_id):
    return render(request, "orgaos/editar_orgaos.html", {'orgao_id': orgao_id}) #Passamos o id que vem através da url