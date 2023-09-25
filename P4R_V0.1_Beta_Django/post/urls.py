from os import name
from django.urls import path
from . import views
from .views import PostCreateView, PostCreateViewM, PostListView, UserPostListView, PostDetailView, PostDeleteView, PostUpdateView, PostUpdateViewM

urlpatterns = [ 
    path('', PostListView.as_view(), name='post'),
    path('blog/<str:username>/', UserPostListView.as_view(), name='user-post'),
    path('user/<int:pk>/', PostDetailView.as_view(), name='user-detail-post'),
    path('new/', PostCreateView.as_view() , name='new-post'),
    path('start/', PostCreateViewM.as_view() , name='new-m-post'),
    path('user/<int:pk>/delete/', PostDeleteView.as_view(), name='user-delete-post'),
    path('user/<int:pk>/update/', PostUpdateView.as_view(), name='user-update-post'),
    path('user/<int:pk>/updatem/', PostUpdateViewM.as_view(), name='user-update-post-m'),
]