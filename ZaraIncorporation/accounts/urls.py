from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('register', views.register, name='register'),
        path('signin', views.signin, name='signin'),
        path('logout', views.logout, name= 'logout'),
        path('password-reset', auth_views.PasswordResetView.as_view(template_name='accounts/PasswordResetView.html'), name='PasswordReset'),
        path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name= 'accounts/PasswordResetDoneView.html'), name='password_reset_done'),
        path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'accounts/password_reset_email.html'), name='password_reset_confirm'),
        path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name= 'accounts/password_reset_complete.html'), name='password_reset_complete')
]