from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class CheckoutMoneyDbs(models.Model):
        DnsName = models.CharField(max_length=50)
        name = models.CharField(max_length=50)
        email = models.CharField(max_length=50)
        address = models.CharField(max_length=50)
        stripeToken = models.CharField(max_length=50)
        username = models.CharField(max_length=50, null=True, blank=False)

        def __str__(self):
                return self.DnsName