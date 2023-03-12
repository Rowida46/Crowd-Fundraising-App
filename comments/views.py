from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

# Create your views here.
from projects.models import Project
from comments.forms import CommentForm
from comments.models import Comments, Reply


def addComment(request, id):
    project = Project.get_one_project(id)

    if request.method == "POST":
        newCommentContent = CommentForm(request.POST)

        if newCommentContent.is_valid():
            print("-------------------------------",
                  newCommentContent.cleaned_data['comment_content'])

            newCommit = Comments(project=project,
                                 comment_content=newCommentContent.cleaned_data['comment_content'])
            newCommit.save()
            return redirect("singledonation", id=id)
