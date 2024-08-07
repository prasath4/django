from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
posts=[
    {
        'creater': 'Prasath B',
        'title' : 'portfolio',
        'date_posted': 'August 05, 2024'
    }
]

def index(request):
    context={
        'posts': posts
    }
    return render(request, 'polls/index.html', context)

def about(request):
    return render(request, 'polls/about.html', {'title': 'About'})