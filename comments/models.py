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
        return cls.objects.filter(project=project_id)  # not sure yet ->>>

    # @classmethod
    # def get_project_number_of_comments(self):
    #     return Comments.objects.filter(project=self).count()

    # @classmethod
    # def get_project_comments(self):
    #     return Comments.objects.filter(project=self)


class Reply(models.Model):
    reply_content = models.TextField()

    # user =  models.ForeignKey(user, on_delete=models.CASCADE,
    #                             related_name='user_commit')
    comment_id = models.ForeignKey(Comments, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ReportOption(models.TextChoices):
    VALUE0 = 'V0', 'in'
    VALUE1 = 'V1', 'Value 1'
    VALUE2 = 'V2', 'Value 2'


class ReportComment(models.Model):
    comment = models.ForeignKey(
        Comments, on_delete=models.CASCADE, related_name="report_comment")
    # user = models.ForeignKey(User, related_name="user_report")
    option = EnumField(ReportOption, null=True, blank=True)
