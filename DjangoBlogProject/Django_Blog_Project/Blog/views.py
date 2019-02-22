from django.shortcuts import render

# List of Dictionaries below
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2019'
    }
]


def home (request):
    # Here we set a dictionary called context
    # the 'posts' key variable is accessible within our 
    # home.html template
    # the corresponding value for the dict is the posts list of dicts
    # which we defined above
    context = {
        'posts': posts
    }
    return render(request, 'Blog/home.html', context)
    

def about (request):
    return render(request, 'Blog/about.html')
   




