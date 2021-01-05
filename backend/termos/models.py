from django.db import models
from linguas.models import Lingua


class Termo(models.Model):
    lingua = models.ForeignKey(Lingua, on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.texto} ({self.lingua})'
