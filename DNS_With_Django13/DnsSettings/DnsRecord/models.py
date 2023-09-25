from django.db import models
from django.utils import timezone


class ARecords(models.Model):
        DomainName = models.CharField(max_length=50, null=False, blank=False)
        HostName = models.CharField(max_length=50, null=False, blank=False)
        IPv4Value = models.CharField(max_length=50, null=False, blank=False)
        TTL = models.CharField(max_length=50, null=False, blank=False)
        Time = models.DateTimeField(default=timezone.now)