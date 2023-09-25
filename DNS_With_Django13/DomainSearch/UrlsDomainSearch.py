from django.http import response
import requests
from django.contrib import messages
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from ipware import get_client_ip, ip
import json, urllib


def DomainCheckByUrls(request, args):
        dnsname = args
        name = dnsname[0:-4]
        tld = dnsname[-4:]

        DomainList = [f'{name}.com', f'{name}.org', f'{name}.net', f'{name}.biz', f'{name}.xyz']

        avis = []
        for Domain in DomainList:
                # 'https://sugapi.verisign-grs.com/ns-api/2.0/suggest?name={Domain}'
                Checkurl = f'https://sugapi.verisign-grs.com/ns-api/2.0/suggest?name={Domain}'
                
                ReqUrl = requests.get(Checkurl)
                response = ReqUrl.json()
                results = response['results'][0]

                if results['availability'] == 'registered' :
                        avis.append([f'{Domain}', False])
                else:
                        avis.append([f'{Domain}', True])

        context = {
                'DomainSearch': dnsname, 
                'dnsname':dnsname,
                'name':name,
                'tld':tld,
                'avis': avis,
        }
        return render(request, 'DomainSearch/UrlResultPage.html', context)


def DomainCheckUrls(request, args):
        dnsname = args
        name = dnsname[0:-4]
        tld = dnsname[-4:]
        
        avis = []
        # 'https://sugapi.verisign-grs.com/ns-api/2.0/suggest?name={Domain}'
        Checkurl = f'https://sugapi.verisign-grs.com/ns-api/2.0/suggest?name={dnsname}'
                
        ReqUrl = requests.get(Checkurl)
        response = ReqUrl.json()
        results = response['results']
        
        for result in results:
                if result['availability'] == 'registered' :
                        res = result['name']
                        avis.append([f'{res}', False])
                else:
                        res = result['name']
                        avis.append([f'{res}', True])

        context = {
                'DomainSearch': dnsname, 
                'dnsname':dnsname,
                'name':name,
                'tld':tld,
                'avis': avis,
        }
        return render(request, 'DomainSearch/UrlResultPage.html', context)


def ReDomainCheckUrls(request, args):
        DomainName = args
        sld = DomainName[0:-4]
        tld = DomainName[-4:]

        ReUrl = f"https://test.httpapi.com/api/domains/v5/suggest-names.json?auth-userid=1125655&api-key=0QiYjWBZGSjbu3ebZ55NEBgYVZMYDLnH&keyword={sld}&tld-only=com&tld-only=org&tld-only=net&tld-only=xyz&tld-only=biz"

        Request = requests.get(ReUrl)
        Results = Request.json()
        avis = []
        for Result in Results:
                x = Results[f'{Result}']
                if x['status'] == 'available':
                        avis.append([Result, True])
                else:
                        avis.append([Result, False])

        
        context = {
                'DomainSearch': DomainName, 
                'dnsname':DomainName,
                'name': sld,
                'tld':tld,
                'avis': avis,
                'price': "$13"
        }
        return render(request, 'DomainSearch/UrlResultPage.html', context)


# Some Url where can we  search 

# url = f'https://resellertest.enom.com/interface.asp?command=check&sld={name}&tld={tld}&uid=resellid&pw=resellpw&responsetype=json'

# https://resellertest.enom.com/interface.asp?UID=resellid&PW=resellpw&SLD=dotlab&TLD=com&Command=check&responsetype=json&version=2&includeprice=1&includeproperties=1&includeeap=1

#Domain Registration: https://test.httpapi.com/api/domains/register.xml?auth-userid=1125655&api-key=0QiYjWBZGSjbu3ebZ55NEBgYVZMYDLnH&domain-name=tablabcorp.com&years=1&ns=dns3.parkpage.foundationapi.com&ns=dns4.parkpage.foundationapi.com&customer-id=23924871&reg-contact-id=100707544&admin-contact-id=100707544&tech-contact-id=100707544&billing-contact-id=100707544&invoice-option=NoInvoice&discount-amount=0.0 

#contact = https://test.httpapi.com/api/contacts/add.json?auth-userid=1125655&api-key=0QiYjWBZGSjbu3ebZ55NEBgYVZMYDLnH&name=TabLab&company=TabLab Corporation&email=tablab.bd@gmail.com&address-line-1=EasternPlaza&city=Sylhet&country=BD&zipcode=3100&phone-cc=880&phone=880534577773&customer-id=23924871&type=Contact 


class dom_check(APIView):
        permission_classes = (AllowAny,)
        def get(self, request, args, format=None):
                try:
                        client_ip, is_routable = get_client_ip(request)
                        if client_ip is None:
                                client_ip = "0.0.0.0"

                        else:
                                if is_routable:
                                        ip_type = 'public'  
                                else:
                                        ip_type = 'private'

                        print(client_ip, ip_type)
                        # ip_address = client_ip
                        # ip_address = "175.156.66.173"
                        ip_address = "103.160.137.1"
                        url = f"http://ip-api.com/json/{ip_address}"
                        # url = f"https://api.ipfind.com/?ip={ip_address}"
                        response = urllib.request.urlopen(url)
                        client_data = json.loads(response.read())
                        # client_data['client_ip'] = client_ip
                        # client_data['ip_type'] = ip_type

                        # if client_data['country_code'] == 'BD':
                        if client_data['countryCode'] == 'BD':
                                price = '1200 Taka'

                        else:
                                price = '$12 USD'
                        
                except:
                        price = '$13 USD'

                finally:
                        DomainName = args
                        sld = DomainName[0:-4]
                        tld = DomainName[-4:]

                        ReUrl = f"https://test.httpapi.com/api/domains/v5/suggest-names.json?auth-userid=1125655&api-key=0QiYjWBZGSjbu3ebZ55NEBgYVZMYDLnH&keyword={sld}&tld-only=com&tld-only=org&tld-only=net&tld-only=xyz&tld-only=biz"

                        Request = requests.get(ReUrl)
                        Results = Request.json()
                        avis = []
                        for Result in Results:
                                x = Results[f'{Result}']
                                if x['status'] == 'available':
                                        avis.append([Result, True])
                                else:
                                        avis.append([Result, False])

                        
                        context = {
                                'DomainSearch': DomainName, 
                                'dnsname':DomainName,
                                'name': sld,
                                'tld':tld,
                                'avis': avis,
                                'price': price,
                        }
                        return render(request, 'DomainSearch/UrlResultPage.html', context)
                