# -*- coding: utf-8 -*-

from django.contrib import admin
from core.models import *
from core.forms import PeopleForm, TaskForm
from  django.contrib.admin.sites import AdminSite
from daterange_filter.filter import DateRangeFilter

AdminSite.site_title = 'POP-RN - Rede Nacional de Ensino e Pesquisa'
AdminSite.site_header = 'POP-RN - Rede Nacional de Ensino e Pesquisa'
AdminSite.index_title = 'POP-RN - Rede Nacional de Ensino e Pesquisa'

class PeopleAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'office',
        'email',
        'is_staff',
        'is_active',
        'is_superuser',
    )
    search_fields = (
        'username',
        'first_name',
        'last_name',
        'office',
        'email',
        'direction',
    )
    list_filter = [
        'office',
        'direction',
        'groups',
        'is_staff',
        'is_active',
        'is_superuser',
    ]
    form = PeopleForm


class ManagementAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )
    list_filter = [
        'name',
    ]

class DirectionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )
    list_filter = [
        'management',
    ]

class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'priority',
        'status',
    )
    search_fields = (
        'name',
        'management',
        'priority',
        'status',
    )
    list_filter = [
        'management',
        'priority',
        'status',
    ]

class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'start_date',
        'conclusion_date',
        'people',
        'activity',
        'priority',
        'status',
    )
    search_fields = (
        'name',
        'people',
        'activity',
        'priority',
        'status',
    )
    list_filter = [
        'priority',
        'status',
        'people',
    ]


admin.site.register(People, PeopleAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Direction, DirectionAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Task, TaskAdmin)
