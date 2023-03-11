from django.db import models

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name