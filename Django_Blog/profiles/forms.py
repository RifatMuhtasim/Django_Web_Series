from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Field('first_name', css_class="container-fluid p-5"),
    #         Field('last_name', css_class="container-fluid"),
    #         Field('email', css_class="container-fluid"),
    # )
    

class UserImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['ProfileImage']