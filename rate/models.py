from django.db import models

# Create your models here.

class Rating(models.Model):
    #user_id =  models.ForeignKey(user, on_delete=models.CASCADE,
    #                        related_name='project_rate' , )