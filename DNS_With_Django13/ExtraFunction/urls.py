from django.urls import path

from .IpWithApi import IpWithApix
from . import views


urlpatterns = [ 
    path('function', views.ExtraFunction, name='ExtraFunction'),
    path('re-captcha', views.re_captcha, name='re_captcha'),
    path('country-tel', views.country_tel_no, name='country_tel_no'),
    path('email', views.email, name='email'),

    path('', IpWithApix.as_view(), name='IpWithApi'),
]