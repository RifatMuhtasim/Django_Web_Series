from django.contrib import messages
from django.shortcuts import redirect, render
# import stripe
from .models import UserPersonalInformation, DnsInformation, IcannModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from accounts.models import CustomerInfo
from decouple import config

# Create your views here.

@login_required
def UploadDataView(request):
        dnsname = request.POST['dnsname'].lower()
        username = request.user.username
        obj = CustomerInfo.objects.get(UserName = username)
        context={
                'DomainSearch':dnsname,
                'dnsname':dnsname,
                'obj': obj,
        }
        return render(request, 'UserDetails/UploadData.html', context)

@login_required
def UploadData(request, dnsname):
        if request.method == "POST":
                FirstName = request.POST['FirstName']
                LastName = request.POST['LastName']
                CompanyName = request.POST['CompanyName']
                JobTitle = request.POST['JobTitle']
                Address = request.POST['Address1']
                City = request.POST['City']
                State = request.POST['State']
                Country = request.POST['countryCode']
                PhoneCode = request.POST['phoneCode']
                PhoneNumber = request.POST['phoneNumber']
                Email = request.POST['Email']
                print(PhoneCode, Country, PhoneNumber)

                UserName = request.POST['UserName']
                DnsName = request.POST['DnsName']

                SavedUserData = UserPersonalInformation(UserName= UserName, DnsName=DnsName, FirstName= FirstName, LastName = LastName, CompanyName= CompanyName, JobTitle= JobTitle, Address1 = Address, 
                                        City= City, State = State, Country= Country, PhoneNumber = PhoneNumber, Email=Email)
                SavedUserData.save()
                return render(request, 'UserDetails/DataSecurity.html', {'DnsName': DnsName, 'dnsname':dnsname})
        else:
                return render(request, 'UserDetails/DataSecurity.html')


@login_required
def UploadDnsInformation(request, dnsname):

        NameServer1 = request.POST['NameServer1']
        NameServer2 = request.POST['NameServer2']
        DnsName = request.POST['DnsName']
        UserName = request.POST['UserName']

        DomainAutoRenew = request.POST['DomainAutoRenew']
        DnsStatus = request.POST['status']
        DomainSsl = request.POST['DomainSsl']
        DomainPremium = request.POST['DomainPremium']
        DomainYear = request.POST['DomainYear']

        SavedDnsInformation = DnsInformation(DomainYear = DomainYear, DomainAutoRenew=DomainAutoRenew, DomainSsl=DomainSsl, DomainPremium=DomainPremium , DnsStatus = DnsStatus, NameServer1 = NameServer1, NameServer2=NameServer2, DnsName= DnsName, UserName= UserName)
        SavedDnsInformation.save()

        return render(request, 'UserDetails/DnsBuy.html', {'DnsName': DnsName, 'dnsname':dnsname})


@login_required
def DnsIcann(request, dnsname):
        DnsName = request.POST['DnsName']
        return render(request, 'UserDetails/DnsIcann.html' , {'DnsName': DnsName, 'dnsname':dnsname})


@login_required
def DnsCon(request, args):
        DnsName = args
        if IcannModel.objects.filter(DnsName=DnsName).exists():
                messages.info(request, 'Dns Name is Already in Database')
                return redirect('/')
        else:
                obj10 = UserPersonalInformation.objects.filter(DnsName = DnsName)
                obj1 = obj10.last()
                obj20 = DnsInformation.objects.filter(DnsName=DnsName)
                obj2= obj20.last()
                CName= obj1.CompanyName

                CustomerId = obj1.CustomerId
                ReContactId = obj1.ReContactId
                AdContactId = obj1.AdContactId
                DnsName = obj1.DnsName
                UserName = obj1.UserName
                FirstName = obj1.FirstName
                LastName = obj1.LastName
                CompanyName = obj1.CompanyName
                JobTitle = obj1.JobTitle
                Address1 = obj1.Address1
                Address2 = obj1.Address2
                ZipCode = obj1.ZipCode
                City = obj1.City
                State = obj1.State
                Country = obj1.Country
                PhoneCode = obj1.PhoneCode
                PhoneNumber = obj1.PhoneNumber
                Email = obj1.Email

                DomainYear = obj2.DomainYear
                DomainAutoRenew = obj2.DomainAutoRenew
                DnsSecurityStatus = obj2.DnsStatus
                DomainSsl = obj2.DomainSsl
                DomainPremium = obj2.DomainPremium
                NameServer1 = obj2.NameServer1
                NameServer2 = obj2.NameServer2


                SavedIcann= IcannModel( CustomerId = CustomerId , ReContactId = ReContactId, AdContactId = AdContactId, DomainYear=DomainYear , DnsName=DnsName, UserName=UserName, FirstName=FirstName, LastName=LastName, CompanyName=CompanyName,
                                                JobTitle=JobTitle, Address1=Address1, Address2=Address2, ZipCode=ZipCode, PhoneCode=PhoneCode, City=City, State=State, Country=Country, PhoneNumber=PhoneNumber, Email=Email,
                                                DomainAutoRenew= DomainAutoRenew, DnsSecurityStatus=DnsSecurityStatus, DomainSsl=DomainSsl, DomainPremium= DomainPremium , NameServer1=NameServer1, NameServer2=NameServer2)
                SavedIcann.save()

                return render(request, 'DomainRegistration/ConfirmDomainRegistration.html', {'DnsName': DnsName, 'CName': CName , 'dnsname':args})
