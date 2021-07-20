from django.shortcuts import render, redirect
from .forms import UserUpdateForm, UserImageUpdateForm
from django.contrib.auth.decorators import login_required
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