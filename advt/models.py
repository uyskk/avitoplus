from django.contrib.auth.models import User
from django.db import models


class Advert(models.Model):

    title = models.CharField(max_length=128, verbose_name="Заголовок объявления")
    text = models.TextField(blank=True, null=True, verbose_name="Информация об объявлении")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    address = models.CharField(max_length=128, verbose_name="Адресс")
    photo = models.ImageField(upload_to="uploads/", verbose_name="Фото")

    is_liked = models.BooleanField(default=False, verbose_name="Пользователь поставил лайк")

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")

    def __str__(self):
        return self.title


class Like(models.Model):

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    advt = models.ForeignKey(Advert, null=True, on_delete=models.SET_NULL)

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'advt'], name="unique_like"),
        ]


class Comment(models.Model):

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    advt = models.ForeignKey(Advert, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=255, verbose_name="Текст комментария")

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
