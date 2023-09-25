from django.urls import path
from . import views, Contact

urlpatterns = [
        # path('', views.DomainName, name='DomainName'),
        # path('nameserver', views.DomainNameserver, name='DomainNameserver'),
        # path('nameserver-confirm', views.NameserverConfirm, name= 'NameserverConfirm'),
        path('dns-args', views.DnsArgs, name='DnsArgs'),
        path('<str:args>/settings/', views.DnsSettings, name='DnsSettings'),
        path('auto-renew', views.DnsAutoRenew, name='DnsAutoRenew'),
        path('addson', views.DnsAddson, name='DnsAddson'),
        path('dns-management', views.DnsManagement, name='DnsManagement'),
        path('dns-record', views.DnsMangementRecord, name='DnsManRecord'),
        path('dns-delete-record', views.DnsDeleteRecord, name='DnsDeleteRecord'),
        path('dns-email-forward', views.DnsEmailForwards, name='DnsEmailForward'),
        path('dns-email-save', views.DnsEmailForwardsSave, name='DnsEmailForwardSave'),
        path('dns-id-pro', views.DnsIdPro, name='DnsIdPro'),
        path('<str:args>/dns-private-nameserver/', views.PrivateNameserver, name='DnsPrivateNameserver'),
        path('<str:args>/dns-private-nameserver-register/', views.RegisterPrivateNameserver, name='RegisterPrivateNameserver'),
        path('<str:args>/modify-private-nameserver/', views.ModifyPrivateNameserver, name='ModifyPrivateNameserver'),
        path('<str:args>/private-name-server-remove/', views.DeletePrivateNameserver, name='DeletePrivateNameserver'),

        path('<str:args>/contact-information', Contact.ContactInformation, name='ContactInformation'),
        path('<str:dnsname>/whois-information-update', Contact.wiupdate, name='wiupdate'),
        path('<str:dnsname>/admin-information-update', Contact.aiupdate, name='aiupdate'),
        path('transfer-domain', Contact.TransferView, name='TransferView'),
        path('transfer-domain-name', Contact.TransferDomain, name='TransferDomainName')
]