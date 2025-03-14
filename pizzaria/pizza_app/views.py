from django.shortcuts import render

# Create your views here.
def home(request):
    lista_produtos = [
        {
            'img': 'http://',
            'nome': 'pizza 4 queijos',
            'ingredientes': 'huauhauh, huahua, ppipipi',
            'preco': 'R$ 90,00',
        },
        {
            'img': 'http://',
            'nome': 'pizza de boldo',
            'ingredientes': 'huauhauh, huahua, ppipipi',
            'preco': 'R$ 66,00',
        },
        {
            'img': 'http://',
            'nome': 'pizza 4 carqueja',
            'ingredientes': 'huauhauh, huahua, ppipipi',
            'preco': 'R$ 60,00',
        },
    ]
    return render(request, "pizza_app/pages/home.html", context={'produtos': lista_produtos})
# def sobre(request):
#     return render(request, 'sobre.html')