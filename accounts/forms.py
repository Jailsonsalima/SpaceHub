from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Usuário ou Email")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)