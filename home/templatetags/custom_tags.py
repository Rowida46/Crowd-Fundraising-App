

from comments.models import Comments

from django import template

register = template.Library()


@register.simple_tag
def get_method(project):
    return Comments.get_project_number_of_comments(project)
