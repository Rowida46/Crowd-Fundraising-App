from tags.models import Tags
from django.shortcuts import render, reverse, redirect, HttpResponse, get_object_or_404

# Create your views here.


def filter_Projects_by_tag(request, tag_id):
    category = Tags.get_spesific_tag(tag_id)

    return redirect(reverse('home') + f"?tag_id={tag_id}")
