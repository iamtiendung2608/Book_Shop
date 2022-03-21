from django.shortcuts import render
# Create your views here.
from .models import Item
def homepage(request):
    Items = Item.objects.all()
    return render(request,'homepage.html',{'Items':Items})
def details(request, id=None):
    item = Item.objects.get(id=id)
    return render(request,'details.html',{'item':item})
