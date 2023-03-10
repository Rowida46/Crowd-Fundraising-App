from django.db import models
from projects.models import Project
# Create your models here.


class Comments(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE,
                                 related_name='project_comment')
    # user_id
    comment_content =  models.TextField(null=True, blank=True)