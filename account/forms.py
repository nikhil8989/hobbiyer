from django import forms
from django.contrib.auth.models import User
from account.models import user_profile

class user_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control radius','placeholder':'Password'}))
    class Meta:
        model = User
        fields = ('username','password','email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control radius ','placeholder':'Username'}),
            'email' : forms.TextInput(attrs={'class':'form-control radius ','placeholder':'Email'}),
        }

class profile_form(forms.ModelForm):
    class Meta:
        model = user_profile
        exclude = ('user','email')

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control radius','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control radius','placeholder':'Last Name'}),
            'profile_pic': forms.FileInput(attrs={'class':'form-control radius'}),
            'phone': forms.TextInput(attrs={'class':'form-control radius','placeholder':'Phone'}),
            'country': forms.TextInput(attrs={'class':'form-control radius','placeholder':'Country'}),
            'state': forms.TextInput(attrs={'class':'form-control radius','placeholder':'State'}),
            'city': forms.TextInput(attrs={'class':'form-control radius','placeholder':'City'}),
            'dob':forms.DateInput(attrs={'class':'form-control radius','type':'date'}),
            'gender':forms.Select(attrs={'class':'form-control radius'}),
        }