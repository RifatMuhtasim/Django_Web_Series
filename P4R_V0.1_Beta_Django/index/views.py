from django.shortcuts import render
from .models import HomePost

# Create your views here.

def home(request):
    context = {
        'title': 'Pray for Refugees - Home',
        'HomePosts': HomePost.objects.all()
    }
    return render(request, 'index/index.html', context)