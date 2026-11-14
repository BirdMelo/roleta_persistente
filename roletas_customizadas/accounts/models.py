from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UsuarioManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('O usuário precisa de um nome de usuário.')

        usuario = self.model(username=username, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(
        max_length=37,
        unique=True,
        db_column='nome'
    )
    password = models.CharField(max_length=128, db_column='senha')
    dark_mode = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'Usuario'
        ordering = ['username']

    def __str__(self):
        return f'Usuário: {self.username}'