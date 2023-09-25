from django.contrib import messages
from django.contrib.messages.api import info
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from DnsSettings.Reviews import ReApiKey, ReUserId
from UserDetails.models import IcannModel as IM
from UserDetails.models import DnsInformation as DnsInfo
from .models import DnsServer, DnsManRecord, DnsEmailForward, DnsIdPros, DnsRegisterPrivateNameserver
import requests
import time
# Create your views here.

@login_required
def DomainName(request):
        Username = None
        if request.user.is_authenticated:
                Username = request.user.username
                userx = IM.objects.filter(UserName = Username)
                context = {
                        'title': 'My Domain Name',
                        'objs': reversed(userx),
                }
                return render(request, 'DnsSystem/DomainName.html', context)

        else:
                context = {
                        'title': 'My Domain Name',
                }
                return render(request, 'DnsSystem/DomainName.html' , context)

def DnsArgs(request):
        if request.method=='POST':
                DnsName= request.POST['DnsName']
                username = request.user.username
                obj = IM.objects.get(DnsName=DnsName)
                objn = obj.UserName
                if  username == objn:
                        return redirect(reverse('DnsSettings', args =[DnsName]))
                else:
                        messages.info(request, 'Sorry You can not Edit this Domain Settings !')
                        return redirect('/')

@login_required
def DnsSettings(request, args):
        DnsName = args
        oview = IM.objects.get(DnsName = DnsName)
        if request.user.username == oview.UserName:
                context={
                        'title':'DNS Settings',
                        'oview': oview,
                        'args':args
                }
                return render(request, 'DnsSystem/DnsSettings.html', context)
        else:
                messages.info(request, 'Sorry You are not Eligible  Person for this Domain Name!')
                return redirect('/')

        

@login_required
def DomainNameserver(request):

        if request.method == "POST":
                DnsName = request.POST['DnsName']
                obj = IM.objects.get(DnsName = DnsName)

                Nameserver1 = obj.NameServer1
                Nameserver2 = obj.NameServer2

                context = {
                        'title': 'Domain Nameserver',
                        'DnsName': DnsName,
                        'Nameserver1': Nameserver1,
                        'Nameserver2': Nameserver2,
                }
                return render(request, 'DnsSystem/DomainNameserver.html', context)

        else:
                context = {
                        'title': 'Domain Nameserver',
                }
                return render(request, 'DnsSystem/DomainNameserver.html', context)

@login_required
def NameserverConfirm(request):
        Username = None
        if request.user.is_authenticated:
                Username = request.user.username

        if request.method == "POST":
                DnsName = request.POST['DnsName']
                Nameserver1 = request.POST['Nameserver1']
                Nameserver2 = request.POST['Nameserver2']

                ns = IM.objects.filter(DnsName = DnsName)
                ns.update(DnsName=DnsName, NameServer1=Nameserver1, NameServer2=Nameserver2)
                messages.info(request, 'Name Server Update Successfully !')
                return redirect('home')
        
        else:
                return redirect('home')


def DnsAddson(request):
        if request.method=="POST":
                DnsName = request.POST['DnsName']
                obj = IM.objects.get(DnsName = DnsName)
                objn = obj.DnsName
                if DnsIdPros.objects.filter(DnsName = DnsName).exists():
                        context={
                                'title':'Addson',
                                'obj': obj,
                                'idpro':DnsIdPros.objects.get(DnsName=objn),
                                }
                        return render(request, 'DnsSystem/DnsAddson.html', context)
                else:
                        context={
                                'title':'Addson',
                                'obj': obj,
                                # 'idpro':DnsIdPros.objects.get(DnsName=objn),
                                }
                        return render(request, 'DnsSystem/DnsAddson.html', context)

def DnsManagement(request):
        DnsName = request.POST['DnsName']
        obj = IM.objects.get(DnsName= DnsName)

        context={
                'title':'Dns Management',
                'obj': obj,
                'Dres': DnsManRecord.objects.filter(DnsName=DnsName)
        }
        return render(request, 'DnsSystem/DnsManagement.html', context)

def DnsMangementRecord(request):
        username = None
        if request.user.is_authenticated:
                username = request.user.username
        if request.method=="POST":
                DnsName = request.POST['DnsName']
                RecordType = request.POST['RecordType']
                HostName= request.POST['HostName']
                IpAddress = request.POST['IpAddress']
                Ttl = request.POST['Ttl']
                obj = IM.objects.get(DnsName = DnsName)

                DnsV = DnsManRecord(DnsName=DnsName, username=username, RecordType=RecordType, HostName=HostName, IpAddress=IpAddress, Ttl=Ttl)
                DnsV.save()
                context={
                        'title':'Dns Record',
                        'obj':obj,
                        'Dres': DnsManRecord.objects.filter(DnsName=DnsName)
                 }
                return render(request, 'DnsSystem/DnsManagement.html', context)

        else:
                return redirect('home')

def DnsDeleteRecord(request):
        if request.method == "POST":
                DnsName =request.POST['DnsName']
                Code = request.POST['Code']
                DnsDe = DnsManRecord.objects.get(id=Code)
                DnsDe.delete()

                obj = IM.objects.get(DnsName = DnsName)
                context={
                        'title':'Dns Record',
                        'obj':obj,
                        'Dres': DnsManRecord.objects.filter(DnsName=DnsName)
                }
                return render(request, 'DnsSystem/DnsManagement.html', context)

def DnsEmailForwards(request):
        if request.method == "POST":
                DnsName= request.POST['DnsName']
                obj = IM.objects.get(DnsName=DnsName)
      
                context = {
                        'title':'Email Forward',
                        'obj':obj,
                        'objxs': DnsEmailForward.objects.filter(DnsName=DnsName)
                }   
                return render(request, 'DnsSystem/DnsEmailForward.html', context)        

def DnsEmailForwardsSave(request):
        if request.method == "POST":
                DnsName = request.POST['DnsName']
                prefix = request.POST['prefix']
                forward= request.POST['forward']
                username = request.user.username
                sd = DnsEmailForward(DnsName=DnsName, username=username, prefix=prefix, forward=forward)
                sd.save()
                messages.info(request, 'Congratulations! We Forward your Email')
                return redirect('home')
                

def DnsIdPro(request):
        if request.method=='POST':
                DnsName = request.POST['DnsName']
                IdPro = request.POST['IdPro']
                username = request.user.username

                if DnsIdPros.objects.filter(DnsName = DnsName).exists():
                        ns = DnsIdPros.objects.filter(DnsName = DnsName)
                        ns.update(DnsName=DnsName, IdPro=IdPro, username=username)
                        messages.info(request, 'We successfully Update your Database')
                        return redirect('home')
                else:
                        save = DnsIdPros(DnsName=DnsName, IdPro=IdPro, username=username)
                        save.save()
                        messages.info(request, 'Congratulations! We just Saved your Database')
                        return redirect('home')
                

# Private Child  NAMESERVER Url modification
def PrivateNameserver(request, args):
        DnsName = args
        obj = IM.objects.get(DnsName= DnsName)
        if request.user.username != obj.UserName:
                messages.info(request, 'Sorry You are not Eligible  Person for this Domain Name!')
                return redirect('/')

        else:
                url = f"https://test.httpapi.com/api/domains/details.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}&options=All"
                response = requests.get(url)
                result = response.json()['cns']
                items = result.items()
                for a,b in items:
                                print(a, b)

                context={
                        'title': 'Private Nameserver',
                        'obj':obj,
                        'args':args,
                        'cnsl': reversed(items),
                }
                return render(request, 'DnsSystem/DnsPrivateNameserver.html', context)



def RegisterPrivateNameserver(request, args):
        DnsName = args
        obj = IM.objects.get(DnsName=DnsName)
        if request.user.username == obj.UserName:
                if request.method=="POST":
                        Nameserver = request.POST['Nameserver']
                        NameserverIp = request.POST['NameserverIp']
                        newNameserver = Nameserver +'.' +DnsName
                        username = request.user.username

                        url = f"https://test.httpapi.com/api/domains/add-cns.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}&cns={newNameserver}&ip={NameserverIp}"
                        response = requests.post(url)
                        result = response.json()
                        print(result)

                        try:
                                msg = result['actionstatusdesc']
                                messages.info(request, f"{msg}")
                                return redirect(reverse('DnsPrivateNameserver', args=[DnsName]))
                        except:
                                msg = result['message']
                                messages.info(request, f"{msg}")
                                return redirect(reverse('DnsPrivateNameserver', args=[DnsName]))

                        # if DnsRegisterPrivateNameserver.objects.filter(Nameserver=Nameserver, DnsName=DnsName).exists() :
                        #         messages.info(request, 'Your Nameserver is already Exists')
                        #         return redirect(reverse('DnsPrivateNameserver', args=[DnsName]))
                        # else:                        
                        #         db = DnsRegisterPrivateNameserver(DnsName=DnsName, Nameserver=newNameserver, NameserverIp=NameserverIp, username=username )
                        #         db.save()
                        #         messages.info(request, 'Congratulations! We saved your Nameserver')
                        #         return redirect(reverse('DnsPrivateNameserver', args=[DnsName]))
                else:
                        messages.info(request, 'Sorry You are not Eligible  Person for this Domain Name!')
                        return redirect('/')

def ModifyPrivateNameserver(request, args):
        if request.method =="POST":
                DnsName = args
                obj = IM.objects.get(DnsName=DnsName)
                username = request.user.username
                Nameserver = request.POST['Nameserver']
                NameserverIp = request.POST['NameserverIp']
                NewNameserverIp  = request.POST['NewNameserverIp']

                if request.user.username == obj.UserName:
                        Id = DnsRegisterPrivateNameserver.objects.filter(DnsName=DnsName, username=username, Nameserver= Nameserver, NameserverIp = NameserverIp)
                        if Id.exists():
                                ud = DnsRegisterPrivateNameserver.objects.filter(Nameserver = Nameserver)
                                ud.update(DnsName=DnsName, username=username, Nameserver=Nameserver, NameserverIp = NewNameserverIp)
                                messages.info(request, 'Congratulations ! You Changed your Private Nameserver Ip Address')
                                return redirect(reverse('DnsPrivateNameserver', args=[DnsName]))
                        else:
                                messages.info(request, "We do not found your Private Nameserver")
                                return redirect(reverse('DnsPrivateNameserver', args=[DnsName]))
                else:
                        messages.info(request, 'Sorry You are not Eligible  Person for this Domain Name!')
                        return redirect('/')


def DeletePrivateNameserver(request, args):
        if request.method == "POST":
                DnsName = args
                obj = IM.objects.get(DnsName=DnsName)
                username = request.user.username
                Nameserver = request.POST['Nameserver']
                NameserverIp = request.POST['NameserverIp']
                newNameserver = Nameserver+'.' +DnsName

                url = f"https://test.httpapi.com/api/domains/delete-cns-ip.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}&cns={newNameserver}&ip={NameserverIp}"
                response = requests.post(url)
                result = response.json()
                print(result)
                try:
                        msg = result['actionstatusdesc']
                        messages.info(request, f"{msg}")
                        return redirect(reverse('DnsPrivateNameserver', args=[DnsName]))
                except:
                        msg = result['message']
                        messages.info(request, f"{msg}")
                        return redirect(reverse('DnsPrivateNameserver', args=[DnsName]))

                # if username == obj.UserName:
                #         if DnsRegisterPrivateNameserver.objects.filter(Nameserver=Nameserver, DnsName=DnsName).exists():
                #                 de = DnsRegisterPrivateNameserver.objects.filter(Nameserver=Nameserver)
                #                 de.delete()
                #                 messages.info(request, 'We successfully Delete Your Private Name server')
                #                 return redirect(reverse('DnsPrivateNameserver', args=[DnsName]))
                #         else:
                #                 messages.info(request, 'We do not found your Private Nameserver')
                #                 return redirect(reverse('DnsPrivateNameserver', args=[DnsName]))

                # else:
                #         messages.info(request, 'Sorry You are not Eligible  Person for this Domain Name!')
                #         return redirect('/')


@login_required
def DnsAutoRenew(request):
        if request.method=="POST":
                DnsName = request.POST['DnsName']
                obj = IM.objects.get(DnsName= DnsName)

                urlx = f"https://test.httpapi.com/api/domains/details-by-name.json?auth-userid={ReUserId}&api-key={ReApiKey}&domain-name={DnsName}&options=All"
                resultx = requests.get(urlx).json()
                if resultx['currentstatus'] == 'InActive':
                        messages.info(request, 'Your Domain Name Is Inactive. Please Check your Email and Active this Domain Name')
                        return redirect('home')

                url = f"https://test.httpapi.com/api/domains/details-by-name.json?auth-userid={ReUserId}&api-key={ReApiKey}&domain-name={DnsName}&options=OrderDetails"
                result = requests.get(url).json()
                # print(result)

                try:
                        msg = result['message']
                        messages.info(request, f"{msg}")
                        return redirect('home')

                except:
                        endtime = int(result['endtime'])
                        expire_time = time.strftime('%d %b %Y  , %I:%M %p', time.localtime(endtime))

                context={
                        'title':'Auto Renew',
                        'obj':obj,
                        'DnsName': DnsName,
                        'expire_time': expire_time,
                        'exp_time': result['endtime'],
                }
                return render(request, 'DnsSystem/DnsAutoRenew.html', context)