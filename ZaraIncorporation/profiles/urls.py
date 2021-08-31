from django.urls import path
from . import views

urlpatterns = [
        path('', views.profiles, name='profile'),
        path('update', views.UpdateProfile, name='UpdateProfile')
]