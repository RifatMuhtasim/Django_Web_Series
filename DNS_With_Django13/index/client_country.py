from django.db.models.fields import NullBooleanField
from django.shortcuts import  redirect, render
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from ipware import get_client_ip, ip
import json, urllib
from .models import IndexBlog

# client_ip_country =  []
# client_ip_country= ""


context = {'IndexBlogs': IndexBlog.objects.all() }

class client_countries(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        global client_ip_country
        client_ip, is_routable = get_client_ip(request)
        if client_ip is None:
            client_ip = "0.0.0.0"

        else:
            if is_routable:
                ip_type = 'public'  
            else:
                ip_type = 'private'

        print(client_ip, ip_type)
        # ip_address = "175.156.66.173"
        ip_address = "103.160.137.1"
        url = f"https://api.ipfind.com/?ip={ip_address}"
        response = urllib.request.urlopen(url)
        client_data = json.loads(response.read())
        client_data['client_ip'] = client_ip
        client_data['ip_type'] = ip_type

        if client_data['country_code'] == 'BD':
            # client_ip_country.append('BD')
            client_ip_country = "BD"
            print(client_ip_country)
            ordering= {'-time'}
            return render(request, 'index/IndexBlog.html', context)

        else:
            # client_ip_country.append('WORLD')
            # return Response(client_data)
            ordering= {'-time'}
            # print(client_ip_country)
            return render(request, 'index/IndexBlog.html', context)