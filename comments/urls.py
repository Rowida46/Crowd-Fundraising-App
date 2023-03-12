
from django.urls import path
from .views import *

urlpatterns = [
    path('addCommit/<int:id>', addComment, name="addComment")

]
