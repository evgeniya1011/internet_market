from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    is_active = models.BooleanField(default=False)

    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone_number = models.CharField(max_length=50, verbose_name='Номер телефона', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна')
    verif_code = models.CharField(max_length=50, verbose_name='Верификация')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
