from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from UserDetails.models import UserPersonalInformation, IcannModel as IM
import requests
from accounts.models import CustomerInfo
from decouple import config
from django.urls import reverse
from django.core.mail import send_mail

# ReCustomerId = 23924871
ReCustomerId = 23931832
ReUserId = 1125655
ReApiKey = '0QiYjWBZGSjbu3ebZ55NEBgYVZMYDLnH'

def Congratulations(request):
        context = {
                'title': 'Domain Registration Successfull',
        }
        return render(request, 'DomainRegistration/DnsCongratulations.html', context)


@login_required
def ReUserData(request, dnsname):
        if request.method == "POST":
                FirstName = request.POST['FirstName']
                LastName = request.POST['LastName']
                CompanyName = request.POST['CompanyName']
                JobTitle = request.POST['JobTitle']
                Address1 = request.POST['Address1']
                Address2 = request.POST['Address2']
                ZipCode = request.POST['ZipCode']
                City = request.POST['City']
                State = request.POST['State']
                Country = request.POST['CountryCode'].upper()
                PhoneCode = request.POST['DialCode']
                PhoneNum = request.POST['PhoneNumber']
                PhoneNumber = int(PhoneNum.replace("-",""))
                Email = request.POST['Email']
                DnsName = request.POST['DnsName']
                UserName = request.POST['UserName']

                data = CustomerInfo.objects.get(UserName=UserName)
                CustomerId = data.CustomerId

                client_key = request.POST['g-recaptcha-response']
                secret_key = config('ReCaptchaSecretKey2')

                captcha_data = {
                        'secret': secret_key,
                        'response': client_key,
                }
                urlz = f"https://www.google.com/recaptcha/api/siteverify"
                responsez = requests.post(url=urlz, data=captcha_data)
                resultz = responsez.json()

                if resultz['success'] != True:
                        messages.info(request, 'please check that you are not a robot')
                        return redirect('home')

                else:
                        #url part for reseller club
                        ReUrl = f"https://test.httpapi.com/api/contacts/add.json?auth-userid={ReUserId}&api-key={ReApiKey}&name={FirstName} {LastName}&company={CompanyName}&email={Email}&address-line-1={Address1}&address-line-2={Address2}&city={City}&country={Country}&zipcode={ZipCode}&phone-cc={PhoneCode}&phone={PhoneNumber}&customer-id={CustomerId}&type=Contact"
                        AdUrl = f"https://test.httpapi.com/api/contacts/add.json?auth-userid={ReUserId}&api-key={ReApiKey}&name={FirstName} {LastName}&company={CompanyName}&email={Email}&address-line-1={Address1}&address-line-2={Address2}&city={City}&country={Country}&zipcode={ZipCode}&phone-cc={PhoneCode}&phone={PhoneNumber}&customer-id={CustomerId}&type=Contact"

                        ReRequest = requests.post(ReUrl)
                        ReResponse = ReRequest.json()
                        ReContactId = ReResponse
                        AdRequest = requests.post(AdUrl)
                        AdResponse = AdRequest.json()
                        AdContactId = AdResponse
                        # print(ReResponse)

                        if ReRequest.status_code != 200 or AdRequest.status_code !=200:
                                messages.info(request, f"Sorry !! Your Login Request still Pending")
                                return redirect('home')
                        # print(ReResponse, AdResponse)

                        SavedUserData = UserPersonalInformation(CustomerId = CustomerId, ReContactId = ReContactId, AdContactId= AdContactId, UserName= UserName, DnsName=DnsName, FirstName= FirstName, LastName = LastName, CompanyName= CompanyName, JobTitle= JobTitle, Address1 = Address1, Address2 = Address2, ZipCode = ZipCode, 
                                                City= City, State = State, Country= Country, PhoneCode = PhoneCode, PhoneNumber = PhoneNumber, Email=Email)
                        SavedUserData.save()

                        return render(request, 'UserDetails/DataSecurity.html', {'DnsName': DnsName, 'dnsname':dnsname})
        else:
                return render(request, 'UserDetails/DataSecurity.html')


def ReDomainApiData(request):
        dnsname = request.POST['dnsname']
        obj = IM.objects.get(DnsName = dnsname)
        DomainYear = obj.DomainYear
        AutoRenew = obj.DomainAutoRenew
        PrivacySecurity = obj.DnsSecurityStatus
        DomainPremium = obj.DomainPremium

        CustomerId = obj.CustomerId
        ReContactId = obj.ReContactId
        AdContactId = obj.AdContactId

        InvoiceOption = 'NoInvoice'
        # InvoiceOption = 'PayInvoice'
        # InvoiceOption = 'KeepInvoice'
        # InvoiceOption = 'OnlyAdd'

        ns1= obj.NameServer1
        ns2 = obj.NameServer2
        # ns1 = 'dns3.parkpage.foundationapi.com'
        # ns2 = 'dns4.parkpage.foundationapi.com'

        ReUrl = f"https://test.httpapi.com/api/domains/register.json?auth-userid={ReUserId}&api-key={ReApiKey}&domain-name={dnsname}&years={DomainYear}&ns={ns1}&ns={ns2}&customer-id={CustomerId}&reg-contact-id={ReContactId}&admin-contact-id={AdContactId}&tech-contact-id={ReContactId}&billing-contact-id={AdContactId}&invoice-option={InvoiceOption}&discount-amount=0.0&protect-privacy={PrivacySecurity}&auto-renew={AutoRenew}&purchase-premium-dns={DomainPremium}"

        Response = requests.post(ReUrl)
        Result = Response.json()
        if Response.status_code != 200:
                msg = Result['message']
                messages.info(request, f"{msg}")
                return redirect('home')

        # print(Result)
        if Result['status'] == 'Success' or Result['actionstatus'] == 'Success':
                OrderId = Result['entityid']
                # ActionId = Result['eaqid']
                # ActionId = Result['invoiceid']
                up = IM.objects.filter(DnsName= dnsname)
                up.update(OrderId=OrderId)
                
                try:
                        # SendEmail 
                        subject  = f"{obj.DnsName} Info. Congratulations ! Now you are the owner of the {obj.DnsName} Domain"
                        message = f"Hey, {obj.FirstName} {obj.LastName}.\nYou Successfully buy this {obj.DnsName} domain Name from us. \n \n \nTry to login this Website: http://127.0.0.1:8000/accounts/signin \nEmail is : {obj.Email}\nUser Name is: {obj.UserName} \n  \nAlso, \nManage Domain from this Website: https://tabl1125655.myorderbox.com/servlet/LoginServlet?role=customer&currenturl=https://tabl1125655.myorderbox.com \nEmail is : {obj.Email} \n\nThank You! WasiLab Corporation 2021"
                        to_email = "tablab.bd@gmail.com"
                        send_mail(subject, message, to_email, [f"{obj.Email}"])
                        return redirect('Congratulations')
                except: 
                        messages.info(request, 'We can not send email on your account')
                        return redirect('Congratulations')
        else:
                messages.info(request, f"Sorry!  {Response} wrong in here. ")
                return redirect('home')