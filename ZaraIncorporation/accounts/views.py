import accounts
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

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
                        return redirect('/')

        else:
                return render(request, 'accounts/signin.html')

def logout(request):
        auth.logout(request)
        return redirect('/')