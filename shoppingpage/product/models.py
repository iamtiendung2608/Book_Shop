from operator import mod
from django.db import models
from django.urls import reverse

# Create your models here.
class tag(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=12)
    tag = models.ManyToManyField(tag)
    image = models.TextField()
    def __str__(self):
        return self.name
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.pk)+" "+self.user.name