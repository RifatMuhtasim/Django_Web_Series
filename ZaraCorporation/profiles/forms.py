from django import forms
from django.contrib.auth.models import User
from .models import profile

class UserUpdateForm(forms.ModelForm):
        class Meta:
                model= User
                fields = ['first_name', 'last_name', 'username', 'email']

class UserImageUpdateForm(forms.ModelForm):
        class Meta:
                model= profile
                fields = ['image']

