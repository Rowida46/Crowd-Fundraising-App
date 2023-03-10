from django.urls import path
from .views import donation,donationlist,singledonation,newdonation

urlpatterns = [
    path('donation', donation, name="donation"),
    path('donationlist', donationlist, name="donationlist"),
    path('singledonation', singledonation, name="singledonation"),
    path('newdonation', newdonation, name="newdonation"),

]
