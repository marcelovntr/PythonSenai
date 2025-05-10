from django.shortcuts import render, redirect
# from django.http import HttpResponse
from pizza_app.models import PizzaModel, UsuarioModel
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    # lista_produtos = [
        
    #     {
    #         'img': 'https://w3c.br/wp-content/uploads/2010/09/Prancheta-1.png',
    #         'nome': 'HTML',
    #         'detalhes': 'huauhauh, huahua, ppipipi',
    #         'preco': 'R$ ??,??',
    #     },
    #
    # ]
    print(request.session.get('item', []))
    lista_produtos = PizzaModel.objects.all()
    # mandar_email('recebedor@gmail', 'mensagem', 'assunto')
    return render(request, "pizza_app/pages/home.html", context={'produtos': lista_produtos})

def criar_pizza(request):
    if request.method == 'GET':
        return render(request, 'pizza_app/pages/pizza.html')
    
    img = request.POST.get('img')
    nome = request.POST.get('nome')
    detalhes = request.POST.get('detalhes')
    preco = request.POST.get('preco')
    nome = PizzaModel.objects.create(img=img, nome=nome, detalhes=detalhes, preco=preco)
    return render(request, 'pizza_app/pages/pizza.html', context={'nome': nome})

def listar_pizzas(request):
    nomes= PizzaModel.objects.all()
    return render(request, 'pizza_app/pages/listar.html', context={'nomes': nomes})

def deletar_pizza(resquest, id):
    nome = PizzaModel.objects.get(id=id)
    nome.delete()
    return redirect('listar')

def atualizar_pizza(request, id):
    if request.method == 'GET':
        nome = PizzaModel.objects.get(id=id)
        return render(request, 'pizza_app/pages/atualizar_pizza.html', context={'nome': nome})
    
    img = request.POST.get('img')
    nome = request.POST.get('nome')
    detalhes = request.POST.get('detalhes')
    preco = request.POST.get('preco')
    # PizzaModel.objects.create(img=img, nome=nome, detalhes=detalhes, preco=preco)
    # return render(request, 'listar')
    PizzaModel.objects.filter(id=id).update(img=img, nome=nome, detalhes=detalhes, preco=preco)
    return redirect('listar')

def carrinho_pizza(request, id):
   itens = request.session.get('item', [])
   itens.append(id)
   request.session['item'] = itens

   quantidade_itens = request.session.get('quantidade_itens', 0) #seria possível retirar essa linha, segundo eu + GPT
   quantidade_itens = len(itens)
   request.session['quantidade_itens'] = quantidade_itens
   #return HttpResponse('Conteúdo adicionado ao carrinho!')
   return redirect('home')

def comprar_carrinho_pizza(request):
    itens = request.session.get('item', [])
    lista_itens = []
    for item in itens: #este for foi inserido para ser possível obter itens repitidos do banco de dados
        item = PizzaModel.objects.get(id=item)
        lista_itens.append(item)
    return render(request, 'pizza_app/pages/listar_carrinho.html', context={'itens': lista_itens, 'quantidade_itens': len(itens)})


def mandar_email(usuario,mensagem,titulo):
    print(f'Enviando email para {usuario} com a mensagem: {mensagem}')
    send_mail(
    titulo,
    mensagem,
    'seu_email@gmail.com',
    [usuario],
    fail_silently=False,
)
    
def cadastrar_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if usuario and email and senha:
            User.objects.create_user(usuario=usuario, email=email, senha=senha)
        return render(request, 'login.html') 
    return render(request, 'pizza_app/pages/cadastro_usuario.html')

def login_request(request):
    message = ''
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('home')
        message = 'Usuário ou senha inválidos'
    return render(request, 'pizza_app/pages/login.html', {'message': message})
