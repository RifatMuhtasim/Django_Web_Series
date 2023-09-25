from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.


class DnsServer(models.Model):
        username = models.CharField(max_length=50)
        DnsName = models.CharField(max_length=50)
        Nameserver1 = models.CharField(max_length=50)
        Nameserver2 = models.CharField(max_length=50)
        Nameserver3 = models.CharField(max_length=50)
        Nameserver4 = models.CharField(max_length=50)
        Nameserver5 = models.CharField(max_length=50)

        def __str__(self):
                return self.DnsName

class DnsManRecord(models.Model):
        username = models.CharField(max_length=50)
        DnsName = models.CharField(max_length=50)
        RecordType = models.CharField(max_length=50)
        HostName = models.CharField(max_length=50)
        IpAddress = models.CharField(max_length=50)
        Ttl = models.CharField(max_length=50)

        def __str__(self):
                return f'Dns Management Record: {self.DnsName}'

class DnsEmailForward(models.Model):
        username =models.CharField(max_length=50)
        DnsName = models.CharField(max_length=50)
        prefix = models.CharField(max_length=50)
        forward = models.CharField(max_length=50)

        def __str__(self):
                return f'Email Forwarding {self.forward} : {self.DnsName}'

class DnsIdPros(models.Model):
        username =models.CharField(max_length=50)
        DnsName = models.CharField(max_length=50)
        IdPro = models.CharField(max_length=50)

        def __str__(self):
                return self.DnsName

class DnsRegisterPrivateNameserver(models.Model):
        username =models.CharField(max_length=50)
        DnsName =models.CharField(max_length=50)
        Nameserver =models.CharField(max_length=50)
        NameserverIp = models.CharField(max_length=50)

        def  __str__(self):
                return f'Private Nameserver for {self.DnsName}'