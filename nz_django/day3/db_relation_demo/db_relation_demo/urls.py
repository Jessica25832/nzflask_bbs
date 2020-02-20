"""db_relation_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from cms import views

urlpatterns = [
    path('',views.index,name='index'),
    path('one_to_many/',views.one_to_many,name='one_to_many'),
    path('one_to_one/',views.one_to_one,name='one_to_one'),
    path('many_to_many/',views.many_to_many,name='many_to_many'),
]
