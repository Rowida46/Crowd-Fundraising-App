import datetime
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

# Create your views here.

from projects.models import Project
from comments.models import Comments



def home(request):
    recently_creatd_projects = Project.get_recently_created_projects()
    # print("-----recently_creatd_projects------------", recently_creatd_projects)
    # project_comments_number = Comments.get_project_number_of_comments(project)
    comments_number = 90
    return render(request, "home/index.html",
                  context={"recently_creatd_projects": recently_creatd_projects,
                           "comments_number": comments_number
                           })


def notfound(request):
    return render(request, "error/notfound.html")


def becomevolunteer(request):
    return render(request, "becomeVoluenteer.html")
