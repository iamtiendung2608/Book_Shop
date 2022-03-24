from django.urls import path
from .views import homepage, details, tagDetails,create
urlpatterns = [
    path('', homepage,name='homepage'),
    path('product/<int:id>',details,name='details'),
    path('tag/<int:id>',tagDetails,name='tag'),
    path('edit',create,name='create'),
]