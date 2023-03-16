

from comments.models import Comments
from projects.models import Image,Project

from rate.models import likes

from django import template

register = template.Library()


@register.simple_tag
def get_method(project):
    return Comments.get_project_number_of_comments(project)


@register.simple_tag
def get_user_react_on_project(project, user=''):
    queries = likes.get_user_reaction_on_proj(project)
    return queries.like if queries else False

@register.simple_tag
def get_project_images(project):
    queries = Image.objects.filter(project=project)
    return queries.image if queries else False
