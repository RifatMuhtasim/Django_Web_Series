from django.urls import path
from . import views

urlpatterns  = [ 
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/' , views.register, name='register'),
    path('logoutx', views.logoutx, name='logoutx')
]