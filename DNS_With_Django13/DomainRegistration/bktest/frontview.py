from django.shortcuts import redirect, render
from django.contrib import messages
import requests, json 
from UserDetails.models import IcannModel as IM
from CheckoutMoney.models import CheckoutMoneyDbs as CM


def DomainApiData(request):
        dnsname = request.POST['dnsname']
        obj1 = IM.objects.get(DnsName = dnsname)
        obj2 = CM.objects.get(DnsName = dnsname)

        IP = '747.747.747.747'
        Currency = 'USD'
        PriceType = 'Card'
        PaymentMethod = 'Visa'
        Type = 'register'

        url = f"http://127.0.0.1:8000/domain-registration/?DnsName={obj1.DnsName}&UserName={obj1.UserName}&FirstName={obj1.FirstName}&LastName={obj1.LastName}&CompanyName={obj1.CompanyName}&JobTitle={obj1.JobTitle}&Address={obj1.Address1}&City={obj1.City}&Country={obj1.Country}&State={obj1.State}&Email={obj1.Email}&PhoneNumber={obj1.PhoneNumber}&DomainYear={obj1.DomainYear}&DomainAutoRenew={obj1.DomainAutoRenew}&DnsStatus={obj1.DnsSecurityStatus}&DomainSsl={obj1.DomainSsl}&DomainPremium={obj1.DomainPremium}&NameServer1={obj1.NameServer1}&NameServer2={obj1.NameServer2}&IP={IP}&Currency={Currency}&PriceType={PriceType}&PaymentMethod={PaymentMethod}&Type={Type}"

        response = requests.get(url)
        print(response)
        if response.status_code != 200:
                messages.info(request, 'FAILED!! Sorry we can not save your data !! ')
                return redirect('home')
        else:
                # return redirect('ApiTestSaveView')
                return redirect('Congratulations')