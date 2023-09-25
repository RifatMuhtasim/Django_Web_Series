from django.shortcuts import redirect, render
from django.urls.base import reverse
import requests
from UserDetails.models import IcannModel as IM
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import ARecords



ReUserId = 1125655
ReApiKey = '0QiYjWBZGSjbu3ebZ55NEBgYVZMYDLnH'

@login_required
def DnsRecord(request, args):
        DnsName = args
        obj = IM.objects.get(DnsName=DnsName)
        if obj.UserName == request.user.username:
                res = f"https://test.httpapi.com/api/dns/activate.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}"
                rest = requests.post(res)
                result = rest.json()
                print(result)
                if rest.status_code != 200:
                        messages.info(request, f"Sorry!  {rest} . Dns not active ")
                        return redirect('home')

                context = {
                        'title': 'DNS Record',
                        'obj': obj,
                        'DomainName': DnsName,
                }
                return render(request, 'DnsSettings/DnsRecord.html', context)
        else:
                messages.info(request, 'Bad Request!! You are not Owner of this Domain Name')
                return redirect('home')


@login_required
def ARecord(request, DomainName):
        DomainName = DomainName
        obj = IM.objects.get(DnsName=DomainName)
        if obj.UserName == request.user.username:
                if request.method == "POST":
                        TTL = request.POST['TTL']
                        IPv4Value = request.POST['IPv4Value']
                        HostName = request.POST['HostName'].lower()

                        url = f"https://test.httpapi.com/api/dns/manage/add-ipv4-record.json?auth-userid={ReUserId}&api-key={ReApiKey}&domain-name={DomainName}&value={IPv4Value}&host={HostName}&ttl={TTL}"
                        Respone = requests.post(url)
                        Result = Respone.json()
                        print(Result)

                        if Respone.status_code != 200:
                                messages.info(request, f"{Result['message']}")
                                return redirect('home')
                        elif Result['status'] != 'Success':
                                messages.info(request, f"{Result['msg']}")
                                return redirect('home')
                        # else:
                        #         data = ARecords(DomainName=DomainName, TTL =TTL, IPv4Value=IPv4Value, HostName=HostName)
                        #         data.save()
                        #         context = {
                        #                 'title': 'DNS Record',
                        #                 'obj': obj,
                        #                 'DomainName': DomainName,
                        #                 'values': reversed(ARecords.objects.filter(DomainName=DomainName))
                        #         }
                        #         return render(request, 'DnsSettings/ARecords.html', context)
                        return redirect(reverse('ARecords', args=[DomainName]))
                else:
                        urls = f"https://test.httpapi.com/api/dns/manage/search-records.json?auth-userid={ReUserId}&api-key={ReApiKey}&domain-name={DomainName}&type=A&no-of-records=10&page-no=1"
                        Responses = requests.get(urls)
                        Resultsx = Responses.json()
                        # print(Results)
                        items_list = []
                        
                        result_db_no = int(Resultsx['recsindb'])+1
                        for i in range(1, result_db_no):
                                # print(i)
                                res = Resultsx[f'{i}']
                                print(res)
        
                                ttl = res['timetolive']
                                host = res['host']
                                value = res['value']
                                type = res['type']

                                items_list.append([f"{host}", f"{value}", f"{ttl}", f"{type}"])

                        # print(items_list)
                        context = {
                                'title': 'DNS Record',
                                'obj': obj,
                                'DomainName': DomainName,
                                'values': reversed(ARecords.objects.filter(DomainName=DomainName)),
                                'items_list': items_list,
                        }
                        return render(request, 'DnsSettings/ARecords.html', context)
        else:
                messages.info(request, 'Bad Request!! You are not Owner of this Domain Name')
                return redirect('home')


def DeleteARecord(request, DomainName):
        DomainName = request.POST['DnsName']
        HostName = request.POST['HostName']
        IPv4Value = request.POST['IPv4Value']
        # Code  = request.POST['Code']
        # data = ARecords.objects.get(id=Code)

        url = f"https://test.httpapi.com/api/dns/manage/delete-ipv4-record.json?auth-userid={ReUserId}&api-key={ReApiKey}&domain-name={DomainName}&host={HostName}&value={IPv4Value}"
        Response = requests.post(url)
        Result = Response.json()
        print(Result)

        if Response.status_code != 200:
                messages.info(request, f"{Result['message']}")
                return redirect(reverse('ARecords', args=[DomainName]))
        else:
                # data.delete()
                messages.info(request, f"{Result['status']}")
                return redirect(reverse('ARecords', args=[DomainName]))


def ModifyARecord(request, DomainName):
        DomainName = DomainName
        HostName = request.POST['HostName']
        IPv4Value = request.POST['IPv4Value']
        # Code = request.POST['Code']
        NewIPv4Value = request.POST['NewIPv4Value']
        NewTTL = request.POST['NewTTL']
        # data = ARecords.objects.get(id=Code)

        # if NewIPv4Value != data.IPv4Value or NewTTL != data.TTL:
        url = f"https://test.httpapi.com/api/dns/manage/update-ipv4-record.json?auth-userid={ReUserId}&api-key={ReApiKey}&domain-name={DomainName}&host={HostName}&current-value={IPv4Value}&new-value={NewIPv4Value}&ttl={NewTTL}"
        Response = requests.post(url)
        Result = Response.json()
        print(Result)

        if Response.status_code != 200:
                        messages.info(request, f"{Result['message']}")
                        return redirect(reverse('ARecords', args=[DomainName]))
        elif Result['status'] == 'Failed':
                        messages.info(request, f"{Result['msg']}")
                        return redirect(reverse('ARecords', args=[DomainName]))
        else:
                        # db = ARecords.objects.filter(id=Code)
                        # db.update(IPv4Value = NewIPv4Value, TTL = NewTTL)
                        messages.info(request, f"{Result['msg']}")
                        return redirect(reverse('ARecords', args=[DomainName]))
        # else:
        #         messages.info(request, "Nothigs Changed in the value ")
        #         return redirect(reverse('ARecords', args=[DomainName]))

        