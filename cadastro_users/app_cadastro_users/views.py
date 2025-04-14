from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,"usuarios/home.html")

def usuarios(request):

    # Salvar dados da tela no banco de dados

    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome_post')
    novo_usuario.idade = request.POST.get('idade_post')
    novo_usuario.save()

    # Exibir todos os usuários já cadastrados em uma nova página  

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar dados para a página de listagem

    return render(request, 'usuarios/usuarios.html', usuarios)