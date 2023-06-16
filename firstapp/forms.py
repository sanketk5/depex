from django import forms
from django.core import validators
from django.contrib.auth.models import User
from .models import userinfo

def check(value):
    if value[0]!='z':
        raise forms.ValidationError("Start with Z")

class formname(forms.Form):
    name = forms.CharField(validators=[check])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again.")
    text = forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(6)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Email not matched')
        

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserprofileInfo(forms.ModelForm):
    class Meta():
        model = userinfo
        fields = ('portfolio_site', 'pro_pic')