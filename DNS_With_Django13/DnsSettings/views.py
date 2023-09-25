from django.http import response
from django.shortcuts import redirect, render
from DnsSettings.Reviews import ReApiKey, ReUserId
from UserDetails.models import IcannModel as IM
from accounts.models import CustomerInfo as CI
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests
from django.urls import reverse

# Create your views here.
ReUserId = 1125655
ReApiKey = '0QiYjWBZGSjbu3ebZ55NEBgYVZMYDLnH'

def domain_name_contact_information(request, args):
    domain_name = args 
    obj = IM.objects.get(DnsName = domain_name)
    if request.user.username != obj.UserName:
        messages.info(request, 'You are not eligible person for this Domain Name')
        return redirect('home')

    url_registant = f"https://test.httpapi.com/api/domains/details.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}&options=RegistrantContactDetails"
    response_registant = requests.get(url_registant)
    registant = response_registant.json()['registrantcontact']
    # print(registant)

    url_admin = f"https://test.httpapi.com/api/domains/details.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}&options=AdminContactDetails"
    response_admin = requests.get(url_admin)
    admin = response_admin.json()['admincontact']
    # print(admin)

    context = {
        'title': 'Domain Contact Information',
        'obj': obj,
        'ri': registant,
        'ai': admin,
        'dnsname': domain_name,
        're_name': registant['name'], 're_company': registant['company'], 're_email': registant['emailaddr'], 're_country': registant['country'], 're_city': registant['city'], 're_zip': registant['zip'], 're_address1': registant['address1'], 're_address2': registant['address2'], 're_phonecc': registant['telnocc'], 're_phonenumber': registant['telno'],
        'ad_name': admin['name'], 'ad_company': admin['company'], 'ad_email': admin['emailaddr'], 'ad_country': admin['country'], 'ad_city': admin['city'], 'ad_zip': admin['zip'], 'ad_address1': admin['address1'], 'ad_address2': admin['address2'], 'ad_phonecc': admin['telnocc'], 'ad_phonenumber': admin['telno'],
    }
    return render(request, 'DnsSettings/dns_information.html', context)

@login_required
def domain_name_list(request):
    username = request.user.username
    customer_info = CI.objects.get(UserName = username)
    customer_id = customer_info.CustomerId
    url = f"https://test.httpapi.com/api/domains/search.json?auth-userid={ReUserId}&api-key={ReApiKey}&no-of-records=100&page-no=1 &customer-id={customer_id}"
    response = requests.get(url)
    result = response.json()

    items = []
    result_db_no = int(result['recsonpage'])+1
    for i in range(1 , result_db_no):
        res = result[f'{i}']
        domain_name = res['entity.description']
        orders_time = res['orders.timestamp'][0:10]
        auto_renew = res['orders.autorenew']
        is_active = res['entity.currentstatus']
        items.append([f'{domain_name}', f'{orders_time}', f'{auto_renew}', f'{is_active}'])

    items.reverse()
    # print(items)
    context = {
        'title': 'Domain List',
        'items': items,
        'obj': items,
    }
    return render(request, 'DnsSystem/DomainName.html', context)

        
def domain_forward(request, args):
    domain_name = args
    obj = IM.objects.get(DnsName = domain_name)
    if request.user.username != obj.UserName:
        messages.info(request, 'You are not eligible person for this Domain Name .')
        return redirect('home')
    
    check_url = f"https://test.httpapi.com/api/domainforward/details.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}&include-subdomain=true"
    check_response = requests.get(check_url)
    check_result = check_response.json()
    forward_list = []

    for i in check_result:
        domain = check_result[f'{i}']
        domain_name = i
        forwards = domain['forward']
        is_name_maskin = domain['urlmasking']

        forward_list.append([domain_name, forwards, is_name_maskin])

    print(forward_list)
    
    context = {
        'title':'Domain Forwarding Service',
        'obj': obj,
        'DomainName': obj.DnsName,
        'click': 'checked',
        'forward_list': forward_list,
    }
    return render(request, 'DnsSettings/domain_forward.html', context)


def add_domain_forward(request, DomainName):
    DnsName = str(DomainName),
    print(DnsName)
    obj = IM.objects.get(DnsName = DomainName)
    if request.user.username != obj.UserName:
        messages.info(request, 'You are not eligible person for this Domain Name')
        return redirect('home')

    sub_domain_prefix = request.POST['sub_domain_prefix']
    forward_to = request.POST['forward_to']
    url_masking = request.POST['url_masking']
    add_url = f"https://test.httpapi.com/api/domainforward/activate.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}&sub-domain-prefix={sub_domain_prefix}&forward-to={forward_to}&url-masking={url_masking}"
    add_response = requests.post(add_url)
    add_result = add_response.json()
    print(add_result)

    return redirect(reverse('domain_forward', args=[obj.DnsName]))


@login_required
def disable_forward(request, DomainName):
    obj = IM.objects.get(DnsName = DomainName)
    if request.user.username != obj.UserName: 
        messages.info(request, 'You are not eligiable person for this Domain Name')
        return redirect('home')
    
    name = request.POST['Name']
    domain_name = request.POST['DomainName']
    len_name = len(name)
    len_domain_name = len(domain_name)+1
    domain_int = int(len_name-len_domain_name)
    print(domain_int)

    if domain_int == -1:
        subx_domain_prefix = ''
        # remove_domain = f"https://test.httpapi.com/api/domainforward/delete.json?auth-userid={ReUserId}&api-key={ReApiKey}&domain-name={obj.DnsName}"
        removex_sub_domain = f"https://test.httpapi.com/api/domainforward/sub-domain-record/delete.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}&sub-domain-prefix={subx_domain_prefix}"
        domain_response = requests.post(removex_sub_domain)
        domain_remove_result = domain_response.json()

        if domain_response.status_code != 200:
            messages.info(request, f"{domain_remove_result['message']}")
            return redirect('home')
        return redirect(reverse('domain_forward', args=[obj.DnsName]))
        
    else:
        subs_domain_prefix = name[0:domain_int]
        print(subs_domain_prefix)

        remove_sub_domain = f"https://test.httpapi.com/api/domainforward/sub-domain-record/delete.json?auth-userid={ReUserId}&api-key={ReApiKey}&order-id={obj.OrderId}&sub-domain-prefix={subs_domain_prefix}"
        response_remove_sub_domain = requests.post(remove_sub_domain)
        result_remove_sub_domain = response_remove_sub_domain.json()

        if response_remove_sub_domain.status_code != 200:
                messages.info(request, f"{result_remove_sub_domain['message']}")
                return redirect('home')
        return redirect(reverse('domain_forward', args=[obj.DnsName]))


        