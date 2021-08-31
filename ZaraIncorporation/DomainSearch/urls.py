from django.urls import path
from . import views

urlpatterns = [
        path('', views.DomainSearchResultPage, name='DomainSearchResultPage')
]