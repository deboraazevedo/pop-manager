# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from vanilla import CreateView, DeleteView, ListView, UpdateView
from core.models import *
from core.forms import PeopleForm

def index(request):
    return render(
        request,
        'core/index.html'
    )

class ListPeople(ListView):
    model = People
    template_name = 'core/people/people_list.html'
    paginate_by = 10

class CreatePeople(CreateView):
    model = People
    success_url = reverse_lazy('list_people')
    form_class = PeopleForm
    fields = '__all__'
    template_name = 'core/people/people_form.html'

class EditPeople(UpdateView):
    model = People
    success_url = reverse_lazy('list_people')


class DeletePeople(DeleteView):
    model = People
    success_url = reverse_lazy('list_people')
