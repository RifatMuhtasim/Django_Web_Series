from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField

class WhoisInformation(models.Model):
        DnsName = models.CharField(max_length=50)
        UserName = models.CharField(max_length=50)
        FirstName = models.CharField(max_length=50)
        LastName = models.CharField(max_length=50)
        EmailField = models.CharField(max_length=50)
        CompanyName = models.CharField(max_length=50)
        JobTitle = models.CharField(max_length=50)
        Address = models.CharField(max_length=50)
        City = models.CharField(max_length=50)
        State = models.CharField(max_length=50)
        Country = models.CharField(max_length=50)
        PhoneNumber = models.CharField(max_length=50)
        PhoneCode = models.CharField(max_length=50)
        ZipCode = models.CharField(max_length=50)
        CustomerId = models.CharField(max_length=50)
        ReContactId = models.CharField(max_length=50)

        def __str__(self):
                return f'Register Information {self.DnsName}'

class AdminInformation(models.Model):
        DnsName = models.CharField(max_length=50)
        UserName = models.CharField(max_length=50)
        FirstName = models.CharField(max_length=50)
        LastName = models.CharField(max_length=50)
        EmailField = models.CharField(max_length=50)
        CompanyName = models.CharField(max_length=50)
        JobTitle = models.CharField(max_length=50)
        Address = models.CharField(max_length=50)
        City = models.CharField(max_length=50)
        State = models.CharField(max_length=50)
        Country = models.CharField(max_length=50)
        PhoneNumber = models.CharField(max_length=50)
        PhoneCode = models.CharField(max_length=50)
        ZipCode = models.CharField(max_length=50)
        CustomerId = models.CharField(max_length=50)
        AdContactId = models.CharField(max_length=50)

        def __str__(self):
                return f'Admin Information {self.DnsName}'

class TransferDomainUs(models.Model):
        DnsName = models.CharField(max_length=50)
        Token = models.CharField(max_length=50)

        def __str__(self):
                return f'Transfer Domain {self.DnsName} to Us'