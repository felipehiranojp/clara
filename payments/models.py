from django.db import models

class Tabela(models.Model):
    nome = models.CharField(max_length=20,default='-')
    email = models.EmailField(unique=False,default='-')
    estilo = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.email