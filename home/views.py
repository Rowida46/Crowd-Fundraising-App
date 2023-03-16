import datetime
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

# Create your views here.

from projects.models import Project
from comments.models import Comments

from categories.models import Categories


def home(request):
    print("inside home")
    recently_creatd_projects = Project.get_recently_created_projects()
    lst_nombers = []
    for proj in recently_creatd_projects:
        number_of_comments = Comments.objects.filter(project=proj).count()
        lst_nombers.append(number_of_comments)
        print(f"---------{proj.id}---------------", number_of_comments)

    return render(request, "home/index.html",
                  context={"recently_creatd_projects": recently_creatd_projects,

                           })


def notfound(request):
    return render(request, "error/notfound.html")


def becomevolunteer(request):
    return render(request, "becomeVoluenteer.html")
