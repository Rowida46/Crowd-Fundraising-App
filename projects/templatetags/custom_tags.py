

from comments.models import Comments

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
