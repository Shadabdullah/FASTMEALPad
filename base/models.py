from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name





class Order(models.Model):
    PAYMENT_CHOICES = [
        ('Cash', 'Cash'),
        ('Paid', 'Paid'),
    ]
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Out for delivery', 'Out for delivery'),
        ('Cancelled', 'Cancelled'),
    )

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    customer_name = models.CharField(max_length=200, null=True)
    item_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    prepaid_postpaid = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField(null=True)
    order_number = models.CharField(max_length=100)

    status = models.CharField(max_length=200, null=True, choices=STATUS)
    booking_time = models.DateTimeField() 
    delivery_time = models.DateTimeField() 

    def __str__(self) -> str:
        return self.customer_name

