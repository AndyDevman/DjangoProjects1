from django.shortcuts import render
from .models import Post

def home(request):
    #defining context dict - 'posts' key holds list of dicts defined above
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Blog/home.html', context)


def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})


