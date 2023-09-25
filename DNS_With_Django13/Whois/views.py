from django.shortcuts import redirect, render
from django.urls import reverse
import whois
import requests
from django.contrib import messages
# Create your views here.

def Whois(request):

        context = {
                'title':'Whois Search',
        }
        return render(request, 'Whois/WhoisSearch.html', context)

def dnsname(request):
                if request.method == "POST":
                        dnsname  = str( request.POST['DomainSearch'])
                        return redirect(reverse('WhoisResult', args=[dnsname]))

def WhoisResult(request, args):
        dnsname = str(args)

        try:
                WhoisResult = whois.whois(dnsname)
                context = {
                                'title':'Whois Result',
                                'dnsname': dnsname,
                                'WhoisResult': WhoisResult
                }
                return render(request, 'Whois/WhoisResult.html', context)

        except:
                dnsname = args
                context ={
                        'title':'Whois Result',
                        'dnsname':dnsname
                }
                return render(request, 'Whois/WhoisResult.html', context)


#Whois Result search by URL 

def WhoisResultUrl(request, args):
        dnsname = args
        ApiKey = 'c39f169f3ba7a02348c366ddcc6d1f5a'
        # http://api.whoapi.com/?apikey=c39f169f3ba7a02348c366ddcc6d1f5a&r=whois&domain={dnsname}
        ResultWhois = f'http://api.whoapi.com/?apikey={ApiKey}&r=whois&domain={dnsname}'
        try:
                ReqWho = requests.get(ResultWhois)

                if ReqWho.status_code != 200: 
                        messages.info(request, "Could not get availability state of Domain Name ")
                        return redirect('/')

                WhoisResult = ReqWho.json()
                if WhoisResult['registered'] != True:
                        context ={
                                'title':'Whois Result',
                                'dnsname':dnsname
                        }
                        return render(request, 'Whois/WhoisResult.html', context)
                else:
                        context = {
                                                'title':'Whois Result',
                                                'dnsname': dnsname,
                                                'WhoisResult': WhoisResult
                        }
                        return render(request, 'Whois/WhoisResult.html', context)

        except:
                context = {
                                        'title':'Whois Result',
                                        'dnsname': dnsname,
                                        'InvalidTld':'InvalidTld',
                }
                return render(request, 'Whois/WhoisResult.html', context)


def WhoisResultJs(request, args):
        dnsname = args
        ApiKey = '6bc09cdadec544090041d43278ed38a0'

        ResultWhois =requests.get("https://jsonwhois.com/api/v1/whois",
        headers={
        "Accept":"application/json",
        "Authorization":f"Token token=<{ApiKey}>"
        },
        params={
        "domain": f"{dnsname}"
        })

        if ResultWhois.status_code != 200: 
                messages.info(request, "Could not get availability state of Domain Name ")
                return redirect('/')
        else:
                WhoisResult = ResultWhois.json()
                print(WhoisResult)
                context = {
                        'title':'Whois Result',
                         'dnsname': dnsname,
                        'WhoisResult': WhoisResult
                }
                return render(request, 'Whois/WhoisResult.html', context)

                



