from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decouple import config
import json
from django.http import JsonResponse
import requests
from UserDetails.models import IcannModel as IM
from DomainRegistration.views import ReApiKey, ReUserId
import time
from django.utils import timezone
from datetime import datetime


@login_required
def paypal(request):

    context = {
        'title': 'Paypal Payment',
        'PaypalClientId': config('PaypalSanboxClientId'),
        'DnsName': 'tablab.com'
    }
    return render(request, 'CheckoutMoney/paypal.html', context)

def paypal_payment_confirm(request):
    if request.method != 'POST':
        context = {
            'title': 'Paypal Payment Confirm',
            'DnsName': 'TabLab.com',
            'CName': 'TabLab Corporation',
        }
        return render(request, 'UserDetails/DnsCongratulations.html', context)

    else:
        body = json.loads(request.body)
        print('Domain Name of Transacion ID is : ', body)
        return JsonResponse('Payment completed!', safe=False)


# PayPal on Auto Renew 
@login_required
def paypal_auto_renew(request):
    global domain_auto_renew_year , exp_time
    renew_payment_per_year = 0.12
    UserName = request.user.username
    DnsName = request.POST['DnsName']
    exp_time = int(request.POST['exp_time'])
    domain_auto_renew_year = int(request.POST['domain_auto_renew_year'])
    auto_renew_payment = float(renew_payment_per_year * domain_auto_renew_year)
    
    current_time = int(time.time())
    future_10_year_time = int(current_time+315532800)
    domain_auto_renew_time = int((domain_auto_renew_year * 31536000)+exp_time)
    if domain_auto_renew_time > future_10_year_time:
        messages.info(request, 'You can not Renew 10 Years from Local time')
        return redirect('home')

    context = {
        'title': 'Paypal Payment',
        'PaypalClientId': config('PaypalSanboxClientId'),
        'DnsName': DnsName,
        'Payment': auto_renew_payment,
        'exp_time': exp_time,
    }
    return render(request, 'CheckoutMoney/paypal2.html', context)


def paypal_auto_renew_confirm(request):
    InvoiceOption = 'NoInvoice'
    DnsName = request.POST['DnsName']
    obj = IM.objects.get(DnsName =DnsName)

    url = f"https://test.httpapi.com/api/domains/renew.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}&years={domain_auto_renew_year}&exp-date={exp_time}&invoice-option={InvoiceOption}&discount-amount=0.0&auto-renew=true"
    result = requests.post(url).json()
    print(result)
        
    try:
        msg = result['message']
        messages.info(request, f'{msg}')
        return redirect('home')

    except:
        msg = result['actiontypedesc']
        messages.info(request, f'{msg}')
        TransactionId = request.POST['TransactionId']
        print(DnsName+ ' of Transaction ID is: ' + TransactionId)

        return redirect('Congratulations')



        


        