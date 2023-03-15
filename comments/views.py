from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

# Create your views here.
from projects.models import Project
from comments.forms import CommentForm
from comments.models import Comments, Reply

from django.shortcuts import reverse, get_object_or_404


def addComment(request, id):
    project = Project.get_one_project(id)

    if request.method == "POST":
        newCommentContent = CommentForm(request.POST)

        if newCommentContent.is_valid():
            # print("-------------------------------",
            #       newCommentContent.cleaned_data['comment_content'])

            newCommit = Comments(project=project,
                                 comment_content=newCommentContent.cleaned_data['comment_content'])
            newCommit.save()
            return redirect("singledonation", id=id)
        else:
            commentForm = CommentForm()

        # return redirect(reverse("singledonation"), id=id,  kwargs={"id": id, 'form': form})
        return redirect("singledonation", id=id)


def addReply(request, project_id, comment_id):
    project = Project.get_one_project(project_id)
    comment = Comments.get_spesific_comment(comment_id)

    print("reply proj ---------", project)
    print("reply comment ---------", comment)

    if request.method == "POST":
        newReplyContent = CommentForm(request.POST)

        if newReplyContent.is_valid():
            # print("-------------------------------",
            #       newCommentContent.cleaned_data['comment_content'])

            newReply = Reply(comment_id=comment, project=project,
                             reply_content=newReplyContent.cleaned_data['comment_content'])
            newReply.save()
            return redirect("singledonation", id=project_id)
        else:
            commentForm = CommentForm()

        # return redirect(reverse("singledonation"), id=id,  kwargs={"id": id, 'form': form})
        return redirect("singledonation", id=id)
