from django.db import models

# Create your models here.
class PizzaModel(models.Model):
    img = models.URLField()
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    detalhes = models.TextField()

    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pizza({self.nome}, {self.preco}, {self.detalhes})"

class UsuarioModel(models.Model):
    usuario = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=20)

    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Usuário({self.usuario}, {(self.email), {(self.senha)}})"
