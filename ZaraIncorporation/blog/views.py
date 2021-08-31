from django.forms.models import fields_for_model
from django.shortcuts import render, redirect 
from .models import blog
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

context = {'blogs': blog.objects.all()}

class BlogListView(ListView):
        model= blog
        template_name = 'blog/blog.html'
        context_object_name = 'blogs'
        ordering= {'-time'}
        paginate_by = 2

class BlogDetailView(DetailView):
        model = blog
        template_name = 'blog/BlogDetail.html'
     

