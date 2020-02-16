from django import template

register = template.Library()


@register.filter
def is_like_user(post, user):
    return post.is_like_user(user)
