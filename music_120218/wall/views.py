from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.urls import reverse

from wall.models import Post, Repost


def wall(request, user_id):
    posts = Post.objects.filter(user_id=user_id).order_by("-date")
    return render(request, "wall/wall.html", {"posts": posts})

@login_required
def make_repost(request, post_id):
    if request.method == 'POST':
        new_post = Post()
        origin = Post.objects.get(pk=post_id)
        new_post.user_id = request.user.id
        new_post.text = 'RT "%s"' % origin.text
        new_post.save()
        repost = Repost()
        repost.text = new_post.text
        repost.source_id = post_id
        repost.destination_id = new_post.id
        repost.save()
        return HttpResponseRedirect(reverse("wall", args=(request.user.id,)))

@login_required
def add_like(request, post_id):
    if post_id in request.COOKIES:
        return HttpResponseRedirect(reverse("wall", args=(request.user.id,)))
    else:

        post = Post.objects.get(pk=post_id)

        repost = Repost.objects.filter(destination_id=post_id)
        if repost:
            origin = Post.objects.get(pk=repost[0].source.id)
            origin.likes += 1

        post.likes += 1
        post.save()
        response = HttpResponseRedirect(reverse("wall", args=(request.user.id,)))
        response.set_cookie(post_id, "like")
        return response


