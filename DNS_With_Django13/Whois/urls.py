from django.urls import path
from . import views

urlpatterns = [
        path('', views.Whois, name='Whois'),
        path('dnsname', views.dnsname, name='dnsname'),
        # path('<str:args>', views.WhoisResult, name='WhoisResult'),
        path('<str:args>', views.WhoisResultUrl, name='WhoisResult'),
        # path('<str:args>', views.WhoisResultJs, name='WhoisResult'),
]