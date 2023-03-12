from django.contrib import admin
from django.urls import path
from .views import home,notfound,becomevolunteer

urlpatterns = [
    path('', home, name="home"),
    path('volunteer', becomevolunteer, name="becomevolunteer"),
    path('notfound', notfound, name="notfound"),

]
