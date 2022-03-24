from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from .models import Item,Order,User, tag
from .forms import MyForm
def homepage(request):
    q = request.GET.get('text',None)
    if q is None or q is '':
        Items = Item.objects.all()
    elif q is not None:
        Items = Item.objects.filter(name__contains = q)
    return render(request,'homepage.html',{'Items':Items})



def details(request, id=None):
    item = Item.objects.get(id=id)
    return render(request,'details.html',{'item':item})
def userDetails(request,id=None):
    user = User.objects.get(id=id)
    item = User.order_set.all()
    content = {
        'user':user,
        'item':item
    }
    return render(request,'cart.html',content)
    
def tagDetails(request,id=None):
    items = Item.objects.filter(tag__id=id)
    return render(request,'tagDetails.html',{'Items':items})
def create(request):
    if request.method == 'POST' :
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
    return render(request, 'edit.html',{'form':form})
