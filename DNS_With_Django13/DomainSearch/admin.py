from django.contrib import admin
from .models import Dns, DnsTlds
# Register your models here.

admin.site.register(Dns)
admin.site.register(DnsTlds)
