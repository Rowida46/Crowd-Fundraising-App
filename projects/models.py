from django_enum import EnumField
from django.db import models
from django.shortcuts import reverse, get_object_or_404
from django.contrib.postgres.fields import ArrayField
from categories.models import Categories
# from comments.models import Comments
from django.db.models import Avg
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator

# Create your models here.

from djmoney.models.fields import MoneyField
from django.utils.text import slugify
from tags.models import Tags

# from rate.models import Rating, ReportOption
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default="", null=True, blank=True)
    details = models.TextField(null=True, blank=True)
<<<<<<< HEAD
    image = ArrayField(models.ImageField(
        upload_to='projects/images') ,  blank=True)
=======
    image = models.ImageField(
        upload_to='projects/images')
>>>>>>> 1cf3a5f (merge)

    features = ArrayField(
        models.CharField(max_length=100)
    )

    # avg_rate = models.DecimalField(
    #     max_digits=5, decimal_places=2, null=True, blank=True)

    target_budget = MoneyField(max_digits=14, decimal_places=2,
                               default_currency='USD', default=0, null=False,
                               validators=[
                                   MinMoneyValidator(10),
                                   MaxMoneyValidator(1500)]
                               )

    total_donation = MoneyField(max_digits=14, decimal_places=2,
                                default_currency='USD', default=0)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    start_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    # required -> to spesify end date
    end_at = models.DateTimeField(null=True)

    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True,
                                 related_name='project_category', blank=True)
    # tags
    tags = models.ManyToManyField(Tags, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # def get_project_avg_rate(self, id):
    #     rate_lst = Rating.objects.filter(
    #         project=self)

    #     avg = round(rate_lst.aggregate(Avg("rate"))["rate__avg"], 2)
    #     return avg

    # @classmethod
    # def get_project_number_of_reports(self):
    #     return ReportOption.objects.filter(project=self).count()

    # @classmethod
    # def get_project_comments(self):
    #     return Comments.objects.filter(project=self)

    @classmethod
    def get_projects(cls):
        return cls.objects.all()

    @classmethod
    def get_one_project(cls, id):
        try:
            return get_object_or_404(cls, pk=id)
        except Exception as e:
            return None

    @classmethod
    def filter_projects_by_title(cls, title):
        try:
            res = cls.objects.filter(title__contains=title)
            return res
        except Exception as e:
            return None

    @classmethod
    def filter_projects_by_category(cls, category):
        try:
            res = cls.objects.filter(project_category__contains=category)
            return res
        except Exception as e:
            return None

    @classmethod
    def filter_projects_by_slug(cls, slug):
        try:
            res = cls.objects.filter(slug__contains=slug)
            return res
        except Exception as e:
            return None

    @classmethod
    def get_top_rated_projects(cls):
        # dsc order
        top_rated = cls.objects.order_by("-rate")
        return top_rated

    @classmethod
    def get_recently_created_projects(cls):
        # dsc order
        res = cls.objects.order_by("-created_at")
        return res

    # instead of using urls ->>>
    # note -> fill in ur reverse usedurl

    def get_spefic_project(self):
        try:
            return reverse('', args={self.id})
        except Exception as e:
            return None

    def get_title(self):
        return self.title

    def get_delete_url(self):
        return reverse('', args={self.id})

    def get_edit_url(self):
        return reverse('', args={self.id})

    def get_spefic_project_by_slug(self):

        try:
            return reverse('', args={self.slug})
        except Exception as e:
            return None
