from django.db import models


NULLABLE = {"blank": True, "null": True}


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    slug = models.CharField(max_length=150, verbose_name="slug", **NULLABLE)
    body = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='blog/', verbose_name="Изображение", **NULLABLE)
    data_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    view_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
