from django.contrib import messages
from django.http import response
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from ipware import get_client_ip, ip
import json, urllib


class IpWithApix(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        client_ip, is_routable = get_client_ip(request)
        if client_ip is None:
            client_ip = "0.0.0.0"

        else:
            if is_routable:
                ip_type = 'public'  
            else:
                ip_type = 'private'

        print(client_ip, ip_type)
        ip_address = client_ip
        # ip_address = "175.156.66.173"
        # ip_address = "103.160.137.1"
        url = f"https://api.ipfind.com/?ip={ip_address}"
        response = urllib.request.urlopen(url)
        client_data = json.loads(response.read())
        client_data['client_ip'] = client_ip
        client_data['ip_type'] = ip_type
        if client_data['country_code'] == 'BD':
            print('Bangladesh')
            messages.info(request, 'Country is Bangladesh and Currency is BDT')
            return redirect("home")
        print(f"{client_data['country_code']}")
        print('Hellow World')
        return Response(client_data)
