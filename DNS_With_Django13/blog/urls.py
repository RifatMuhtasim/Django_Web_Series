from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView

urlpatterns = [
        path('', BlogListView.as_view(), name='blog'),
        path('<str:slug>', BlogDetailView.as_view(), name= 'BlogDetail'),
        path('search-content/', views.SearchBlog, name='SearchBlog')
]