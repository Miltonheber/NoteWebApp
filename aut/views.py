from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import UserInfo
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            return render(request, 'login.html', {
                'username':username,
                'senha':senha
            })
        else:
            auth.login(request, usuario)
    return render(request, 'login.html', {})


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('user').strip()
        apelido = request.POST.get('apelido').strip()
        email = request.POST.get('email').strip()
        senha = request.POST.get('senha').strip()

        if not nome or not apelido or not email or not senha:
            return render(request, 'cadastro.html', {
                'nome':nome,
                'email':email,
                'apelido':apelido,
                'senha':senha
                
            })
        elif len(senha) < 8:
            return render(request, 'cadastro.html', {
                             'nome':nome,
                             'email':email,
                             'apelido':apelido,
                            'senha':senha     
                         })
        elif UserInfo.objects.filter(email=email).exists():
            return render(request, 'cadastro.html', {
                             'nome':nome,
                             'email':email,
                             'apelido':apelido,
                            'senha':senha
            
                         })
        elif User.objects.filter(username=nome).exists():
            return render(request, 'cadastro.html', {
                'nome':nome,
                'email':email,
                'apelido':apelido,
                'senha':senha
            })
        
        else:
            user = User.objects.create_user(username=nome, password=senha)
            usuario = UserInfo(
                nome=apelido,
                email=email,
                user=user
            )
            usuario.save()
            

        

            return HttpResponse(f'nome: {nome} senha: {senha}')
    return render(request, 'cadastro.html', {})

def logout(request):
    auth.logout(request)
    return redirect('/auth/login/')
    
