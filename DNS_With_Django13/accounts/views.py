import accounts
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decouple import config
import requests
import json

# Create your views here.

def register(request):
        if request.method == 'POST':
                first_name = request.POST['first_name']
                last_name =request.POST['last_name']
                username = request.POST['username']
                email = request.POST['email']
                password1 = request.POST['password1']
                password2 = request.POST['password2']

                if password1 == password2:
                        if User.objects.filter(username = username).exists():
                                messages.info(request, 'UserName is already taken')
                                return redirect('register')

                        if User.objects.filter(email= email).exists():
                                messages.info(request, 'Email name is already taken')
                                return redirect('register')

                        else:
                                user = User.objects.create_user(first_name= first_name, last_name= last_name, username= username, email= email, password=password1)
                                user.save()
                                return redirect('signin')

                else:
                        messages.info(request, 'Your password is not matched')
                        return redirect('register')

        return render(request, 'accounts/register.html')

def signin(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']

                try:
                        user = auth.authenticate(username = User.objects.get(email=username), password= password)
                except:
                        user = auth.authenticate(username = username, password= password)

                if user is not None:
                        auth.login(request, user)
                        return redirect('/')
                else:
                        messages.info(request, 'Somethings wrong in here')
                        return redirect('signin')

        else:
                return render(request, 'accounts/signin.html')

def logout(request):
        auth.logout(request)
        return redirect('/')


@login_required
def update_password(request):
        if request.method != 'POST':
                context = {
                        'title': 'Update Password',
                }                
                return render(request, 'accounts/update_password.html', context)
                
        else:
                old_password = request.POST['old_password']
                new_password1 = request.POST['new_password1']
                new_password2 = request.POST['new_password2']
                client_key = request.POST['g-recaptcha-response']

                secret_key = config('ReCaptchaSecretKey2')
                captcha_data = {
                'secret': secret_key,
                'response': client_key,
                }

                url = f"https://www.google.com/recaptcha/api/siteverify"
                response = requests.post(url=url, data=captcha_data)
                result = response.json()
                print(result)

                if result['success'] != True:
                        messages.info(request, 'please check that you are not a robot')
                        return redirect('re_captcha')

                else:
                        username = request.user.username
                        data = User.objects.get(username = username)

                        if check_password(old_password, data.password) is not True:
                                messages.info(request,'Your Old Password does not matched' )
                                return redirect('update_password')
                        elif new_password1 != new_password2:
                                messages.info(request,'New password and Confirm New Password does not matched' )
                                return redirect('update_password')

                        data.set_password(new_password2)
                        data.save()

                        messages.info(request, 'Password Updated.')
                        auth.logout(request)
                        return redirect('signin')