
from django.urls import path
from .views import *

urlpatterns = [
    path('reportProject/<int:project_id>', reportProject, name="reportProject"),


]
