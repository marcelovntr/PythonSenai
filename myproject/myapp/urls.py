from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path("turismo/", views.turismo),
    path("contato/", views.contato),
]