from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
#from ckeditor.fields import RichTextField
#from ckeditor_uploader.fields import RichTextUploadingField


def randomString():
    um = UserManager()
    return( um.make_random_password( length=25 ) )


class Category(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, default=randomString, blank=True, null=True)


    def __str__(self):
        return self.nome 


class Churrasco(models.Model):
    nome_receita = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=False, blank=True, null=True)
    ingredientes = models.TextField(blank=True, null=True)
    modo_preparo = models.TextField(blank=True, null=True)
    tempo_preparo = models.IntegerField(blank=True, null=True)
    rendimento = models.CharField(max_length=100, blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    date_receita = models.DateTimeField(default=datetime.now, blank=True, null=True)
    autor = models.ForeignKey(User, max_length=255, on_delete= models.CASCADE, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    authorimage = models.ImageField (verbose_name='Imagem do Autor', blank=True, null=True)
    thumbnail = models.ImageField(verbose_name='Capa do Post', blank=True, null=True)
  

    def __str__(self):
        return self.nome_receita + '/' + str(self.autor)
