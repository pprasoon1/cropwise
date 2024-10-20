from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class AgriForm(forms.Form):
    state = forms.CharField(max_length=100)
    district = forms.CharField(max_length=100)
    block = forms.CharField(max_length=100, required=False)
    start_month = forms.ChoiceField(choices=[(str(i), i) for i in range(1, 13)], required=False)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']