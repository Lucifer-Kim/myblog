from django.shortcuts import render
from django.utils import timezone
from .models import Post

def about(request):
    return render(request, 'blog/about.html', {})


def index(request):
    #posts = Post.objexts.filter(published_date__let=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {})
