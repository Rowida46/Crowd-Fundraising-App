from django.db import models
from projects.models import Project
from django_enum import EnumField

# Create your models here.


class Rating(models.Model):
    # user_id =  models.ForeignKey(user, on_delete=models.CASCADE,
    #                        related_name='user_rate_on_project'  )

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_rate")

    rate = models.DecimalField(max_digits=5, decimal_places=2)


class ReportOption(models.TextChoices):
    VALUE0 = 'V0', 'in'
    VALUE1 = 'V1', 'Value 1'
    VALUE2 = 'V2', 'Value 2'


class ReportProject(models.Model):
    project = models.ForeignKey(Project, related_name="report_project")
    # user = models.ForeignKey(User, related_name="user_report")
    option = EnumField(ReportOption, null=True, blank=True)

# register like in admin ->>>>


class likes(models.Model):
    # user = models.ForeignKey(User, related_name="user_report")
    like = models.BooleanField(default=False)
