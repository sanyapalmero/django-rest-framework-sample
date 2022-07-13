from django.db import models


class Book(models.Model):
    name = models.CharField(
        max_length=255, unique=True, db_index=True, verbose_name="Название"
    )
    published_at = models.DateTimeField(
        verbose_name="Дата публикации", auto_now_add=True
    )
    pages = models.SmallIntegerField(verbose_name="Кол-во страниц")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена")
    author = models.ForeignKey(
        "auth.User",
        verbose_name="Автор",
        related_name="books",
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["published_at"]
