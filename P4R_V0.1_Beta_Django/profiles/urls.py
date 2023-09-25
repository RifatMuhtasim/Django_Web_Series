from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.profile, name='profile'),
    path('update', views.UpdateProfile, name='UpdateProfile'),
    path('contact-id', views.ContactId, name='ContactId')
]