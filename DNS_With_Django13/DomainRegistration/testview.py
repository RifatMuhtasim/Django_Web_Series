from django.shortcuts import redirect, render
from django.contrib import messages
import requests, json

from requests.models import Response 
from UserDetails.models import IcannModel as IM


username = 'store230008'
password = 'alpha'

def ApiTestData(request):
        IPSG = '206.189.92.74'
        port = 'SG = 38888, BD = 1080'
        IPBD = '180.210.222.237'

        DomainName = 'rifatmuhtasim.com'

        urlx = f"https://api.duoservers.com/?auth_username={username}&auth_password={password}&section=order&command=create&plan=1&country=BD&firstname=Tablab&lastname=Corporation&email=tablab.bd@gmail.com&phone=555555555&address1=EasternPlaza&state=Sylhet&city=Sylhet&zip=1234&domains[0][type]=register&domains[0][sld]={DomainName[0:-4]}&domains[0][tld]={DomainName[-3:]}&domains[0][period]=1&domains[0][epp]=&domains[0][contacts]=&domains[0][extra_attributes]=&fax=&currency=USD&period=12&ip={IPSG}&cancel_url=http://127.0.0.1&return_url=http://127.0.0.1/domain-registration/congratulations&payment_method=2co&signup_from=template16&return_type=json"

        response = requests.get(urlx)
        result = response.json()
        print(result)
        if response.status_code != 200 or result['1']['error_code'] == 1:
                messages.info(request, 'FAILED!! Cloud Error !! ')
                return redirect('home')
        else:
                # return redirect('Congratulations')
                reurl = result['1']['redirect_url']
                print(reurl)
                return redirect(reurl)


def ApiDomainTest(request, args):
        sld = args

        url = f"https://api.duoservers.com/?auth_username={username}&auth_password={password}&section=domains&command=check&name={sld}&tlds[0]=com&tlds[1]=net&tlds[2]=org&tlds[3]=biz&tlds[4]=xyz&return_type=json"

        response = requests.get(url)
        result = response.json()
        print(result)
        messages.info(request, 'We check your Domain Name. 1 Means Not Available 0 Means Available ')
        return redirect('home')