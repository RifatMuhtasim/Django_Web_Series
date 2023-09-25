from django.http import response
from django.shortcuts import redirect, render
from django.contrib import messages
from decouple import config
import requests
import json
from django.core.mail import send_mail

# Create your views here.

def ExtraFunction(request):
    return redirect('home')


def re_captcha(request):
    if request.method != 'POST':
        context = {
            'title': 'Re Captcha',
        }
        return render(request, 'ExtraFunction/recaptcha.html', context)

    else:
        email = request.POST['email']
        password = request.POST['password']

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
            messages.info(request, 'congrates you are not a robot')
            return redirect('home')


def country_tel_no(request):
    if request.method != 'POST': 
        context = {
            'title' : 'Country Telephone Code'
        }
        return render(request, 'ExtraFunction/country_telephone.html', context)

    else:
        return redirect('home')



def email(request):
    try:
        subject  = 'Congratulations ! Now you are the owner of the blackmafia.com Domain'
        message = "Hey, Rifat Muhtasim .\nYou Successfully buy this TabLab.com domain Name from us. \n \n \nTry to login this Website: http://127.0.0.1:8000/accounts/signin \nEmail is : bffmasum@wasilab.com \n  \n \nManage Domain from this Website: https://tabl1125655.myorderbox.com/servlet/LoginServlet?role=customer&currenturl=https://tabl1125655.myorderbox.com \nEmail is : bffmasum@wasilab.com \n\n WasiLab Corporation 2021"
        to_email = 'tablab.bd@gmail.com'

        send_mail(
            subject,
            message,
            to_email,
            ['khandokar19@student.sust.edu']
        )

        messages.info(request, 'Email Send Successfully! ')
        return redirect('home')
    except:
        messages.info(request, 'Sorry ! We Can not send Email Successfully!  ')
        return redirect('home')
        