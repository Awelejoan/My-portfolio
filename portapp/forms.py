
from django import forms
from portapp.models import *
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form_control','placeholder':'Your Name', 'style':'width:100%'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form_control', 'placeholder':'Your Email', 'style':'width:100%'}))
    vemail= forms.CharField(widget=forms.EmailInput(attrs={'class':'form_control','placeholder':'Re-enter email', 'style':'width:100%'}))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form_control','placeholder':'Your Phone_no', 'style':'width:100%'}))
    message=forms.CharField(widget=forms.Textarea(attrs={'class':'form_control','placeholder':'Message', 'style':'width:100%'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    class Meta():
        model = Contact
        fields = '__all__'



    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        vemail = cleaned_data.get('vemail')
        
        if email != vemail:
            raise forms.ValidationError('Your emails must match')

class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'width:100%'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'style':'width:100%'}))
    comment= forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'comment', 'style':'width:100%'}))
    class Meta():
        model =Comment 
        fields = ('name', 'email', 'comment')

class RegForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control p-3', 'placeholder':'Username', 'style':'width:90%'}))
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control p-3','placeholder':'Firstname', 'style':'width:90%'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control p-3', 'placeholder':'Lastname', 'style':'width:90%'}))
    password1= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control p-3', 'placeholder':'Input Password', 'style':'width:90%'}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control p-3', 'placeholder':'Re-enter password', 'style':'width:90%'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control p-3','placeholder':'Email', 'style':'width:90%'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,validators=[validators.
    MaxLengthValidator(0)])
    
              

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']     
       

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 != password2:
            raise forms.ValidationError('passwords must match')

        