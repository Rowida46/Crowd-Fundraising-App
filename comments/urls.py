
from django.urls import path
from .views import *

urlpatterns = [
    path('addComment/<int:id>', addComment, name="addComment")

]
