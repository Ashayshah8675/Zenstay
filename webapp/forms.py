from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile
from datetime import datetime, date 


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def _init_(self, *args, **kwargs):
        super(RegisterUserForm, self)._init_(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'        
        self.fields['password1'].widget.attrs['class'] = 'form-control'        
        self.fields['password2'].widget.attrs['class'] = 'form-control'        

        # for field_name in self.fields:
        #     self.fields[field_name].widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):
    bio = forms.Textarea(attrs={'class': 'form-control'})
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    contact = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.Textarea(attrs={'class': 'form-control'})

    class Meta:
        model = UserProfile
        fields = ('fname', 'lname', 'bio', 'email', 'birthdate', 'contact', 'gender', 'address')