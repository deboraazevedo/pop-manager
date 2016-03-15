# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from vanilla import CreateView, DetailView, DeleteView, ListView, UpdateView
from core.models import *
from core.forms import PeopleForm, TaskForm

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
    paginate_by = 5

class CreatePeople(CreateView):
    model = People
    success_url = reverse_lazy('list_people')
    form_class = PeopleForm
    fields = '__all__'
    template_name = 'core/people/people_create_form.html'

class DetailPeople(DetailView):
    model = People
    template_name = 'core/people/people_detail.html'

class EditPeople(UpdateView):
    model = People
    success_url = reverse_lazy('list_people')
    form_class = PeopleForm
    template_name = 'core/people/people_update_form.html'

class DeletePeople(DeleteView):
    model = People
    success_url = reverse_lazy('list_people')
    template_name = 'core/people/people_confirm_delete.html'



class ListManagement(ListView):
    model = Management
    template_name = 'core/management/management_list.html'
    paginate_by = 5

class CreateManagement(CreateView):
    model = Management
    success_url = reverse_lazy('list_management')
    fields = '__all__'
    template_name = 'core/management/management_create_form.html'

class DetailManagement(DetailView):
    model = Management
    template_name = 'core/management/management_detail.html'

class EditManagement(UpdateView):
    model = Management
    success_url = reverse_lazy('list_management')
    fields = '__all__'
    template_name = 'core/management/management_update_form.html'

class DeleteManagement(DeleteView):
    model = Management
    success_url = reverse_lazy('list_management')
    template_name = 'core/management/management_confirm_delete.html'


class ListDirection(ListView):
    model = Direction
    template_name = 'core/direction/direction_list.html'
    paginate_by = 5

class CreateDirection(CreateView):
    model = Direction
    success_url = reverse_lazy('list_direction')
    fields = '__all__'
    template_name = 'core/direction/direction_create_form.html'

class DetailDirection(DetailView):
    model = Direction
    template_name = 'core/direction/direction_detail.html'

class EditDirection(UpdateView):
    model = Direction
    success_url = reverse_lazy('list_direction')
    fields = '__all__'
    template_name = 'core/direction/direction_update_form.html'

class DeleteDirection(DeleteView):
    model = Direction
    success_url = reverse_lazy('list_direction')
    template_name = 'core/direction/direction_confirm_delete.html'



class ListActivity(ListView):
    model = Activity
    template_name = 'core/activity/activity_list.html'
    paginate_by = 5

class CreateActivity(CreateView):
    model = Activity
    success_url = reverse_lazy('list_activity')
    fields = '__all__'
    template_name = 'core/activity/activity_create_form.html'

class DetailActivity(DetailView):
    model = Activity
    template_name = 'core/activity/activity_detail.html'

class EditActivity(UpdateView):
    model = Activity
    success_url = reverse_lazy('list_activity')
    fields = '__all__'
    template_name = 'core/activity/activity_update_form.html'

class DeleteActivity(DeleteView):
    model = Activity
    success_url = reverse_lazy('list_activity')
    template_name = 'core/activity/activity_confirm_delete.html'


class ListTask(ListView):
    model = Task
    template_name = 'core/task/task_list.html'
    paginate_by = 5

class CreateTask(CreateView):
    model = Task
    success_url = reverse_lazy('list_task')
    form_class = TaskForm
    fields = '__all__'
    template_name = 'core/task/task_create_form.html'

class DetailTask(DetailView):
    model = Task
    template_name = 'core/task/task_detail.html'

class EditTask(UpdateView):
    model = Task
    success_url = reverse_lazy('list_task')
    form_class = TaskForm
    fields = '__all__'
    template_name = 'core/task/task_update_form.html'

class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy('list_task')
    template_name = 'core/task/task_confirm_delete.html'
