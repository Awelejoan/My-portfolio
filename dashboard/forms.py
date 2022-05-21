
from django import forms
from django.core import validators
from django.contrib.auth.models import User
from portapp.models import Blog
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from dashboard.models import *

class AddBlog(forms.ModelForm):
    title =forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control','style':'width:60%'}))
    description =forms.CharField(max_length=20, widget=forms.Textarea(attrs={'class':'form-control','style':'width:60%'}))
    class Meta():
        model = Blog
        exclude = ['title2', 'poster']

    
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs = {'class':'form-control', 'type':'password', 'style':'width:60%'})) 
    new_password1 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'style':'width:60%'})) 
    new_password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'style':'width:60%'}))
    class Meta():
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class EditUserForm(forms.ModelForm):
    username =forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control','style':'width:60%'}))
    first_name =forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control','style':'width:60%'}))
    last_name =forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control','style':'width:60%'}))
    email =forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control','style':'width:60%'}))
    
    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name','email']
        exclude = ['password']
        
class EditBlogForm(forms.ModelForm):
    class Meta():
        model = Blog
        exclude=['poster']
