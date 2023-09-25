from django.db import models

# Create your models here.

class Dns(models.Model):
        DnsName = models.CharField(max_length=100, blank=True)

        def __str__(self):
                return self.DnsName

class DnsTlds(models.Model):
        DnsTldsName = models.CharField(max_length=10, blank=True)

        def __str__(self):
                return self.DnsTldsName