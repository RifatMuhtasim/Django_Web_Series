# from django.db.models import fields
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import StartPost
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, UpdateView
# Create your views here.

context = {'StartPosts': StartPost.objects.all()}

class PostCreateViewM(LoginRequiredMixin, CreateView):
    model = StartPost
    template_name= 'post/PostCreateViewM.html'
    fields = ['Title', 'Body', 'Image']

    def form_valid(self, form):
        form.instance.StartPostAuthor = self.request.user
        return super().form_valid(form)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = StartPost
    fields = ['Title', 'Body', 'Image']

    def form_valid(self, form):
        form.instance.StartPostAuthor = self.request.user
        return super().form_valid(form)

class PostListView(ListView):
    model = StartPost 
    template_name= 'post/postlist.html'
    context_object_name= 'StartPosts'
    ordering = ['-StartPostTime']
    paginate_by= 5

class PostDetailView(DetailView):
    model = StartPost

class UserPostListView(ListView):
    model = StartPost 
    template_name= 'post/userpost.html'
    context_object_name= 'StartPosts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username= self.kwargs.get('username'))
        return StartPost.objects.filter(StartPostAuthor=user).order_by('-StartPostTime')

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = StartPost
    template_name = 'post/updatepost.html'
    fields = ['Title', 'Body', 'Image']

    def form_valid(self, form):
        form.instance.StartPostAuthor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.StartPostAuthor:
            return True
        return False

class PostUpdateViewM(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = StartPost
    template_name = 'post/updatepostm.html'
    fields = ['Title', 'Body', 'Image']

    def form_valid(self, form):
        form.instance.StartPostAuthor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.StartPostAuthor:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = StartPost
    template_name= 'post/deletepost.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.StartPostAuthor:
            return True
        return False


