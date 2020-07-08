from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from datetime import datetime
from blog.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def home(request):
    date = calender_today()
    posts = Post.objects.all()
    return render(request, 'Blog/home.html', {'posts': posts, 'title': 'Blog', 'date': date})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # enabling the author to be logged in user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # enabling the author to be logged in user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False


def about(request):
    date = calender_today()
    return render(request, 'Blog/about.html', {'title': 'About', 'date': date})


def calender_today():
    date = datetime.today()
    date = str(date).split()[0] + " - " + weekdays[date.weekday()]
    return date
