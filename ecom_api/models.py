from email.policy import default
from django.db import models
from django.contrib.auth.models import  User
# Create your models here.



class Category(models.Model):
    title = models.CharField(max_length=50 , unique= True)
    def __str__(self):
        return "%s " % self.title

class Product(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return "%s " % self.name

class Cart(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    def __str__(self):
        return "%s "% self.user.username

class CartItem(models.Model):
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete = models.CASCADE)
    price = models.IntegerField()

   