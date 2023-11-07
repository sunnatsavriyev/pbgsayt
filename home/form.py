from django import forms
from .models import *



# exclude bu kerak emasi uchun


class LoginForm(forms.Form):
    UserName = forms.CharField(
        label='User Name',
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs = {'plaseholder':'User Name'}),
    )
    password = forms.CharField(
        label='password',
        min_length=4,
        max_length=50,
        widget=forms.TextInput(attrs={'plaseholder':'password','type':'password'})
    )
    

# class SignupForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','username','password1','password2']

class ProfilForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        exclude = ['user']



class AccountForm(forms.ModelForm):
    class Meta:
        model = AccountModel
        fields = '__all__'
        exclude = ['profil']

