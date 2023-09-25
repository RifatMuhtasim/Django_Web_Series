from django.shortcuts import redirect, render
from django.http import JsonResponse
import requests
import json

# Create your views here.

def ReCountry(request):
        # https://api.duoservers.com/?auth_username=store230008&auth_password=alpha&section=countries&command=get&TEST_MODE=1&return_type=json
        FirstName = 'Rifat'
        LastName = 'Muhtasim'
        CompanyName = 'WasiCorporation'

        data = {
                'FirstName': FirstName,
                'LastName': LastName,
                'CompanyName': CompanyName,
        }
        
        username = 'store230008'
        password = 'alpha'
        section = 'countries'
        command = 'get'
        type='json'

        url = f'https://api.duoservers.com/?auth_username={username}&auth_password={password}&section={section}&command={command}&return_type={type}&TEST_MODE=1'
        api = requests.post(url = url, data= data)
        resp = json.loads(api.text)
        print(resp)
        return redirect('/')