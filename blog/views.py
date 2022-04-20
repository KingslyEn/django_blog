from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'KingslyEn',
        'title': 'First Post 9898',
        'content': 'Hey there, this is the first static post.',
        'date_posted': '24 October 2021'
    },
    {
        'author': 'Rj009',
        'title': 'Sec one fro RJ',
        'content': 'Yo yo, and the is the sec one from rj.',
        'date_posted': '1 July 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About page'})
