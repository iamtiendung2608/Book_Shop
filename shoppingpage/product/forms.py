from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Item
class MyForm(ModelForm):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.CharField(label='price', widget=forms.TextInput(attrs={'class':'form-control'}))
    image = forms.CharField(label='image', widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Item
        fields = ['name','price','image']
class CreateUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']