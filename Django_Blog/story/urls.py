from django.urls import path
from . import views
from .views import StoryPostList , StoryPostDetail, StoryPostAuthor

urlpatterns = [ 
    path('', StoryPostList.as_view() , name='story'),
    path('<int:pk>/', StoryPostDetail.as_view(), name='storydetail'),
    path('refugee/<str:username>/', StoryPostAuthor.as_view(), name= 'storyauthor')
]