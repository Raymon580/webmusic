from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "audify/index.html")

def login(request):
    return render(request, "audify/login.html")