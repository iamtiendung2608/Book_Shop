import imp
from django.contrib import admin
from .models import Item,User,Order,tag
# Register your models here.
admin.site.register(Item)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(tag)
