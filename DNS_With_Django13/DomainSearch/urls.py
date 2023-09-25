from django.urls import path
from .UrlsDomainSearch import dom_check
from DomainSearch import UrlsDomainSearch, tests
from . import views

urlpatterns = [
        path('', views.DomainSearchName, name='DomainSearchResultPage'),
        # path('<str:args>/', views.DomainSearchResult, name='DomainSearchResult'),
        path('<str:args>/', dom_check.as_view(), name='DomainSearchResult'),
        # path('<str:args>/', UrlsDomainSearch.ReDomainCheckUrls, name='DomainSearchResult'),
        path('test/<str:args>', tests.ReDomainCheck, name='DomainCheck')
]