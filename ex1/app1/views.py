from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    # posts = Post.objects.filter(published_time__lte=timezone.now()).order_by('-publised_time')
    posts = Post.objects.filter(title__contains='post').order_by('-published_time')
    return render(request, 'app1/post_list.html', {'post':posts})