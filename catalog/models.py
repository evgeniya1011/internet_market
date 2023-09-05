from django.db import models

NULLABLE = {"blank": True, "null": True}

class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    descriptions = models.TextField(verbose_name='Описание')
    picture = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена за покупку')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.product_name}: {self.descriptions}, {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Contacts(models.Model):
    contact_name = models.CharField(max_length=100, verbose_name='Имя')
    ph_number = models.CharField(max_length=100, verbose_name='Телефоный номер')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f'{self.contact_name}: {self.ph_number} - {self.message}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

