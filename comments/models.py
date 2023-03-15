from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.shortcuts import reverse, get_object_or_404
from ckeditor.fields import RichTextField
from django_enum import EnumField

from projects.models import Project

# Create your models here.


class Comments(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='project_commit')

    created_at = models.DateTimeField(auto_now_add=True)
    comment_content = RichTextField(blank=True, null=True)

    def __str__(self):
        self.user = "rowida"
        return 'Comment by {} on {}'.format(self.user, self.project)

    @classmethod
    def get_project_comments(cls, project_id):
        # not sure yet ->>>
        return cls.objects.filter(project=project_id).order_by("-created_at")

    @classmethod
    def get_project_number_of_comments(self, project):
        return Comments.objects.filter(project=project).count()

    @classmethod
    def get_spesific_comment(cls, comment_id):
        try:
            return get_object_or_404(cls, pk=comment_id)
        except Exception as e:
            return None
    # @classmethod
    # def get_project_comments(self):
    #     return Comments.objects.filter(project=self)


class Reply(models.Model):
    reply_content = models.TextField()
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_reply")

    # user =  models.ForeignKey(user, on_delete=models.CASCADE,
    #                             related_name='user_reply')
    comment_id = models.ForeignKey(
        Comments, on_delete=models.CASCADE, related_name="comment_reply")

    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_comment_replys(cls, comment):
        return cls.objects.filter(comment_id=comment)

    @classmethod
    def get_project_replys(cls, project):
        return cls.objects.filter(project=project)


class ReportOption(models.TextChoices):
    VALUE0 = 'V0', 'in'
    VALUE1 = 'V1', 'Value 1'
    VALUE2 = 'V2', 'Value 2'


class ReportComment(models.Model):
    comment = models.ForeignKey(
        Comments, on_delete=models.CASCADE, related_name="report_comment")
    # user = models.ForeignKey(User, related_name="user_report")
    option = EnumField(ReportOption, null=True, blank=True)
