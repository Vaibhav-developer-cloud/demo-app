from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('hello/',views.hello,name="hello"),

    path('calculate/', views.calculate,name="cal"),

    path('index/',views.index,name="indexing page")
]