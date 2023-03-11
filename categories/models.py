from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def total_subscribes(self):
        return self.subscribes.count()
    
    def __str__(self):
        return self.name
    
    @classmethod
    def get_categories(cls):
        return cls.objects.all()
    
