from tags.models import Tags
from django.shortcuts import render, reverse, redirect, HttpResponse, get_object_or_404

# Create your views here.


def filter_Projects_by_tag(request, tag):
    tags = Tags.get_spesific_tag(tag)

    return redirect(reverse('home') + f"?tag={tag}")


# def lst_projects_by_tags(request , ):
