from django.shortcuts import redirect, render
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .bkmodels import ApiTestModel
from .serializers import Serializers
import json
import requests


class ApiTestSaveView(APIView):
        permission_classes = (AllowAny,)

        def get(self, request, *args, **kwargs):
                qs = ApiTestModel.objects.all()
                serializers = Serializers(qs, many=True)
                return Response(serializers.data)
                # return redirect('Congratulations')

        def post(self, request, *args, **kwargs):
                serializers = Serializers(data = request.data)
                if serializers.is_valid():
                        serializers.save()
                        return Response(serializers.data)
                        # return redirect('Congratulations')
                else:
                        return Response(serializers.errors)


@api_view()
@permission_classes([AllowAny])
def ApiDataLab(request):
        qp = request.query_params
        data = { 'DnsName': f"{qp['DnsName']}", 'UserName': f"{qp['UserName']}", 'FirstName': f"{qp['FirstName']}",
                'LastName': f"{qp['LastName']}", 'CompanyName': f"{qp['CompanyName']}", 'JobTitle': f"{qp['JobTitle']}", 'Address': f"{qp['Address']}",
                'City': f"{qp['City']}", 'State': f"{qp['State']}", 'Country': f"{qp['Country']}", 'PhoneNumber': f"{qp['PhoneNumber']}",
                'Email': f"{qp['Email']}", 'DomainYear': f"{qp['DomainYear']}", 'DomainAutoRenew': f"{qp['DomainAutoRenew']}", 'DnsStatus': f"{qp['DnsStatus']}",
                'DomainSsl': f"{qp['DomainSsl']}", 'DomainPremium': f"{qp['DomainPremium']}", 'NameServer1': f"{qp['NameServer1']}", 'NameServer2': f"{qp['NameServer2']}",
                'IP': f"{qp['IP']}", 'Currency': f"{qp['Currency']}", 'PriceType': f"{qp['PriceType']}", 'PaymentMethod': f"{qp['PaymentMethod']}",
                'Type': f"{qp['Type']}" }
        url = 'http://127.0.0.1:8000/domain-registration/api'
        api = requests.post(url=url, json=data)
        try: 
                resp = json.loads(api.text)
        except:
                resp = None
        print('WasiLab : ', resp)
        return redirect('ApiTestSaveView')