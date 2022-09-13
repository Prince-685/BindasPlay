"""BindasPlay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import userview
from .import auto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',userview.Userview),

    path('displayresult/',userview.displayResult),
    path('saveresult/',userview.saveResult),
    path('searchAll/',userview.SearchAll),
    path('search/',userview.SearchByDate),
    path('',include('authentication.urls')),
    path('notification/',userview.Notification),
    path('addNotification/',userview.AddNotification),
    path('typeSubmit1/',auto.TypeSubmit1),
    path('typeSubmit2/',auto.TypeSubmit2),
    path('typeSubmit3/',auto.TypeSubmit3),
    
]
