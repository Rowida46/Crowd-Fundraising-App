from projects.models import Project
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .donation_forms import DonationForm
# Create your views here.
from djmoney.money import Money


def donation(request):
    return render(request, "projects/index.html")


def submitDonation(request, id):
    project = Project.get_one_project(id)
    print("-------------------------", project)

    if request.method == "POST":
        donationForm = DonationForm(request.POST)
        if donationForm.is_valid():
            print(donationForm.cleaned_data["donation"])
            print("-----------------", project.total_donation)

            project.total_donation += Money(
                donationForm.cleaned_data["donation"], 'USD')
            print("-----------------", project.total_donation)
            project.save()

        return redirect("singledonation" , id = id)


def addComment(request, projectid=""):
    pass


def donationlist(request):
    return render(request, "projects/listDonation.html")


def singledonation(request, id):
    donationForm = DonationForm()
    project = Project.get_one_project(id)
    return render(request, "projects/singleDonation.html",
                  context={"donationForm": donationForm, "project": project})


def newdonation(request):
    return render(request, "projects/newDonation.html")


# ahmed ->

def single_project_view(request, id):
    project = Project.get_one_project(id)

    return
