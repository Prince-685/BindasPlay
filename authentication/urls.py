<<<<<<< HEAD
from django.contrib import admin
from django.urls import path
from . import views
from . import admin
urlpatterns = [
     path('userlogin/',views.userLogin),
     path('adminlogin/',admin.adminLogin),
     path('updatePassword/',admin.updatePassword),
     path('adduserPage/',admin.AddUserPage),
     path('addUser/',admin.AddUser),
=======
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
     path('login',views.login),
>>>>>>> bef1a1313f76ef3f7c82ced7344ab96c8179d76c
]