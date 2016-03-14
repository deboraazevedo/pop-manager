# -*- coding: utf-8 -*-

from django import forms
from core.models import People, Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class PeopleForm(forms.ModelForm):

    class Meta:
        model = People
        fields = [
            'username',
            'first_name',
            'last_name',
            'office',
            'email',
            'password',
            'direction',
            'groups',
            'user_permissions',
            #'is_staff',
            #'is_active',
            'is_superuser',
            'last_login',
            'date_joined',
        ]
        widgets = {
            'password': forms.PasswordInput()
        }
