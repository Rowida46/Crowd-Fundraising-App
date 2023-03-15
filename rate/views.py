from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from projects.models import Project
# Create your views here.

from rate.models import ReportProject


def reportProject(request,  project_id):
    project = Project.get_one_project(project_id)
    print("----------replay comment ----------", project)
    newReport = ReportProject(project=project)
    newReport.save()
    return redirect("singledonation", id=project_id)
