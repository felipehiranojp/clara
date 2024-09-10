from django.db import models

class Tabela(models.Model):
    nome = models.CharField(max_length=20)
    email = models.EmailField(unique=False)
    estilo = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.email