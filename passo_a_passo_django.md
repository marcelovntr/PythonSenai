
# 🛠️ Passo a Passo: Projeto Django - CRUD Básico

## 🚀 Iniciando o Projeto

### 1️⃣ (Opcional) Criar ambiente virtual:
   ```bash
   python -m venv .venv #(.venv ou somente venv)
   ```
   Atualizar o gerenciador de pacotes:

   ```bash
   python.exe -m pip install --upgrade pip

   ```

### 2️⃣ Comandos iniciais:
   ```bash
   pip install django
   django-admin startproject projetinho
   cd projetinho  # não esquecer!
   python manage.py startapp projetinho_app
   ```

## ⚙️ Configurando `settings.py`

- Adicionar o app ao `INSTALLED_APPS`:
   ```python
   INSTALLED_APPS = [
       ...
       "projetinho_app",
   ]
   ```

## 🌐 Configurando URLs

### 1️⃣ URLs do Projeto (arquivo `projetinho/urls.py`)

- Importar `include`:
   ```python
   from django.urls import path, include
   ```

- Declarar as rotas:
   ```python
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('projetinho_app.urls')),
   ]
   ```

### 2️⃣ URLs do App (arquivo `projetinho_app/urls.py`)

- Criar o arquivo `urls.py` dentro do app e adicionar:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.home, name='home'),
       path('demais/', views.demais, name='demais'),
   ]
   ```

## 🧱 Models

- Em `projetinho_app/models.py`:
   ```python
   from django.db import models

   class Item(models.Model):
       nome = models.CharField(max_length=100)
       descricao = models.CharField(max_length=200)

       def __str__(self):
           return self.nome + ' - ' + self.descricao
   ```

## 🖼️ Templates

- Criar a pasta `templates/` com os seguintes arquivos:
  - `index.html` (ou `home.html`)
  - `criar.html`
  - `listar.html`
  - `editar.html` (parecido com `criar`, mas com valores preenchidos --> value="{{item.nome}}" ...)

- Usar template base (`base.html`) para reaproveitar layout
   
   ```html
   <!DOCTYPE html>
      <html lang="pt-br">
      <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <link rel="stylesheet" href="{% static 'css/style.css' %}">
      </head>
      <body>
   ```
      {% block conteudo %}

- Sintaxe Jinja/Django:
   ```django
   {% extends 'projetinho_app/global/base.html' %}
   {% load static %}

   {% block title %}Título{% endblock %}


   {% block content %}
      Conteúdo aqui
   {% endblock %}
   ```

## 🎨 Static

- Criar a pasta `static/` (no mesmo nível da pasta `templates/`)
  - Subpastas sugeridas:
    - `css/`
    - `js/`
    - `img/`

## 🧠 Views

- Exemplo de view simples:
   ```python
   from django.shortcuts import render, redirect
   from .models import Item #o modelo criado
   from django.contrib import messages

   def home(request):
       return render(request, 'nome_app/pages/home.html')
   ```

- Outras funções esperadas:
  - `criar()`
      ```python
         def criar_item(request):
            if request.method == 'GET':
               return render(request, 'revisao_app/pages/criar.html')
            if request.method == 'POST':
               nome = request.POST.get('nome')
               sobrenome = request.POST.get('sobrenome')
               email = request.POST.get('email')
               Item.objects.create(nome=nome, sobrenome=sobrenome, email=email)
               messages.success(request, f"Item: {nome} criado com sucesso!")
               return redirect('criar_item')
      ```
  - `listar()`
      ```python
        def listar_itens(request):
            itens = Item.objects.all().order_by('nome')

            return render(request, 'revisao_app/pages/listar.html', context={'itens': itens})

      ```
  - `editar()`
      ```python
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

      ```
  - `deletar()`
      ```python
       def deletar_item(request, id):
            item_encontrado = Item.objects.get(id=id)
            try:
               item_encontrado.delete()
               messages.success(request, f"Item: {item_encontrado.nome} deletado com sucesso!")
            except Exception as e:
               messages.error(request, f"Erro ao deletar palavra: {item_encontrado.vocabulo}. Detalhes: {str(e)}")
               
            return redirect('listar_itens')

      ```

