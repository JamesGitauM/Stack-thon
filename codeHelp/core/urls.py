# from django import views
from .import views
from .views import *
from django.urls import path, include

urlpatterns = [
    path('',views.index,name='index')]