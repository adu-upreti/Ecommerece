from django.contrib import admin
from product.models import Products, Category
from django.apps import AppConfig

admin.site.register(Products)
admin.site.register(Category)

class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'

    def ready(self):
        import product.signals
