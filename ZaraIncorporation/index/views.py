from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import IndexBlog
from django.views.generic import DetailView

# Create your views here.
context = {'IndexBlogs': IndexBlog.objects.all() }

# def home(request):
#         return render(request, 'index.html')

def indexBlog(request):
        ordering= {'-time'}
        return render(request, 'index/IndexBlog.html', context)

class indexBlogBody(DetailView):
        model = IndexBlog
        template_name = 'index/IndexBlogBody.html'
