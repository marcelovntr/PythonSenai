from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('criar/', views.criar_item, name='criar_item'),
    path('listar/', views.listar_itens, name='listar_itens'),
    path('deletar/<int:id>', views.deletar_item, name='deletar_item'),
    path('atualizar/<int:id>', views.atualizar_item, name='atualizar_item')


]