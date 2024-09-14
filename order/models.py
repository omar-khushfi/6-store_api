from django.db import models
from operator import mod
from django.contrib.auth.models import User
from app.models import *
# Create your models here.


class OrderStatus(models.TextChoices):
    PROCESSING='processing'
    SHIPPED='Shipped'
    DELIVERED='DeliveredS'



class PaymentStatus(models.TextChoices):
    PAID='Paid'
    UNPAID='Unpaid'



class PaymentMode(models.TextChoices):
    COD='Cod'
    CARD='Card'
    
    
class Order(models.Model):
    city=models.CharField(max_length=100,default="",blank=False)
    zipcode=models.CharField(max_length=100,default="",blank=False)
    street=models.CharField(max_length=500,default="",blank=False)
    state=models.CharField(max_length=100,default="",blank=False)
    country=models.CharField(max_length=100,default="",blank=False)
    phone_number=models.CharField(max_length=100,default="",blank=False)
    total_amount=models.IntegerField(default=0)
    paymentstatus=models.CharField(choices=PaymentStatus,max_length=30,default=PaymentStatus.UNPAID)
    paymentmode=models.CharField(choices=PaymentMode,max_length=30,default=PaymentMode.COD)
    status=models.CharField(max_length=30,choices=OrderStatus,default=OrderStatus.PROCESSING)
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    


class OrderItem(models.Model):
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    order=models.ForeignKey(Order,null=True,on_delete=models.CASCADE,related_name="orderitems")
    name=models.CharField(max_length=100,default="",blank=False)
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=7,decimal_places=2,blank=False)

    def __str__(self):
        return self.name
    

