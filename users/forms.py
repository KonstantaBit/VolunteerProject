from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AbstractRegistrationForm(UserCreationForm):
    pass

    class Meta(UserCreationForm.Meta):
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
        }

        fields = ('username', 'email', 'first_name', 'last_name')


class VolunteerRegistrationForm(AbstractRegistrationForm):
    pass


class ValidatorRegistrationForm(AbstractRegistrationForm):
    pass


class OrganizationRegistrationForm(AbstractRegistrationForm):
    pass

