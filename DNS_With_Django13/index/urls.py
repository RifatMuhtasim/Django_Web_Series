from django.urls import path
from . import views
from .views import indexBlogBody
from .client_country import client_countries

urlpatterns = [
        path('', views.indexBlog , name='home'),
        # path('', client_countries.as_view() , name='home'),
        path('post/<str:slug>', indexBlogBody.as_view(), name= 'IndexBlogBody')
]