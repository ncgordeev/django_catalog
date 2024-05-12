from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_title', 'product_price', 'product_category_id',)
    list_filter = ('product_category_id',)
    search_fields = ('product_title', 'product_description')
