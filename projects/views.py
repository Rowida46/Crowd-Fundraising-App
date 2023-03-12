from comments.forms import CommentForm
from projects.models import Project
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .donation_forms import DonationForm
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm
from comments.models import Comments
# Create your views here.
from djmoney.money import Money


def donation(request):
    return render(request, "projects/index.html")


def submitDonation(request, id):
    # spesify on which project donation would be send
    project = Project.get_one_project(id)

    if request.method == "POST":
        donationForm = DonationForm(request.POST)
        if donationForm.is_valid():
            print(donationForm.cleaned_data["donation"])
            print("-----------------", project.total_donation)

            project.total_donation += Money(
                donationForm.cleaned_data["donation"], 'USD')
            print("-----------------", project.total_donation)
            project.save()
        # show donation upgrade
        return redirect("singledonation", id=id)


def donationlist(request):
    return render(request, "projects/listDonation.html")


def singledonation(request, id):
    project = Project.get_one_project(id)

    donationForm = DonationForm()
    commentForm = CommentForm()

    return render(request, "projects/singleDonation.html",
                  context={"donationForm": donationForm, "project": project,
                           "commentForm": commentForm
                           })


def newdonation(request):
    return render(request, "projects/newproject.html")


# ahmed ->

def single_project_view(request, id):
    project = Project.get_one_project(id)

    return

def projectslist(request):
    projects = Project.get_projects()
    
    return render(request, "projects/listProjects.html", {'projects': projects})





# @login_required
def newproject(request):
    if request.method == 'GET':
        newprojectform=NewProjectForm()
        return render(request, "projects/newproject.html",{'form':newprojectform,'title':'New Project',})
    elif request.method == 'POST':
        newprojectform=NewProjectForm(request.POST , request.FILES)
        if newprojectform.is_valid():
            print(request.POST)
            newprojectform.save()
            return redirect('/')
            # return redirect('singleproject',id=newprojectform.id)
    return render(request, "projects/newproject.html")


def projectdetail(request,id):
    project=get_object_or_404(Project,id=id)
    # comments=Comments.get_project_comments(id)
    return render(request, "projects/projectdetail.html",{'project':project})



# @login_required
def editproject(request,id):
    project=get_object_or_404(project,id=id)
    # project=get_object_or_404(project,id=id,created_by=request.user)
   
    if request.method == 'POST':
        newproject=NewProjectForm(request.POST , request.FILES, instance=project)
        if newproject.is_valid():
            print(request.POST)
            # newproject.save()
            return redirect('/')
            # return redirect('singleproject',id=newproject.id)
    elif request.method == 'GET':
        newproject=NewProjectForm(instance=project)

    return render(request, "projects/newproject.html",{
        'form':newproject,
        'title':'New Project',})


# @login_required
def deleteproject(request,id):
    project=get_object_or_404(project,id=id)
    # project=get_object_or_404(project,id=id, created_by=request.user)
    project.delete()
    return redirect('home')
