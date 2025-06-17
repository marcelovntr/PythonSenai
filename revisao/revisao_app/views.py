from django.shortcuts import render, redirect
from .models import Item
from django.contrib import messages

# Create your views here.
def home(request):
   #comentário teste 
   return render(request, 'revisao_app/pages/home.html')
#lembrar do:  See Real World Examples From GitHub

def criar_item(request):
   if request.method == 'GET':
      return render(request, 'revisao_app/pages/criar.html')
   if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        
        if not all ([nome, sobrenome, email]):
            messages.error(request, "Todos os campos devem ser preenchidos!")
            return redirect('criar_item')
            # return render(request, 'revisao_app/pages/criar.html', {
            # 'nome': nome,
            # 'sobrenome': sobrenome,
            # 'email': email
            #                     }) #deixa os campos preenchidos
                
        Item.objects.create(nome=nome, sobrenome=sobrenome, email=email)
        messages.success(request, f"Item: {nome} criado com sucesso!")
        return redirect('criar_item')


def listar_itens(request):
   itens = Item.objects.all().order_by('nome')

   return render(request, 'revisao_app/pages/listar.html', context={'itens': itens})

def deletar_item(request, id):
   item_encontrado = Item.objects.get(id=id)
   try:
        item_encontrado.delete()
        messages.success(request, f"Item: {item_encontrado.nome} deletado com sucesso!")
   except Exception as e:
        messages.error(request, f"Erro ao deletar palavra: {item_encontrado.vocabulo}. Detalhes: {str(e)}")
       
   return redirect('listar_itens')

def atualizar_item(request, id):
    if request.method == 'GET':
        item_achado = Item.objects.get(id=id)
        return render(request, 'revisao_app/pages/atualizar.html', context={'item_achado': item_achado})
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
    
    Item.objects.filter(id=id).update(
        nome = nome,
        sobrenome = sobrenome,
        email = email,
    )
    messages.success(request, f"Dados do item: {nome} atualizados com sucesso!")

    return redirect('listar_itens')