from django.shortcuts import render, redirect, HttpResponse,get_object_or_404

# Create your views here.


def donation(request):
    return render(request, "projects/index.html")
def donationlist(request):
    return render(request, "projects/listDonation.html")

def singledonation(request):
    return render(request, "projects/singleDonation.html")

def newdonation(request):
    return render(request, "projects/newDonation.html")