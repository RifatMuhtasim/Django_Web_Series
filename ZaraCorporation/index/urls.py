from django.urls import path
from . import views
from .views import indexBlogBody

urlpatterns = [
        path('', views.indexBlog , name='home'),
        path('post/<str:slug>/', indexBlogBody.as_view(), name= 'IndexBlogBody')
]