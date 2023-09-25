from django.db import models
from django.utils import timezone

# Create your models here.

class UserPersonalInformation(models.Model):
        CustomerId = models.CharField(max_length=50, blank=False, null=False)
        ReContactId = models.CharField(max_length=50, blank=False, null=False)
        AdContactId = models.CharField(max_length=50, blank=False, null=False)
        UserName = models.CharField(max_length=50, null=False, blank=False)
        DnsName = models.CharField(max_length=50, null=False, blank=False)

        FirstName = models.CharField(max_length=50, blank=False, null=False)
        LastName = models.CharField(max_length=50, blank=False, null=False)
        CompanyName = models.CharField(max_length=100, blank=False, null=False)
        JobTitle = models.CharField(max_length=50, blank=False, null=False)
        Address1 = models.CharField(max_length=50, blank=False, null=False)
        Address2 = models.CharField(max_length=50, blank=False, null=False)
        ZipCode = models.CharField(max_length=50, blank=False, null=False)
        City=  models.CharField(max_length=50, blank=False, null=False)
        State=  models.CharField(max_length=50, blank=False, null=False)
        Country=  models.CharField(max_length=50, blank=False, null=False)
        PhoneCode = models.CharField(max_length=50, blank=False, null=False)
        PhoneNumber=  models.CharField(max_length=50, blank=False, null=False)
        Email=  models.CharField(max_length=50, blank=False, null=False)
        Time = models.DateTimeField(default=timezone.now)


        def __str__(self):
                return f'Domain Register : {self.DnsName}'


class DnsInformation(models.Model):
        NameServer1=  models.CharField(max_length=50, blank=False, null=False)
        NameServer2=  models.CharField(max_length=50, blank=False, null=False)
        DnsName = models.CharField(max_length=50, blank=False, null=False)
        UserName = models.CharField(max_length=50, blank=False, null=False)

        DomainAutoRenew =  models.CharField( max_length=50)
        DnsStatus = models.CharField(  max_length=50)
        DomainSsl =  models.CharField(  max_length=50)
        DomainPremium =  models.CharField(  max_length=50)

        DomainYear = models.CharField(max_length=50)

        def __str__(self):
                return self.DnsName


class IcannModel(models.Model):
        CustomerId = models.CharField(max_length=50, blank=False, null=False)
        ReContactId = models.CharField(max_length=50, blank=False, null=False)
        AdContactId = models.CharField(max_length=50, blank=False, null=False)
        OrderId=  models.CharField(max_length=50, blank=False, null=False)
        ActionId=  models.CharField(max_length=50, blank=False, null=False)

        DnsName = models.CharField(max_length=50, null=False, blank=False)
        UserName = models.CharField(max_length=50, null=False, blank=False)
        FirstName = models.CharField(max_length=50, blank=False, null=False)
        LastName = models.CharField(max_length=50, blank=False, null=False)
        CompanyName = models.CharField(max_length=100, blank=False, null=False)
        JobTitle = models.CharField(max_length=50, blank=False, null=False)
        Address1 = models.CharField(max_length=50, blank=False, null=False)
        Address2 = models.CharField(max_length=50, blank=False, null=False)
        ZipCode = models.CharField(max_length=50, blank=False, null=False)
        City=  models.CharField(max_length=50, blank=False, null=False)
        State=  models.CharField(max_length=50, blank=False, null=False)
        Country=  models.CharField(max_length=50, blank=False, null=False)
        PhoneCode = models.CharField(max_length=50, blank=False, null=False)
        PhoneNumber=  models.CharField(max_length=50, blank=False, null=False)
        Email=  models.CharField(max_length=50, blank=False, null=False)
        
        DomainYear = models.CharField(max_length=50)
        DomainAutoRenew =  models.CharField( max_length=50)
        DnsSecurityStatus = models.CharField(  max_length=50)
        DomainSsl =  models.CharField(  max_length=50)
        DomainPremium =  models.CharField(  max_length=50)
        NameServer1=  models.CharField(max_length=50, blank=False, null=False)
        NameServer2=  models.CharField(max_length=50, blank=False, null=False)
        Time = models.DateTimeField(default=timezone.now)

        def __str__(self):
                return f"Domain Icann Information: {self.DnsName}"
