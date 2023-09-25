from django.db import models
from django.utils import timezone

# Create your models here.

class CustomerInfo(models.Model):
        FirstName = models.CharField(max_length=50, blank=False, null=False)
        LastName = models.CharField(max_length=50, blank=False, null=False)
        UserName = models.CharField(max_length=50, null=False, blank=False)
        Email=  models.CharField(max_length=50, blank=False, null=False)
        Password=  models.CharField(max_length=50, blank=False, null=False)

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
        Time = models.DateTimeField(default=timezone.now)
        
        CustomerId = models.CharField(max_length=50, blank=False, null=False)

        def __str__(self):
                return f'Customer Info : {self.UserName}'