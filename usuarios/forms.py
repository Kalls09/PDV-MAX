from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Users

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Users
        fields = ('username', 'email', 'cargo')

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('username', 'email', 'password1', 'password2', 'cargo')
