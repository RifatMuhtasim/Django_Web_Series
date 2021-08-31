from django.shortcuts import render

# Create your views here.

def DomainSearchResultPage(request):
        return render(request, 'DomainSearch/ResultPage.html')
