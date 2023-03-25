"""admin URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home, name="home"),
    path('',views.signin, name="signin"),
    path('signup/',views.signup, name="signup"),
    path('signout/',views.signout, name="signout"),
    path('addstd/',views.add_std, name="add_std"),
    path('findstd/<str:params>/',views.find_std, name="find_std"),
    path('result/',views.result, name="result"),
    path('edit/<str:current_id>/',views.edit, name="edit"),
    path('delete/<str:current_id>/',views.delete, name="delete")


]
