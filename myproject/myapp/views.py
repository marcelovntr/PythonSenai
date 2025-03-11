from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def turismo(request):
    return render(request, 'turismo.html')
def contato(request):
    return render(request, 'contato.html')
