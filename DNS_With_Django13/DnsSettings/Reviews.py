from django import contrib
from django.shortcuts import render, redirect
from django.contrib import messages
from requests.models import Response 
from UserDetails.models import IcannModel as IM
import requests, json 
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# ReCustomerId = 23924871
ReCustomerId = 23920350
ReUserId = 1125655
ReApiKey = '0QiYjWBZGSjbu3ebZ55NEBgYVZMYDLnH'

def DomainNameserver(request):
        if request.method == "POST":
                DnsName = request.POST['DnsName']
                obj = IM.objects.get(DnsName = DnsName)
                order_id = obj.OrderId

                haddersx = {
                        'auth-userid': ReUserId,
                        'api-key': ReApiKey,
                }
                datax = {
                        'order-id': order_id,
                        'options': 'NsDetails'
                }
                url = f"https://test.httpapi.com/api/domains/details.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={order_id}&options=NsDetails"
                # urlx = f"https://test.httpapi.com/api/domains/details.json?auth-userid={ReUserId}&api-key={ReApiKey}&"
                response = requests.get(url)
                # response = requests.get(url=urlx, data=datax)
                
                result = response.json()
                print(result)

                if response.status_code != 200:
                        messages.info(request, f"{result['message']}")
                        return redirect('home')
                ns1 = result['ns1']
                ns2= result['ns2']
                context = {
                        'titile': 'DomainNameserver',
                        'Nameserver1': ns1,
                        'Nameserver2': ns2,
                        'DnsName': DnsName,
                }
                return render(request, 'DnsSystem/DomainNameserver.html', context)
        else:
                context = {
                        'title': 'Domain Nameserver',
                }
                return render(request, 'DnsSystem/DomainNameserver.html', context)


def ReNameServerChange(request):
        if request.method == "POST":
                DnsName = request.POST['DnsName']
                Nameserver1 = request.POST['Nameserver1']
                Nameserver2 = request.POST['Nameserver2']
                ns = IM.objects.get(DnsName = DnsName)
                # ns.update(DnsName=DnsName, NameServer1=Nameserver1, NameServer2=Nameserver2)

                # url = f"https://test.httpapi.com/api/dns/manage/add-ns-record.json?auth-userid={ReUserId}&api-key={ReApiKey}&domain-name={DnsName}&value={Nameserver1}&value={Nameserver2}"
                urlx = f"https://test.httpapi.com/api/domains/modify-ns.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={ns.OrderId}&ns={Nameserver1}&ns={Nameserver2}"
                Response = requests.post(urlx)
                res = Response.json()
                print(res)
                if Response.status_code != 200:
                        messages.info(request, f'Problem on NameServer {Response} !')
                        return redirect('home')

                Result = res['actionstatus']
                messages.info(request, f'{Result}')
                return redirect('home')
        
        else:
                messages.info(request, 'Sorry !!')
                return redirect('home')


def re_privacy_protection(request, args):
        DnsName = args
        obj = IM.objects.get(DnsName=DnsName)
        if obj.UserName != request.user.username:
                messages.info(request, 'Sorry !! You are not owner of this domain_name')
                return redirect('home')
        else:
                if request.method != 'POST':
                        url = f"https://test.httpapi.com/api/domains/details.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}&options=DomainStatus"
                        response = requests.get(url)
                        result = response.json()
                        is_privacy_protected = result['isprivacyprotected']
                        print(is_privacy_protected)
                        privacy_result = None
                        click = None
                        if is_privacy_protected == 'false':
                                privacy_result = 'false'
                        else:
                                privacy_result = 'true'
                                click = 'checked'

                        context = {
                                'title': 'Domain Privacy Protection',
                                'obj': obj,
                                'privacy_result': privacy_result,
                                'click': click,
                                'args': DnsName,
                        }
                        return render(request, 'DnsSettings/privacy_protection.html', context)

                else:
                        DnsName = request.POST['DnsName']
                        protect_privacy = request.POST['result']

                        urlc = f"https://test.httpapi.com/api/domains/modify-privacy-protection.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}&protect-privacy={protect_privacy}&reason=somereason"
                        responsec = requests.post(urlc)
                        if responsec.status_code != 200:
                                messages.info(request, 'Somethings Wrong')
                                return redirect('home')

                        resultc = responsec.json()
                        # print(resultc)
                        messages.info(request, resultc['actionstatus'])
                        return redirect(reverse('re_privacy_protection', args=[DnsName]))



def domain_secret_key(request, args):
        domain_name = args 
        obj = IM.objects.get(DnsName = domain_name)

        if obj.UserName != request.user.username:
                messages.info(request, 'You are not this owner of this domain name')
                return redirect('home')

        else:
                url = f"https://test.httpapi.com/api/domains/details.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}&options=OrderDetails"
                response = requests.get(url)

                if response.status_code != 200:
                        messages.info(request, 'SOS')
                        return redirect('home')

                result = response.json()['domsecret']
                print(result)

                context = {
                        'title': 'Domain Secret Key',
                        'obj': obj,
                        'domain_secret_key': result,
                }
                return render(request, 'DnsSettings/domain_secret_key.html', context)


@login_required
def domain_theft_protectionx(request, args):
        domain_name = args
        obj = IM.objects.get(DnsName = domain_name)

        if obj.UserName != request.user.username:
                messages.info(request, 'You are not owner of this Domain Name ')
                return redirect('home')
        else:
                if request.method != 'POST':
                        url_check = f"https://test.httpapi.com/api/domains/locks.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}"
                        response = requests.get(url_check)
                        if response.status_code != 200:
                                messages.info(request, 'somethings wrong in here')
                                return redirect('home')

                        result = response.json()
                        print(result)
                        lock_result = None
                        click = None
                        try:
                                if result['transferlock'] == True or result['customerlock'] == True:
                                        lock_result = True
                                        click = 'checked'
                                else:
                                        lock_result = False
                        except:
                                lock_result=False

                        context = {
                                'title': 'Domain Theft Protection',
                                'obj': obj,
                                'lock_result': lock_result,
                                'click': click,
                                'args': domain_name,
                        }
                        return render(request, 'DnsSettings/theft_protection.html', context)
                else:
                        rex = request.POST['result']
                        lock_result = None
                        click = None
                        if rex == 'True':
                                enable_url = f"https://test.httpapi.com/api/domains/enable-theft-protection.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}"
                                enable_url_response = requests.post(enable_url)
                                print(enable_url_response.json())
                                lock_result = True
                                click = 'checked'

                        else:
                                disable_url = f"https://test.httpapi.com/api/domains/disable-theft-protection.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}"
                                disable_url_response = requests.post(disable_url)
                                dr = disable_url_response.json()
                                print(dr)
                                lock_result = False
                        # return redirect(reverse('domain_theft_protectionx', args=[domain_name]))
                        context = {
                                'title': 'Domain Theft Protection',
                                'obj': obj,
                                'lock_result': lock_result,
                                'click': click,
                                'args': domain_name,
                        }
                        return render(request, 'DnsSettings/theft_protection.html', context)


def delete_domain_name(request, args):
        domain_name = args
        obj = IM.objects.get(DnsName = domain_name)
        if obj.UserName != request.user.username:
                messages.info(request, 'You are not owner of this domain ')
                return redirect('home')
        

        context = {
                        'title': 'Delete Domain Name',
                        'obj': obj,
                        'args': domain_name,
        }
        return render(request, 'DnsSettings/delete_domain.html', context)


def delete_confirm(request, args):
        domain_name =  args
        obj = IM.objects.get(DnsName = domain_name)

        url = f"https://test.httpapi.com/api/domains/delete.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}"
        response = requests.post(url)
        result = response.json()
        print(result)

        try:
                msg = result['status']
                messages.info(request, f"Delete Domain Name: {msg}")
                return redirect('home')
        except:
                msg = result['message']
                messages.info(request, f"{msg}")
                return redirect('home')