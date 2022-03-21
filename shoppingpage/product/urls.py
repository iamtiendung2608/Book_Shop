from django.urls import path
from .views import homepage, details
urlpatterns = [
    path('', homepage,name='homepage'),
    path('product/<int:id>',details,name='details')
]