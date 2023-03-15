from comments.forms import CommentForm
from projects.models import Project, Donate
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .donation_forms import DonationForm
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm
from comments.models import Comments, Reply
# Create your views here.
from djmoney.money import Money

# get_project_comments


def donation(request):
    return render(request, "projects/index.html")


def submitDonation_dup(request, id):
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
    else:
        donationForm = donationForm()

    return redirect("singledonation", id=id)


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
            print("--------------newdonation---", newdonation)
            # newdonation.amount_of_donation = Money(
            #     donationForm.cleaned_data["donation"], 'USD')

            newdonation.save()
        # show donation upgrade
    else:
        donationForm = donationForm()

    return redirect("singledonation", id=id)


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

    print("---------donation total----------------------", project_total_donation)

    return render(request, "projects/projectdetail.html",
                  context={"donationForm": donationForm, "project": project,
                           "replyForm": replyForm,
                           # "comments_replys": comments_replys,
                           "replys": replys,
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

    return render(request, "projects/listProjects.html", {'projects': projects})


# @login_required
def newproject(request):
    if request.method == 'GET':
        newprojectform = NewProjectForm()
        return render(request, "projects/newproject.html", {'form': newprojectform, 'title': 'New Project', })
    elif request.method == 'POST':
        newprojectform = NewProjectForm(request.POST, request.FILES)
        if newprojectform.is_valid():
            print(request.POST)
            newprojectform.save()
            return redirect('/')
            # return redirect('singleproject',id=newprojectform.id)
    return render(request, "projects/newproject.html")

# @login_required


def editproject(request, id):
    project = get_object_or_404(project, id=id)
    # project=get_object_or_404(project,id=id,created_by=request.user)

    if request.method == 'POST':
        newproject = NewProjectForm(
            request.POST, request.FILES, instance=project)
        if newproject.is_valid():
            print(request.POST)
            # newproject.save()
            return redirect('/')
            # return redirect('singleproject',id=newproject.id)
    elif request.method == 'GET':
        newproject = NewProjectForm(instance=project)

    return render(request, "projects/newproject.html", {
        'form': newproject,
        'title': 'New Project', })


# @login_required
def deleteproject(request, id):
    project = get_object_or_404(project, id=id)
    project_total_donation = Donate.get_total_donation_for_project(project)
    total_target = project.target_budget

    print("------------------- target", total_target)
    print("------project_total_donation", project_total_donation)
    if project_total_donation > total_target:
        project.delete()
        return redirect('home')
    else:
        redirect("singledonation", id=id)
