from django.shortcuts import render

# Create your views here.

def home(request):
    contexto = {}
    
    return render(request, 'core/home.html', contexto)