from django import forms
from .models import loginUser, RegistrationEntry, loginUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationEntry
        fields = ['first_name','username', 'last_name','password', 'phone', 'address']
class loginAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))

class loginUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = loginUser
        fields = ('email', 'password')

