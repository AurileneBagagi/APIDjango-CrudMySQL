from django.db import models

# Create your models here.
class PosterDados(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=70)
    descricao = models.CharField(max_length=200)
    datapublicacao = models.DateField(auto_now=True)
    published = models.BooleanField(default=False)
                              