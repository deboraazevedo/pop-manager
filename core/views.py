# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from vanilla import CreateView, DetailView, DeleteView, ListView, UpdateView
from core.models import *
from core.forms import PeopleForm

def index(request):
    peoples = People.objects.all()
    managements = Management.objects.all()
    directions = Direction.objects.all()
    activitys = Activity.objects.all()
    tasks = Task.objects.all()

    return render(
        request,
        'core/index.html',
        {
            'peoples': peoples,
            'managements': managements,
            'directions': directions,
            'activitys': activitys,
            'tasks': tasks
        }
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

class DetailPeople(DetailView):
    model = People
    template_name = 'core/people/people_detail.html'

class EditPeople(UpdateView):
    model = People
    success_url = reverse_lazy('list_people')
    form_class = PeopleForm
    template_name = 'core/people/people_form.html'

class DeletePeople(DeleteView):
    model = People
    success_url = reverse_lazy('list_people')
    template_name = 'core/people/people_confirm_delete.html'
