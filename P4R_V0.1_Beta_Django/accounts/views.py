from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username= username).exists():
                messages.info(request, 'User Name is Already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is Already Register')
                return redirect('register')
            else:
                user = User.objects.create_user(username= username, email= email, first_name= first_name, last_name= last_name, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Your Password is not Matched')
            return redirect('register')

    context= {
        'title': 'Registration - P4R'
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = auth.authenticate(username= User.objects.get(email=username), password= password)
        except:
            user = auth.authenticate(username= username , password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'Not Matched')
            return redirect('login')

    context= {
        'title': 'Login - P4R'
    }
    return render(request, 'accounts/login.html', context)


def logoutx(request):
    auth.logout(request)
    return redirect('logout')

def logout(request):
    context= {
        'title': 'Logout - P4R'
    }
    return render(request, 'accounts/logout.html', context)