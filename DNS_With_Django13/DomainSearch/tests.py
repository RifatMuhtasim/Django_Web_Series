import argparse
import requests
import time
from django.contrib import messages
from django.shortcuts import redirect

# parser = argparse.ArgumentParser(description='Check Domain For availability. ')
# parser.add_argument('domain', type=str, help='Domain Name to be Checked ')
# args = parser.parse_args()

api_key = "3mM44Ubh7wYhH2_Tt6PiFFof77Kp9n8sYZPV3"
api_secret = "PDPywsWFtpjs9vCbJ3sKL9"
req_headers = {
                "Authorization": f"sso-key {api_key}:{api_secret}",
                'accept': 'application/json' 
}

def DomainCheck(request, args):
        a = args

        # b= f'https://api.ote-godaddy.com/v1/domains/available?domain={a}' 
        # b = f"https://who.is/whois/{a}"
        b = f'https://sugapi.verisign-grs.com/ns-api/2.0/suggest?name={a}'

        req_url = b
        req= requests.get(req_url)

        if req.status_code != 200: 
                messages.info(request, "Could not get availability state of Domain - Status ")
                return redirect('/')
        else:
                response = req.json()
                c= response['results'][0]
                if  c['availability'] == 'registered':
                        messages.info(request, 'NOPE  ... Domain is not available for purchase !')
                        return redirect('/')
                else:
                        messages.info(request, 'OLA ... Domain  is available for purchase !')
                        return redirect('/')


def ReDomainCheck(request, args):
        DomainName = args
        ReResellerID = 1125655
        ReApiKey = '0QiYjWBZGSjbu3ebZ55NEBgYVZMYDLnH'

        ReUrl = f"https://domaincheck.httpapi.com/api/domains/available.json?auth-userid={ReResellerID}&api-key={ReApiKey}&domain-name={DomainName[0:-4]}&tlds={DomainName[-3:]}"

        req = requests.get(ReUrl)

        if req.status_code != 200: 
                messages.info(request, "Could not get availability state of Domain - Status ")
                return redirect('/')
        else:
                response = req.json()
                if  response[f"{DomainName}"]['status'] != 'available':
                        messages.info(request, 'NOPE  ... Domain is not available for purchase !')
                        return redirect('/')
                else:
                        messages.info(request, 'OLA ... Domain  is available for purchase !')
                        return redirect('/')
