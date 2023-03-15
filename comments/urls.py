
from django.urls import path
from .views import *

urlpatterns = [
    path('addComment/<int:id>', addComment, name="addComment"),
    path('addReply/<int:project_id>/<int:comment_id>', addReply, name="addReply")

]
