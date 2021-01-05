from django.db import models


class Lingua(models.Model):
    codigo = models.SlugField(primary_key=True)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.codigo
