from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import CheckoutMoneyDbs
from django.contrib.auth.models import User
from decouple import config 
import stripe
from stripe.api_resources import source
stripe.api_key = config('SSecretKey')
# stripe.api_key = 'sk_test_51JbczeBgu337whcjdUTGCGosq7hF9vi4isDvpOKmBnTxBaUTwKQKC5IOGhfSmdLmVd8hSayC625fppP13GVF4E4c00pb6Nl2zA'

@login_required
def Sorry(request, dnsname):
        DnsName = request.POST['DnsName']
        context = {
                'title': 'WasiLab Under Maintenance'
        }
        return render(request, 'CheckoutMoney/Sorry.html', context)

@login_required
def cart(request, dnsname):
        if request.method == 'POST':
                DnsName = request.POST['DnsName']

                return render(request, 'CheckoutMoney/Cart.html', {'DnsName': DnsName, 'dnsname':DnsName})

        else:
                return render(request, 'CheckoutMoney/Cart.html')

@login_required
def charge(request, dnsname):
        if request.method == 'POST':
                # print('Data : ', request.POST)

                DnsName = request.POST['DnsName']
                amount = int(request.POST['amount'])
                name = request.POST['name']
                email = request.POST['email']
                address = request.POST['address']
                stripeToken = request.POST['stripeToken']
                Username = request.POST['username']

                customer = stripe.Customer.create(
                        name = request.POST['name'],
                        email = request.POST['email'],
                        source = request.POST['stripeToken']
                )

                charge = stripe.Charge.create(
                        customer=customer,
                        amount = amount*100,
                        currency = 'usd',
                        description= 'Powered by WasiLab'
                )

                CheckoutMoneyDbSave = CheckoutMoneyDbs(username = User.objects.get(username= Username), DnsName=DnsName, name=name, email=email, address=address, stripeToken = stripeToken)
                CheckoutMoneyDbSave.save()
                return redirect(reverse('DnsCon', args=[DnsName]))

        else:
                return redirect(reverse('DnsCon'))