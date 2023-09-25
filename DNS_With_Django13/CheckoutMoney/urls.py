from os import name
from django.urls import path
from . import views, paypalview

urlpatterns = [
        # path('wasilab-under-maintenance/<str:dnsname>', views.Sorry, name='cart'),
        path('<str:dnsname>/', views.cart, name='cart'),
        path('<str:dnsname>/charge', views.charge, name='charge'),

        path('paypal', paypalview.paypal, name='paypal'),
        path('paypal-confirm', paypalview.paypal_payment_confirm, name='paypal_payment_confirm'),
        path('paypal-auto-renew', paypalview.paypal_auto_renew, name='paypal_auto_renew'),
        path('paypal-auto-renew-confirm', paypalview.paypal_auto_renew_confirm, name='paypal_auto_renew_confirm'),
]