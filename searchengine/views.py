from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index/index.html')

def login(request):
    return HttpResponse("Hello, world. You're at the login page.")

def register(request):
    return HttpResponse("Hello, world. You're at the register page.")

def landing(request):
    return HttpResponse("Hello, world. You're at the landing page.")

def importfiles(request):
    return HttpResponse("Hello, world. You're at the import page.")


