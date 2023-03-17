from re import sub
from decimal import Decimal
from comments.forms import CommentForm
from projects.models import Project, Donate, Image
from .donation_forms import DonationForm
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm
from comments.models import Comments, Reply
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .donation_forms import DonationForm
from .forms import NewProjectForm, Project_Image_Form
from django.core.files.storage import FileSystemStorage
# Create your views here.
from djmoney.money import Money

# get_project_comments


from django.contrib import messages


def donation(request):
    return render(request, "projects/index.html")


@login_required
def submitDonation_dup(request, id):
    # spesify on which project donation would be send
    project = Project.get_one_project(id)

    if request.method == "POST":
        donationForm = DonationForm(request.POST)
        donation.user = request.user
        if donationForm.is_valid():
            print(donationForm.cleaned_data["donation"])
            print("-----------------", project.total_donation)

            project.total_donation += Money(
                donationForm.cleaned_data["donation"], 'USD')
            print("-----------------", project.total_donation)
            project.save()
        # show donation upgrade
    else:
        donationForm = donationForm()

    return redirect("singleproject", id=id)


def submitDonation(request, id):
    # spesify on which project donation would be send
    project = Project.get_one_project(id)

    if request.method == "POST":
        donationForm = DonationForm(request.POST)
        if donationForm.is_valid():
            amount = Money(
                donationForm.cleaned_data["donation"], 'USD')

            # print(donationForm.cleaned_data["donation"])
            print("-----------------", amount)

            # project.total_donation += Money(
            #     donationForm.cleaned_data["donation"], 'USD')
            # print("-----------------", project.total_donation)

            newdonation = Donate(project=project, amount_of_donation=amount)
            newdonation.user = request.user
            print("--------------newdonation---", newdonation)
            # newdonation.amount_of_donation = Money(
            #     donationForm.cleaned_data["donation"], 'USD')

            newdonation.save()
        # show donation upgrade
    else:
        donationForm = donationForm()

    return redirect("singleproject", id=id)


def donationlist(request):
    return render(request, "projects/listDonation.html")


def singledonation(request, id):
    project = Project.get_one_project(id)
    project_comments = Comments.get_project_comments(project)
    # project_replys = Reply.get_comment_replys(project_comments)
    replys = Reply.get_project_replys(project)
    # calcualations
    project_comments_number = Comments.get_project_number_of_comments(project)
    project_total_donation = Donate.get_total_donation_for_project(project)

    # forms
    donationForm = DonationForm()
    commentForm = CommentForm()
    replyForm = CommentForm()

    images = Image.objects.all()

    print("---------donation total----------------------", project_total_donation)

    return render(request, "projects/projectdetail.html",
                  context={"donationForm": donationForm, "project": project,
                           "replyForm": replyForm,
                           # "comments_replys": comments_replys,
                           "replys": replys, 'images': images,
                           "project_comments_number": project_comments_number,
                           "project_total_donation": project_total_donation if project_total_donation else 0,
                           "commentForm": commentForm, "project_comments": project_comments
                           })


def newdonation(request):
    return render(request, "projects/newproject.html")


# ahmed ->

def single_project_view(request, id):
    project = Project.get_one_project(id)

    return


def projectslist(request):
    projects = Project.get_projects()
    images = Image.objects.all()
    return render(request, "projects/listProjects.html", {'projects': projects, 'images': images})


# @login_required
def newproject(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            print("------------USER------------------------------", request.user)
            # Get the form data from the POST request
            project_form = NewProjectForm(request.POST)
            image_form = Project_Image_Form(request.POST, request.FILES)

            print(request.FILES)
            print("------------type--------------", type(request.user))

            # if project_form.is_valid() and image_form.is_valid():
            # Create a new Project object with the form data
            project = project_form.save(commit=False)
            project.user = request.user
            project.save()

            # Get the uploaded images and create an Image object for each one
            for image in request.FILES.keys():
                image_file = request.FILES.getlist(image)
                for i in image_file:
                    fs = FileSystemStorage()
                    filename = fs.save('images/projects/' + i.name, i)
                    img = Image()
                    img.image = filename
                    img.project = project
                    img.save()

            # Redirect to the detail view of the new project
            return redirect('singleproject', id=project.id)
        else:
            project_form = NewProjectForm()
            image_form = Project_Image_Form()

        context = {
            'project_form': project_form,
            'image_form': image_form,
            'title': 'New Project'
        }

        return render(request, 'projects/newproject.html', context)

    else:
        return redirect("login")


@login_required
def deleteproject(request, id):
    project = get_object_or_404(Project, id=id)
    project_total_donation = Donate.get_total_donation_for_project(project)
    total_target = project.target_budget

    print("------------------- target", total_target.amount)
    print("------project_total_donation", project_total_donation)

    if project_total_donation > total_target.amount:
        project.delete()
        return redirect('home')

    print("--------not valid -----------")
    return redirect("singleproject", id=id)


@login_required
def editproject(request, id):
    project = get_object_or_404(Project, id=id)
    images = Image.objects.all().filter(project=project)
    print(images)
    # project=get_object_or_404(project,id=id,created_by=request.user)
    if request.method == 'POST':
        newproject = NewProjectForm(
            request.POST, request.FILES, instance=project)
        image_form = Project_Image_Form(
            request.POST, request.FILES, instance=project)
        if newproject.is_valid():
            print(request.POST)
            newproject.save()
            # Get the uploaded images and create an Image object for each one
        for image in request.FILES.keys():
            image_file = request.FILES.getlist(image)
            for i in image_file:
                fs = FileSystemStorage()
                filename = fs.save('images/projects/' + i.name, i)
                img = Image()
                img.image = filename
                img.project = project
                img.save()
            return redirect('singleproject', id=project.id)
    elif request.method == 'GET':
        project_form = NewProjectForm(instance=project)
        images = Image.objects.all().filter(project=project)
        images.delete()
        context = {
            'project_form': project_form,
            'title': 'Edit Project'
        }
    return render(request, "projects/newproject.html", context)
