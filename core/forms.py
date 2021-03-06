# -*- coding: utf-8 -*-

from django import forms
from core.models import People, Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from datetimewidget.widgets import DateTimeWidget




class PeopleForm(forms.ModelForm):

    class Meta:
        model = People
        fields = [
            'username',
            'first_name',
            'last_name',
            'office',
            'email',
            #'password',
            'direction',
            'groups',
            'user_permissions',
            'is_staff',
            'is_active',
            'is_superuser',
            'last_login',
            'date_joined',
        ]
        widgets = {
            'password': forms.PasswordInput()
        }

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        dateTimeOptions = {
                'format': 'dd/mm/yyyy HH:ii',
                'autoclose': True,
                'minuteStep': 10,
                'pickerPosition': 'bottom-left',
        }
        widgets = {
                #Use localization and bootstrap 3
                'start_date': DateTimeWidget(attrs = {'id': "yourdatetimeid1", 'placeholder': 'Clique aqui'}, options=dateTimeOptions, bootstrap_version=3),
                'conclusion_date': DateTimeWidget(attrs = {'id': "yourdatetimeid2", 'placeholder': 'Clique aqui'}, options=dateTimeOptions, bootstrap_version=3)
        }
