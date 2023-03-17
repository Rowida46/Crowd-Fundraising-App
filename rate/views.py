from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RateForm
from .models import Rating
# Create your views here.

from rate.models import ReportProject, likes


def reportProject(request,  project_id):
    project = Project.get_one_project(project_id)
    print("----------replay comment ----------", project)
    newReport = ReportProject(project=project)
    newReport.user = request.user
    newReport.save()
    return redirect("singleproject", id=project_id)


def toggle_like(request, project_id):
    project = Project.get_one_project(project_id)
    print("----------replay comment ----------", project)

    user_reaction = likes.get_user_reaction_on_proj(project)
    if user_reaction:
        print("------------------------------")
        isLike = user_reaction.like
        print("toggle_like", isLike)
        user_reaction.like = not isLike
        user_reaction.save()
    else:
        print("pp[p[]]")
        user_reaction = likes(project=project, like=True)
        # user_reaction.user = request.user
        user_reaction.save()
    print("------------islike ---------------", user_reaction)
    return redirect("/")


def toggle_like_project(request, project_id):
    project = Project.get_one_project(project_id)
    print("----------replay comment ----------", project)

    user_reaction = likes.get_user_reaction_on_proj(project)
    if user_reaction:
        print("------------------------------")
        isLike = user_reaction.like
        print("toggle_like", isLike)
        user_reaction.like = not isLike
        user_reaction.save()
    else:
        print("pp[p[]]")
        user_reaction = likes(project=project, like=True)
       # user_reaction.user = request.user
        user_reaction.save()
    print("------------islike ---------------", user_reaction)
    return redirect("singleproject", id=project_id)


@login_required
def rate_project(request, id):
    # Get the project object that is being rated
    project = get_object_or_404(Project, id=id)

    if request.method == 'POST':
        # Create a new rate object using the submitted form data
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            # rate.user = request.user
            rate.project = project
            rate.save()
            messages.success(request, 'Thanks for rating this project!')
            return redirect('project_detail', project_id=project.id)
    else:
        # Display a form for the user to rate the project
        form = RateForm()

    return render(request, 'rate_project.html', {'form': form, 'project': project})