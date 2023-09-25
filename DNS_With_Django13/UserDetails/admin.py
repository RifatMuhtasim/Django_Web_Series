from UserDetails.models import UserPersonalInformation
from django.contrib import admin
from .models import DnsInformation, IcannModel, UserPersonalInformation

# Register your models here.

admin.site.register(UserPersonalInformation)
admin.site.register(DnsInformation)
admin.site.register(IcannModel)