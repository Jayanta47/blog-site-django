from django.shortcuts import render
from datetime import datetime
from blog.models import Post
# Create your views here.

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def home(request):
    date = calender_today()
    posts = Post.objects.all()
    return render(request, 'Blog/home.html', {'posts': posts, 'title': 'Blog', 'date': date})


def about(request):
    date = calender_today()
    return render(request, 'Blog/about.html', {'title': 'About', 'date': date})


def calender_today():
    date = datetime.today()
    date = str(date).split()[0] + " - " + weekdays[date.weekday()]
    return date
