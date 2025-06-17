from django.db import models

# Create your models here.
class Item (models.Model):
    nome= models.CharField(max_length=100)
    sobrenome= models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"({self.nome}, {self.sobrenome}), {self.email}" 

    