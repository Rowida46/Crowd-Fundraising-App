from comments.forms import CommentForm
from projects.models import Project,Image
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .donation_forms import DonationForm
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm,Project_Image_Form
from comments.models import Comments
from json import dumps
from django.core.files.storage import FileSystemStorage
# Create your views here.
from djmoney.money import Money


from django.contrib import messages

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
        return redirect("singleproject", id=id)


def donationlist(request):
    return render(request, "projects/listDonation.html")


def singledonation(request, id):
    project = Project.get_one_project(id)
    images=Image.objects.all()
    print("--------------------",images)
    donationForm = DonationForm()
    commentForm = CommentForm()
    context={"donationForm": donationForm, "project": project,"commentForm": commentForm,'images':images
                           }
    return render(request, "projects/projectdetail.html",context)


def newdonation(request):
    return render(request, "projects/newproject.html")


# ahmed ->

def single_project_view(request, id):
    project = Project.get_one_project(id)

    return


def projectslist(request):
    projects = Project.get_projects()
    images=Image.objects.all()
    return render(request, "projects/listProjects.html", {'projects': projects,'images':images})


# @login_required

def newproject(request):
    if request.method == 'POST':
        # Get the form data from the POST request
        project_form = NewProjectForm(request.POST)
        image_form = Project_Image_Form(request.POST, request.FILES)
        print(request.FILES)
        # if project_form.is_valid() and image_form.is_valid():
            # Create a new Project object with the form data
        project = project_form.save(commit=False)
        # project.created_by=request.user

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



# @login_required
def editproject(request, id):
    project = get_object_or_404(Project, id=id)
    images=Image.objects.all().filter(project=project)
    print(images)
    # project=get_object_or_404(project,id=id,created_by=request.user)
    if request.method == 'POST':
        newproject = NewProjectForm(
            request.POST, request.FILES, instance=project)
        image_form = Project_Image_Form(request.POST, request.FILES, instance=project)
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
        images=Image.objects.all().filter(project=project)
        images.delete()
        context = {
        'project_form': project_form,
        'title': 'Edit Project'
    }
    return render(request, "projects/newproject.html",context)


# @login_required
def deleteproject(request, id):
    project = get_object_or_404(Project, id=id)
    # project=get_object_or_404(project,id=id, created_by=request.user)
    project.delete()
    return redirect('projectslist')
