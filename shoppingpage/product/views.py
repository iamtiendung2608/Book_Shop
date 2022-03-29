from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
# Create your views here.
from .models import Item,Order,User, tag
from .forms import MyForm, CreateUserFrom
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = CreateUserFrom()
        if request.method == "POST":
            form = CreateUserFrom(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Hello ' + user)
                return HttpResponseRedirect('login')
        context = {'form':form}
        return render(request,'regist.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username = username, password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.info(request,'username or password is incorrect')
    context = {}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def homepage(request):
    q = request.GET.get('text',None)
    if q is None or q == '':
        Items = Item.objects.all()
    elif q is not None:
        Items = Item.objects.filter(name__contains = q)
    return render(request,'homepage.html',{'Items':Items})


@login_required(login_url='login')
def details(request, id=None):
    item = Item.objects.get(id=id)
    return render(request,'details.html',{'item':item})

@login_required(login_url='login')
def userDetails(request,id=None):
    user = User.objects.get(id=id)
    item = User.order_set.all()
    content = {
        'user':user,
        'item':item
    }
    return render(request,'cart.html',content)

@login_required(login_url='login')
def tagDetails(request,id=None):
    items = Item.objects.filter(tag__id=id)
    return render(request,'tagDetails.html',{'Items':items})

@login_required(login_url='login')
def create(request):
    if request.method == 'POST' :
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
    return render(request, 'edit.html',{'form':form})
