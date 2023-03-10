from django.shortcuts import render, redirect, HttpResponse,get_object_or_404

# Create your views here.


def home(request):
    return render(request, "home/index.html")
def notfound(request):
    return render(request, "error/notfound.html")
def becomevolunteer(request):
    return render(request, "becomeVoluenteer.html")
