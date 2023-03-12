from django.urls import path
from .views import donation, donationlist, singledonation, newdonation, addComment, submitDonation

urlpatterns = [
    path('donation', donation, name="donation"),
    path('donationlist', donationlist, name="donationlist"),
    path('singledonation/<int:id>', singledonation, name="singledonation"),
    path('newdonation', newdonation, name="newdonation"),
    path('donate/<int:id>', submitDonation, name="submit_donation"),
    path('commit', addComment, name="comment")


]
