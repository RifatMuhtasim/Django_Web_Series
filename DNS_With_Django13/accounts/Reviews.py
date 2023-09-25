from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
import requests, json 
from .models import CustomerInfo
import urllib.parse
from decouple import config

ReUserId = 1125655
ReApiKey = '0QiYjWBZGSjbu3ebZ55NEBgYVZMYDLnH'

def ReRegisterTest(request):
        passwd = '#36Khandokar'

        url = f"https://test.httpapi.com/api/customers/v2/signup.json?auth-userid={ReUserId}&api-key={ReApiKey}&username=muhtdfdfrrrr@outlook.com&name=Khandokar Wasi&company=Group Wasi&address-line-1=Rustompur&city=Sylhet&state=Sylhet&country=BD&zipcode=3100&phone-cc=880&phone=1991822453&lang-pref=en&passwd={passwd}"

        Response = requests.post(url)
        print(Response)
        Result = Response.json()
        print(Result)

        return redirect('home')


def ReRegister(request):
        if request.method == "POST":
                FirstName = request.POST['FirstName']
                LastName = request.POST['LastName']
                UserName = request.POST['UserName']
                Email = request.POST['Email']
                Password1 = request.POST['Password1']
                Password2 = request.POST['Password2']

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

                SpecialSym =['~', '*', '!', '@', '$', '#', '%', '_', '+', '.', '?', ':', ',', '{', '}']

                if Password1 != Password2:
                        messages.info(request, 'Password does not matched !')
                        return redirect('register')
                elif len(Password1) < 6:
                        messages.info(request, 'length should be at least 6')
                        return redirect('register')
                elif len(Password1) > 16:
                        messages.info(request, 'length should be not be greater than 16')
                        return redirect('register')
                elif not any(char.isdigit() for char in Password1):
                        messages.info(request, 'Password should have at least one numeral')
                        return redirect('register')
                elif not any(char.isupper() for char in Password1):
                        messages.info(request, 'Password should have at least one uppercase letter')
                        return redirect('register')
                elif not any(char.islower() for char in Password1):
                        messages.info(request, 'Password should have at least one lowercase letter')
                        return redirect('register')
                elif not any(char in SpecialSym for char in Password1):
                        messages.info(request, 'Password should have at least one of the special character ')
                        return redirect('register')
                elif User.objects.filter(username = UserName).exists():
                        messages.info(request, 'UserName is already taken')
                        return redirect('register')
                elif User.objects.filter(email= Email).exists():
                        messages.info(request, 'Email name is already taken')
                        return redirect('register')
                else:
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
                                return redirect('register')

                        else:
                                passwd = urllib.parse.quote(Password1)
                                ReUrl = f"https://test.httpapi.com/api/customers/v2/signup.json?auth-userid={ReUserId}&api-key={ReApiKey}&username={Email}&name={FirstName} {LastName}&company={CompanyName}&address-line-1={Address1}&city={City}&state={State}&country={Country}&zipcode={ZipCode}&phone-cc={PhoneCode}&phone={PhoneNumber}&lang-pref=en&passwd={passwd}"
                                Response = requests.post(ReUrl)
                                Result = Response.json()
                                # print(Result)

                                if Response.status_code != 200:
                                        msg = Result['message']
                                        messages.info(request, f'{msg}')
                                        return redirect('home')

                                CustomerId = Result
                                Info = CustomerInfo(CustomerId= CustomerId, Password = Password1, FirstName=FirstName, LastName=LastName, UserName=UserName, Email=Email, CompanyName=CompanyName, JobTitle=JobTitle, Address1=Address1, Address2=Address2, City=City, State=State, ZipCode=ZipCode, Country=Country, PhoneCode=PhoneCode, PhoneNumber=PhoneNumber )
                                Info.save()
                                user = User.objects.create_user(first_name= FirstName, last_name= LastName, username= UserName, email= Email, password=Password1)
                                user.save()

                                return redirect('signin')

        else:
                context = {
                        'title': 'Sign Up for Customer',
                }
                return render(request, 'accounts/ReRegister.html', context)