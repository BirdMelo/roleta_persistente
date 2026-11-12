from django.db import models

class Usuario(models.Model):
    id = models.BigAutoField(primary_key = True)
    nome = models.CharField(max_length = 100, null = False, unique = True)
    senha = models.CharField(max_length = 120, null = False)
    dark_mode = models.BooleanField(null = False, default = False)

    class Meta:
        db_table = 'Usuario'
        ordering = ['nome']