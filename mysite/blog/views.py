from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Post, Comment


def index(request):
    latest_posts_list = Post.objects.order_by('-published_date')
    context = {'latest_posts_list': latest_posts_list, }
    return render(request, 'blog/index.html', context)


def post_info(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def comments_view(requiest, post_id):
    response = "You're looking for comments below post %s" % post_id
    return HttpResponse(response)
