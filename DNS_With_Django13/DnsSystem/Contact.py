from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from UserDetails.models import IcannModel as IM
from CheckoutMoney.models import CheckoutMoneyDbs as CK
from .ContactModel import WhoisInformation, AdminInformation, TransferDomainUs
import requests

ReUserId = 1125655
ReApiKey = '0QiYjWBZGSjbu3ebZ55NEBgYVZMYDLnH'

def ContactInformation(request, args):
        DnsName = args
        ibj = IM.objects.get(DnsName=DnsName)
        if request.user.username == ibj.UserName:
                if WhoisInformation.objects.filter(DnsName=DnsName).exists() and AdminInformation.objects.filter(DnsName=DnsName).exists():
                        context = {
                        'title': 'Contact Information',
                        'dnsname': args,
                        'ri': WhoisInformation.objects.get(DnsName=DnsName),
                        'ai': AdminInformation.objects.get(DnsName=DnsName)
                        }
                        return render(request, 'DnsSystem/CoInformation.html', context)
                
                else:
                        UserName = ibj.UserName
                        FirstName = ibj.FirstName
                        LastName = ibj.LastName
                        EmailField = ibj.Email
                        CompanyName = ibj.CompanyName
                        JobTitle = ibj.JobTitle
                        Address = ibj.Address1
                        City = ibj.City
                        State = ibj.State
                        Country = ibj.Country
                        PhoneNumber = ibj.PhoneNumber
                        PhoneCode = ibj.PhoneCode
                        ZipCode = ibj.ZipCode
                        CustomerId = ibj.CustomerId
                        ReContactId = ibj.ReContactId
                        AdContactId = ibj.AdContactId

                        widb = WhoisInformation(DnsName=DnsName, UserName=UserName, FirstName=FirstName, LastName=LastName,
                                                        EmailField=EmailField, CompanyName=CompanyName, JobTitle=JobTitle, Address=Address, City=City,
                                                        State=State, Country=Country, PhoneNumber=PhoneNumber, PhoneCode=PhoneCode, ZipCode=ZipCode, CustomerId=CustomerId, ReContactId=ReContactId)
                        widb.save()
                        aidb = AdminInformation(DnsName=DnsName, UserName=UserName, FirstName=FirstName, LastName=LastName,
                                                        EmailField=EmailField, CompanyName=CompanyName, JobTitle=JobTitle, Address=Address, City=City,
                                                        State=State, Country=Country, PhoneNumber=PhoneNumber, PhoneCode=PhoneCode, ZipCode=ZipCode, CustomerId=CustomerId, AdContactId=AdContactId)
                        aidb.save()

                        context = {
                        'title': 'Contact Information',
                        'dnsname': args,
                        'ri': WhoisInformation.objects.get(DnsName=DnsName),
                        'ai': AdminInformation.objects.get(DnsName=DnsName)
                        }
                        return render(request, 'DnsSystem/CoInformation.html', context)
        else:
                messages.info(request, 'Sorry You are not Eligible  Person for this Domain Name!')
                return redirect('/')


def wiupdate(request, dnsname):
        DnsName = dnsname
        obj = IM.objects.get(DnsName=DnsName)
        CustomerId = obj.CustomerId
        if request.user.username == obj.UserName:
                if request.method == "POST":
                        UserName = request.user.username
                        FirstName = request.POST['FirstName']
                        EmailField = request.POST['EmailField']
                        CompanyName = request.POST['CompanyName']
                        JobTitle = request.POST['JobTitle']
                        Address = request.POST['Address']
                        City = request.POST['City']
                        State = request.POST['State']
                        Country = request.POST['Country']
                        PhoneNumber = request.POST['PhoneNumber']
                        PhoneCode = request.POST['PhoneCode']
                        ZipCode = request.POST['ZipCode']

                        ReUrl = f"https://test.httpapi.com/api/contacts/add.json?auth-userid={ReUserId}&api-key={ReApiKey}&name={FirstName} &company={CompanyName}&email={EmailField}&address-line-1={Address}&city={City}&country={Country}&zipcode={ZipCode}&phone-cc={PhoneCode}&phone={PhoneNumber}&customer-id={obj.CustomerId}&type=Contact"
                        ReResponse = requests.get(ReUrl)
                        ReResult = ReResponse.json()
                        
                        if ReResponse.status_code != 200:
                                messages.info(request, f"{ReResult['message']}")
                                return redirect('home')

                        ModifyDomainUrl = f"https://test.httpapi.com/api/domains/modify-contact.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}&reg-contact-id={ReResult}&admin-contact-id={obj.AdContactId}&tech-contact-id={ReResult}&billing-contact-id={obj.AdContactId} "
                        Resp = requests.post(ModifyDomainUrl)
                        Resu = Resp.json()
                        print(Resu)

                        try:
                                msg = Resu['actionstatusdesc']
                                messages.info(request, f"{msg}")
                        except:
                                msg = Resu['message']
                                messages.info(request, f"{msg}")
                                return redirect('home')
                        else:
                                wiupdate = WhoisInformation.objects.filter(DnsName=DnsName)
                                wiupdate.update(ReContactId=ReResult, CustomerId=CustomerId , DnsName=DnsName, UserName=UserName, FirstName=FirstName,
                                                                EmailField=EmailField, CompanyName=CompanyName, JobTitle=JobTitle, Address=Address, City=City,
                                                                State=State, Country=Country, PhoneNumber=PhoneNumber, PhoneCode=PhoneCode, ZipCode=ZipCode)
                                data = IM.objects.filter(DnsName = DnsName)
                                data.update(ReContactId = ReResult)

                                return redirect(reverse('ContactInformation', args=[DnsName]))
        else:
                messages.info(request, 'Sorry You are not Eligible  Person for this Domain Name!')
                return redirect('/')


def aiupdate(request, dnsname):
        DnsName = dnsname
        obj = IM.objects.get(DnsName=DnsName)
        CustomerId = obj.CustomerId
        if request.user.username == obj.UserName:
                if request.method == "POST":
                        UserName = request.user.username
                        FirstName = request.POST['FirstName']
                        EmailField = request.POST['EmailField']
                        CompanyName = request.POST['CompanyName']
                        JobTitle = request.POST['JobTitle']
                        Address = request.POST['Address']
                        City = request.POST['City']
                        State = request.POST['State']
                        Country = request.POST['Country']
                        PhoneNumber = request.POST['PhoneNumber']
                        PhoneCode = request.POST['PhoneCode']
                        ZipCode = request.POST['ZipCode']

                        AdUrl = f"https://test.httpapi.com/api/contacts/add.json?auth-userid={ReUserId}&api-key={ReApiKey}&name={FirstName}&company={CompanyName}&email={EmailField}&address-line-1={Address}&city={City}&country={Country}&zipcode={ZipCode}&phone-cc={PhoneCode}&phone={PhoneNumber}&customer-id={obj.CustomerId}&type=Contact"
                        AdResponse = requests.get(AdUrl)
                        AdResult = AdResponse.json()
                        
                        if AdResponse.status_code != 200:
                                messages.info(request, f"{AdResult['message']}")
                                return redirect('home')

                        ModifyDomainUrl = f"https://test.httpapi.com/api/domains/modify-contact.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}&reg-contact-id={obj.ReContactId}&admin-contact-id={AdResult}&tech-contact-id={obj.ReContactId}&billing-contact-id={AdResult} "
                        Resp = requests.post(ModifyDomainUrl)
                        Resu = Resp.json()
                        print(Resu)

                        try:
                                msg = Resu['actionstatusdesc']
                                messages.info(request, f"{msg}")
                        except:
                                msg = Resu['message']
                                messages.info(request, f"{msg}")
                                return redirect('home')
                        else:
                                aiupdate = AdminInformation.objects.filter(DnsName=DnsName)
                                aiupdate.update(AdContactId=AdResult, CustomerId=CustomerId , DnsName=DnsName, UserName=UserName, FirstName=FirstName, 
                                                                EmailField=EmailField, CompanyName=CompanyName, JobTitle=JobTitle, Address=Address, City=City,
                                                                State=State, Country=Country, PhoneNumber=PhoneNumber, PhoneCode=PhoneCode, ZipCode=ZipCode)
                                data = IM.objects.filter(DnsName = DnsName)
                                data.update(AdContactId = AdResult)

                                return redirect(reverse('ContactInformation', args=[DnsName]))
        else:
                messages.info(request, 'Sorry You are not Eligible  Person for this Domain Name!')
                return redirect('/')



def aixupdate(request, dnsname):
        DnsName = dnsname
        obj = IM.objects.get(DnsName=DnsName)
        if request.user.username == obj.UserName:
                if request.method == "POST":
                        UserName = request.user.username
                        FirstName = request.POST['FirstName']
                        LastName = request.POST['LastName']
                        EmailField = request.POST['EmailField']
                        CompanyName = request.POST['CompanyName']
                        JobTitle = request.POST['JobTitle']
                        Address = request.POST['Address']
                        City = request.POST['City']
                        State = request.POST['State']
                        Country = request.POST['Country']
                        PhoneNumber = request.POST['PhoneNumber']
                        PhoneCode = request.POST['PhoneCode']
                        ZipCode = request.POST['ZipCode']

                        aiupdate = AdminInformation.objects.filter(DnsName=DnsName)
                        aiupdate.update(DnsName=DnsName, UserName=UserName, FirstName=FirstName, LastName=LastName,
                                                        EmailField=EmailField, CompanyName=CompanyName, JobTitle=JobTitle, Address=Address, City=City,
                                                        State=State, Country=Country, PhoneNumber=PhoneNumber,PhoneCode=PhoneCode, ZipCode=ZipCode)
                        return redirect(reverse('ContactInformation', args=[DnsName]))
        else:
                messages.info(request, 'Sorry You are not Eligible  Person for this Domain Name!')
                return redirect('/')


# Transfer Domain Name 
def TransferView(request):
        context={
                'title':'Domain Transfer',
        }
        return render(request, 'DnsSystem/TransferDomain.html', context)

def TransferDomain(request):
        if request.method=="POST":
                DnsName = request.POST['DnsName']
                Token = request.POST['Token']

                if CK.objects.filter(stripeToken = Token, DnsName = DnsName).exists():
                        messages.info(request, 'We Now Transfer your Domain Name')
                        db = TransferDomainUs(DnsName=DnsName, Token=Token)
                        db.save()
                        return redirect('home')

                else:
                        messages.info(request, 'Your Information does not match !!')
                        return redirect('home')
