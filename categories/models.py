from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    #supdated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_categories(cls):
        return cls.query.all()
    
