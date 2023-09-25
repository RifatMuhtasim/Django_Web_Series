from DnsSystem.views import DnsIdPro
from django.contrib import admin
from .models import DnsServer, DnsEmailForward, DnsIdPros, DnsRegisterPrivateNameserver
from .ContactModel import WhoisInformation, AdminInformation, TransferDomainUs
# Register your models here.

admin.site.register(TransferDomainUs),
admin.site.register(WhoisInformation),
admin.site.register(AdminInformation),
admin.site.register(DnsRegisterPrivateNameserver),
admin.site.register(DnsIdPros),
admin.site.register(DnsServer),
admin.site.register(DnsEmailForward),