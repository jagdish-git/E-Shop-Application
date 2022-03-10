from django.contrib import admin
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Order)