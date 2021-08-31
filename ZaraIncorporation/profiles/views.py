from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from .forms import UserUpdateForm, UserImageUpdateForm
# Create your views here.

@login_required
def profiles(request):
        return render(request, 'profiles/profile.html')

@login_required
def UpdateProfile(request):
        if request.method == 'POST' :
                uform = UserUpdateForm(request.POST, instance= request.user)
                iform = UserImageUpdateForm(request.POST, request.FILES, instance= request.user.profile)  
                if uform.is_valid() and iform.is_valid():
                        uform.save()
                        iform.save()
                        return redirect('profile')
        
        else:
                uform = UserUpdateForm(instance= request.user)
                iform = UserImageUpdateForm(instance= request.user.profile)  
        
        context ={
                'uform': uform,
                'iform': iform,
        }
        return render(request, 'profiles/UpdateProfile.html', context)