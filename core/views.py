from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {'path': request.path})

def contato(request):
    return render(request, 'contato.html')

def quem_somos(request):
    return render(request, 'quem_somos.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')