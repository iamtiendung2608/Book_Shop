from django.urls import path
from .views import homepage, details, tagDetails,create,loginPage,registerPage,logoutUser
urlpatterns = [
    path('', homepage,name='homepage'),
    path('product/<int:id>',details,name='details'),
    path('tag/<int:id>',tagDetails,name='tag'),
    path('edit',create,name='create'),
    path('login',loginPage,name='login'),
    path('regist',registerPage,name='regist'),
    path('logout',logoutUser,name='logout'),

]