from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    latest_posts_list = Post.objects.order_by('-published_date')
    out = ', '.join([q.title for q in latest_posts_list])
    return HttpResponse(out)

def post_info(request, post_id):
    response = "This is post %s." % post_id
    return HttpResponse(response)


def comments_view(requiest, post_id):
    response = "You're looking for comments below post %s" % post_id
    return HttpResponse(response)
