from django.urls import path
from . import views

urlpatterns = [
        path('dnsname/', views.UploadDataView, name='UploadDataView'),
        # path('<str:dnsname>/domain-register-information', views.UploadData, name='UploadData'),
        path('<str:dnsname>/dns-cart', views.UploadDnsInformation, name='UploadDnsInformation'),
        path('dns-buy', views.DnsIcann, name='DnsIcann'),
        path('<str:args>/wasi-congratulations/', views.DnsCon, name='DnsCon')
]