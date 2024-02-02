from django.db import models


class Book(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255)
    author = models.CharField(verbose_name='Author', max_length=255)
    genre = models.CharField(verbose_name='Genre', max_length=255)
    price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

