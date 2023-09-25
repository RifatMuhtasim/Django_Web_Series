from django.urls import path 
from . import views, Reviews
from .DnsRecord import views as drv

urlpatterns = [ 
        path('domain-name-list', views.domain_name_list, name='DomainName'),

        path('nameserver', Reviews.DomainNameserver, name='DomainNameserver'),
        path('nameserver-confirm', Reviews.ReNameServerChange, name= 'NameserverConfirm'),
        path('<str:args>/privacy-protection/', Reviews.re_privacy_protection, name='re_privacy_protection'),
        path('<str:args>/domain-secret-key', Reviews.domain_secret_key, name='domain_secret_key'),
        path('<str:args>/domain-theft-protectionx/', Reviews.domain_theft_protectionx, name='domain_theft_protectionx'),
        path('<str:args>/delete-domain-name', Reviews.delete_domain_name, name='delete_domain_name'),
        path('<str:args>/delete-confirm', Reviews.delete_confirm , name='delete_confirm'),

        path('<str:args>/domain-name-contact-information', views.domain_name_contact_information, name = 'domain_name_contact_information'),
        path('<str:args>/domain-forward', views.domain_forward, name = 'domain_forward'),
        path('<str:DomainName>/add-domain-forward', views.add_domain_forward, name='add_domain_forward'),
        path('<str:DomainName>/disable-domain-forward', views.disable_forward, name='disable_forward'),

        path('<str:args>/dns-record/', drv.DnsRecord, name='DnsRecord'),
        path('<str:DomainName>/dns-record/a-ipv4', drv.ARecord, name='ARecords'),
        path('<str:DomainName>/dns-record/delete-a-ipv4', drv.DeleteARecord, name='DeleteARecord'),
        path('<str:DomainName>/dns-record/modify-a-ipv4', drv.ModifyARecord, name='ModifyARecord'),
]