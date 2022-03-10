from django.db import models
from .customer import Customer
from .category import Category
from .product import Product
from datetime import datetime

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=110)
    phone = models.CharField(max_length=10)
    date_time = models.DateTimeField(default=datetime.now)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name

    def placeOrder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date_time')