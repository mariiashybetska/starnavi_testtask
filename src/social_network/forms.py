from django.forms import ModelForm
from django import forms

from social_network.models import User, Post


class SignUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['confirm_password']:
                raise forms.ValidationError('Passwords do not match!')
        return cleaned_data

