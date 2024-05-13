from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    category_title = models.CharField(
        max_length=100,
        verbose_name='Категория'
    )
    category_description = models.TextField(
        verbose_name='Описание категории'
    )

    def __str__(self):
        return f'{self.category_title} {self.category_description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    product_title = models.CharField(
        max_length=100,
        verbose_name='Товар'
    )
    product_description = models.TextField(
        verbose_name='Описание товара'
    )
    product_preview = models.ImageField(
        verbose_name='Превью',
        **NULLABLE
    )
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_price = models.FloatField(
        verbose_name='Цена'
    )
    created_at = models.DateField(
        auto_now=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата обновления'
    )

    def __str__(self):
        return f'{self.product_title} {self.product_description}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('product_title', 'product_price',)
