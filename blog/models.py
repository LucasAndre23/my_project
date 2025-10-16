from django.db import models
from decimal import Decimal

    # Create your models here.
class Editora(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):

        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome
        
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=13, unique=True)
    publicacao = models.DateField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)

    def __str__(self):
        return self.titulo  


        