from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from projects.models import Project
# Create your views here.

from rate.models import ReportProject, likes


def reportProject(request,  project_id):
    project = Project.get_one_project(project_id)
    print("----------replay comment ----------", project)
    newReport = ReportProject(project=project)
    newReport.save()
    return redirect("singledonation", id=project_id)


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
        user_reaction.save()
    print("------------islike ---------------", user_reaction)
    return redirect("singledonation", id=project_id)
