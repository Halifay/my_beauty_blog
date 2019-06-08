from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.views import generic
from .models import Post, Comment


def index(request):
    return render(request, 'blog/index.html')


def post_info(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def leave_a_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        current_comment = Comment()
        current_comment.text = request.POST['comment_text']
        current_comment.post = post
    except (KeyError, Post.DoesNotExist):
        return render(request, 'blog/detail.html',
                      {'post': post,
                       'error_message': "There's error!(("})
    if not current_comment:
        return render(request, 'blog/detail.html',
                      {'post': post,
                       'error_message': "You're motherfucker."})
    else:
        current_comment.save()
        return HttpResponseRedirect(reverse('blog:post_info', args=[post_id]))

