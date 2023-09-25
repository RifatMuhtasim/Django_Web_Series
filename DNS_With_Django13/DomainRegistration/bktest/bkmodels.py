from django.db import models
from django.utils import timezone


class ApiTestModel(models.Model):
        DnsName = models.CharField(max_length=50)
        UserName = models.CharField(max_length=50)
        FirstName = models.CharField(max_length=50)
        LastName = models.CharField(max_length=50)
        CompanyName = models.CharField(max_length=100)
        JobTitle = models.CharField(max_length=50)
        Address = models.CharField(max_length=50)
        City=  models.CharField(max_length=50)
        State=  models.CharField(max_length=50)
        Country=  models.CharField(max_length=50)
        PhoneNumber=  models.CharField(max_length=50)
        Email=  models.CharField(max_length=50)
        
        DomainYear = models.CharField(max_length=50)
        DomainAutoRenew =  models.CharField( max_length=50)
        DnsStatus = models.CharField(  max_length=50)
        DomainSsl =  models.CharField(  max_length=50)
        DomainPremium =  models.CharField(  max_length=50)
        NameServer1=  models.CharField(max_length=50)
        NameServer2=  models.CharField(max_length=50)

        IP=  models.CharField(max_length=50)
        Currency=  models.CharField(max_length=50)
        PriceType =  models.CharField(max_length=50)
        PaymentMethod =  models.CharField(max_length=50)
        Type =  models.CharField(max_length=50)
        Time = models.DateTimeField(default=timezone.now)

        def __str__(self):
                return f'Domain API Test Save : {self.DnsName}'