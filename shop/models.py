from django.db import models
from django.contrib.auth.models import User,auth
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms
# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=5000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")


    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=" ")
    update_desc = models.CharField(max_length=500)
    timestamp = models.DateField(auto_now_add =True)

    def __str__(self):
        return self.update_desc[0:7]+"..."

class Picture(models.Model):
    UserAccountName=models.CharField(max_length=15,default="")
    comment=models.CharField(max_length=100,default="")

    def __str__(self):
        return self.comment

class SubCategoryProduct(models.Model):
    subcategory = models.ForeignKey(Product , on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='shop/images', default="")

class Order_Book(models.Model):
    product = models.IntegerField()
    product_name = models.CharField(max_length=100)
    customer= models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(upload_to='shop/images', default="")

