from django.shortcuts import render, redirect
from .forms import UserUpdateForm, UserImageUpdateForm
from django.contrib.auth.decorators import login_required
import requests
# Create your views here.

@login_required
def profile(request):
    context = {
        'title': 'Profile'
    }
    return render(request, 'profiles/profile.html', context)

@login_required
def UpdateProfile(request):
    if request.method == 'POST':
        uform= UserUpdateForm(request.POST, instance= request.user)
        iform= UserImageUpdateForm(request.POST, request.FILES, instance= request.user.profile)
        if uform.is_valid() and iform.is_valid():
            uform.save()
            iform.save()
            return redirect('profile')
    
    else:
        uform = UserUpdateForm(instance= request.user)
        iform = UserImageUpdateForm(instance= request.user.profile)

    context = {
        'title': 'Update Profile',
        'uform': uform,
        'iform': iform
    }
    return render(request, 'profiles/updateprofile.html', context)
    
    
    
def ContactId(request):
    url = "https://test.httpapi.com/api/customers/v2/signup.json?auth-userid=1125655&api-key=0QiYjWBZGSjbu3ebZ55NEBgYVZMYDLnH&username=khanz@gmail.com&name=Khandokar Rifat &company=Qasi Corporation&address-line-1=Rustom Pur &city=Sylhet&state=Sylhet&country=BD&zipcode=3100&phone-cc=880&phone=1926337247&lang-pref=en&passwd=%2336Khandokar13"
    response = requests.post(url)
    result = response.json()
    
    if response.status_code != 200:
        reject = result['message']
        context = {
            'reject': reject,
        }
        return render(request, 'profiles/ContactId.html', context)
    else:
        ContactId = result
        context = {
            'ContactId': ContactId,
        }
        return render(request, 'profiles/ContactId.html', context)
    
    
    
    
    
    