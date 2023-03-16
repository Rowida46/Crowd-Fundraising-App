from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def total_subscribes(self):
        return self.subscribes.count()

    @classmethod
    def get_categories(cls):
        return cls.objects.all()

    @classmethod
    def get_spesific_category(cls, cat_id):
        return cls.objects.filter(id=cat_id)
