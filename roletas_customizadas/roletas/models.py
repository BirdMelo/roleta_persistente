from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from ..accounts.models import Usuario

class Roleta(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete = models.CASCADE,
        related_name = 'roletas'
    )
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False)
    descricao = models.TextField(null=True)
    som_giro_enabled = models.BooleanField(null=False, default=False)
    efeito_enabled = models.BooleanField(null=False, default=False)
    texto_botao_giro = models.CharField(max_length=45, null=False, default='Girar!')
    cor_bg = models.CharField(max_length=7, validators=[MinLengthValidator(7)], null=False, default='#6C3CE9')
    remover_fatia_sorteada = models.BooleanField(null=False,default=False)

    class Meta:
        db_table = 'Roleta'
        ordering = ['nome']
        constraints = [
            models.UniqueConstraint(
                fields = ['usuario', 'nome'],
                name='uk_roleta_usuario_nome'
            )
        ]

class ItemRoleta(models.Model):
    roleta = models.ForeignKey(
        Roleta,
        on_delete=models.CASCADE,
        related_name='itens'
    )
    id = models.BigAutoField(primary_key=True)
    texto = models.CharField(max_length=45, null=False)
    cor_bg = models.CharField(max_length=7, validators=[MinLengthValidator(7)], null=True)
    peso = models.FloatField(null=False, default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    ordem = models.PositiveIntegerField(null=False)

    class Meta:
        ordering = ['ordem']
        constraints = [
            models.UniqueConstraint(
                fields = ['roleta', 'ordem'],
                name = 'uk_item_roleta_ordem'
            ),
            models.UniqueConstraint(
                fields=['roleta', 'texto'],
                name='uk_item_roleta_texto'
            )
        ]
