from django.shortcuts import render

# Create your views here.
def home(request):
    lista_produtos = [
        
        {
            'img': 'https://w3c.br/wp-content/uploads/2010/09/Prancheta-1.png',
            'nome': 'HTML',
            'detalhes': 'huauhauh, huahua, ppipipi',
            'preco': 'R$ ??,??',
        },
          {
            'img': 'https://www.stickersdevs.com.br/wp-content/uploads/2015/03/css3-stickers-adesivo.png',
            'nome': 'CSS',
            'detalhes': 'huauhauh, huahua, ppipipi',
            'preco': 'R$ ??,??',
        },
          {
            'img': 'https://devblogs.microsoft.com/python/wp-content/uploads/sites/12/2018/08/pythonfeature.png',
            'nome': 'Python',
            'detalhes': 'huauhauh, huahua, ppipipi',
            'preco': 'R$ 00,00',
        },
        {
            'img': 'https://media.geeksforgeeks.org/wp-content/uploads/20200210175202/django-basics.png',
            'nome': 'Django',
            'detalhes': 'huauhauh, huahua, ppipipi',
            'preco': 'R$ 00,00',
        },
        {
            'img': 'https://saidvandeklundert.net/img/jinja_logo.png',
            'nome': 'Jinja',
            'detalhes': 'huauhauh, huahua, ppipipi',
            'preco': 'R$ 00,00',
        },
        {
            'img': 'https://user-images.githubusercontent.com/51070104/268566349-c41e65a5-2ab9-4b54-8cbc-350ab6da746c.png',
            'nome': 'Flask',
            'detalhes': 'huauhauh, huahua, ppipipi',
            'preco': 'R$ ??,??',
        },
    ]
    return render(request, "pizza_app/pages/home.html", context={'produtos': lista_produtos})
# def sobre(request):
#     return render(request, 'sobre.html')