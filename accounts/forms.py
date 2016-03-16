# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate
from core.models import People

class LoginForm(forms.Form):
    username = forms.CharField(
        label=u'Usuário',
        max_length=50
    )
    password = forms.CharField(
        label=u'Senha',
        max_length=50,
        widget=forms.PasswordInput
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not People.objects.filter(username=username):
            raise forms.ValidationError('Usuário inválida!')
        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Senha inválida!')
        return password

    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        return authenticate(username=username, password=password)
