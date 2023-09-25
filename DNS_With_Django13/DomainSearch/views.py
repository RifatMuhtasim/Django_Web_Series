import re
import socket
from django.http import response 
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from .models import Dns, DnsTlds
from UserDetails.models import UserPersonalInformation
from decouple import config
import requests
import json
# Create your views here.

# New Domain Search Result 
def DomainSearchName(request):
        if request.method == 'POST':
                tld = request.POST['tld']
                namez = request.POST['name'].lower()
                name = ''.join(x for x in namez if x.isalnum())
                dnsname = name+tld

                recaptcha_response = request.POST['g-recaptcha-response']
                data = {
			'secret': config('ReCaptchaSecretKey3'),
			'response': recaptcha_response
		}
                url = "https://www.google.com/recaptcha/api/siteverify"
                response = requests.post(url=url, data=data)
                result = response.json()
                print(result)
                
                if result['success'] is False:
                        msg = result['error-codes']
                        messages.info(request, f"{msg}")
                        return redirect('home')
                else:
                        if result['score'] < 0.3:
                                messages.info(request, "Sorry! Recaptcha score is Too Low")
                                return redirect('home')

                        return redirect(reverse('DomainSearchResult', args=[dnsname]))


def DomainSearchResult(request, args):
        dnsname = args
        name = dnsname[0:-4]
        tld = dnsname[-4:]

        if name != '':
                if tld == '.com' or tld =='.org' or tld=='.net' or tld =='.biz' or tld=='.xyz':
                        try:
                                socket.gethostbyname_ex(name+tld)
                                omc = True
                        except:
                                omc = False
                        try:
                                socket.gethostbyname_ex(name+'.com')
                                com = True
                        except:
                                com = False
                        try:
                                socket.gethostbyname_ex(name+'.org')
                                org = True
                        except:
                                org = False
                        try:
                                socket.gethostbyname_ex(name+'.net')
                                net = True
                        except:
                                net = False
                        try:
                                socket.gethostbyname_ex(name+'.biz')
                                biz = True
                        except:
                                biz = False
                        try:
                                socket.gethostbyname_ex(name+'.xyz')
                                xyz = True
                        except:
                                xyz = False
                        context = {
                                'DomainSearch': dnsname, 
                                'dnsname':dnsname,
                                'name':name,
                                'tld':tld,
                                'com': com,
                                'org':org,
                                'net':net,
                                'biz':biz,
                                'xyz':xyz,
                                'omc':omc,
                        }
                        return render(request, 'DomainSearch/ResultPage.html', context)

                else:
                        return render(request, 'DomainSearch/ResultPage.html')
        else:
                messages.info(request,"Domain Name is Null !  Please put a valid Domain Name")
                return redirect('/')
                                
                