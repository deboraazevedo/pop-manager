# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from accounts.forms import LoginForm
from django.contrib.auth import login, logout


def view_login(request):
    next = request.GET.get('next', reverse('core_index'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(next)
    else:
        form = LoginForm()
    return render(
        request,
        'accounts/login.html',
        {
            'form': form
        }
    )

def view_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts_view_login'))
