import datetime
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

# Create your views here.

from projects.models import Project, Image
from comments.models import Comments

from categories.models import Categories
from tags.models import Tags


def home(request):
    print("inside home")
    recently_creatd_projects = Project.get_recently_created_projects()
    projs_by_cat,  projs_by_tag = [], []
    categories = Categories.get_categories()
    images = Image.objects.all()

    if "category_id" in request.GET:
        category_id = request.GET['category_id']

        category = Categories.get_spesific_category(category_id)
        print("----------------inside query params ---------", category_id,
              '\n', category)

        projs_by_cat = Project.filter_projects_by_category(category)
        print("------projc by cat -----", projs_by_cat)

    if "tag_caption" in request.GET:
        tag_caption = request.GET['tag_caption']

        tag = Tags.get_spesific_tag(tag_caption)
        print("----------------inside query params(tag) ---------", tag_caption,
              '\n', tag)

        projs_by_tag = Project.filter_projects_by_tag(tag)
        print("------projc by cat -----", projs_by_tag)

    return render(request, "home/index.html",
                  context={"recently_creatd_projects": recently_creatd_projects,
                           "categories": categories,
                           "projs_by_cat": projs_by_cat,
                           "images": images,
                           "projs_by_tag": projs_by_tag
                           })


def notfound(request):
    return render(request, "error/notfound.html")


def becomevolunteer(request):
    return render(request, "becomeVoluenteer.html")


def approve_project(request, project_id):
    pass
