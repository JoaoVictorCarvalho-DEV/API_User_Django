from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_api(request):
    return render(request, 'autenticacao_novo/login.html')

def registro_api(request):
    return render(request, 'autenticacao_novo/register.html')

def dash_api(request):
    return render(request, '')
