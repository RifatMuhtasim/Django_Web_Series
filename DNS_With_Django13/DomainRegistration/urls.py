from django.urls import path
from .bktest import backview, frontview
from .bktest.backview import ApiTestSaveView

from . import views, testview

urlpatterns = [
        path('congratulations', views.Congratulations, name='Congratulations'),
        path('<str:dnsname>/domain-register-info', views.ReUserData, name='UploadData'),
        path('save', views.ReDomainApiData, name='DomainApiData'),

        path('api', ApiTestSaveView.as_view(), name='ApiTestSaveView'),
        path('', backview.ApiDataLab, name='ApiDataLab' ),
        # path('save', frontview.DomainApiData, name='DomainApiData'),

        path('test', testview.ApiTestData, name='ApiTestData'),
        path('check/<str:args>', testview.ApiDomainTest, name='ApiDomainTest'),
]