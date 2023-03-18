from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('filter_Projects_by_tag/<int:tag_id>', filter_Projects_by_tag,
         name="filter_Projects_by_tag"),
]
