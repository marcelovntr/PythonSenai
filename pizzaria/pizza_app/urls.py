from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("pizza/", views.criar_pizza, name='pizza'),
    path("listar/", views.listar_pizzas, name='listar'),
    path("deletar/<int:id>", views.deletar_pizza, name='deletar_pizza'),
    path("atualizar/<int:id>", views.atualizar_pizza, name='atualizar_pizza'),
    path("carrinho/<int:id>", views.carrinho_pizza, name='carrinho_pizza'),
    path("carrinho/", views.comprar_carrinho_pizza, name='comprar_carrinho_pizza'),
    
    path('cadastro_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
]


