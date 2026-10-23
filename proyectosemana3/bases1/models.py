# Create your models here.
from django.db import models

class musico(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    fecha_fallecimiento = models.DateField(null=True, blank=True)
    musicas_compuestas = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.fecha_nacimiento} {self.fecha_fallecimiento} {self.musicas_compuestas} {self.descripcion}'

class tipo_de_musica(models.Model):
    nombre_de_la_musica = models.CharField(max_length=25) 
    tipo_de_musica = models.CharField(max_length=15)
    banda_de_musica = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre_de_la_musica} {self.tipo_de_musica} {self.banda_de_musica}'

class instrumentos(models.Model):
    nombre_del_instrumento = models.CharField(max_length=25) 
    tipo_de_instrumento = models.CharField(max_length=25)
    que_musica_lo_uso = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.nombre_del_instrumento} {self.tipo_de_instrumento} {self.que_musica_lo_uso} {self.descripcion}'


genero_tipico = models.ForeignKey(tipo_de_musica, on_delete=models.SET_NULL, null=True, blank=True)

genero_principal = models.ForeignKey(tipo_de_musica, on_delete=models.CASCADE, null=True, blank=True)


