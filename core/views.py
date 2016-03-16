# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from vanilla import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.models import *
from core.forms import PeopleForm, TaskForm


@login_required(login_url='/entrar/')
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

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(ListPeople, self).dispatch(*args, **kwargs)


class CreatePeople(CreateView):
    model = People
    success_url = reverse_lazy('list_people')
    form_class = PeopleForm
    fields = '__all__'
    template_name = 'core/people/people_create_form.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(CreatePeople, self).dispatch(*args, **kwargs)

class DetailPeople(DetailView):
    model = People
    template_name = 'core/people/people_detail.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(DetailPeople, self).dispatch(*args, **kwargs)

class EditPeople(UpdateView):
    model = People
    success_url = reverse_lazy('list_people')
    form_class = PeopleForm
    template_name = 'core/people/people_update_form.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(EditPeople, self).dispatch(*args, **kwargs)

class DeletePeople(DeleteView):
    model = People
    success_url = reverse_lazy('list_people')
    template_name = 'core/people/people_confirm_delete.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(DeletePeople, self).dispatch(*args, **kwargs)



class ListManagement(ListView):
    model = Management
    template_name = 'core/management/management_list.html'
    paginate_by = 5

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(ListManagement, self).dispatch(*args, **kwargs)

class CreateManagement(CreateView):
    model = Management
    success_url = reverse_lazy('list_management')
    fields = '__all__'
    template_name = 'core/management/management_create_form.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(CreateManagement, self).dispatch(*args, **kwargs)

class DetailManagement(DetailView):
    model = Management
    template_name = 'core/management/management_detail.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(DetailManagement, self).dispatch(*args, **kwargs)

class EditManagement(UpdateView):
    model = Management
    success_url = reverse_lazy('list_management')
    fields = '__all__'
    template_name = 'core/management/management_update_form.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(EditManagement, self).dispatch(*args, **kwargs)

class DeleteManagement(DeleteView):
    model = Management
    success_url = reverse_lazy('list_management')
    template_name = 'core/management/management_confirm_delete.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteManagement, self).dispatch(*args, **kwargs)


class ListDirection(ListView):
    model = Direction
    template_name = 'core/direction/direction_list.html'
    paginate_by = 5

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(ListDirection, self).dispatch(*args, **kwargs)

class CreateDirection(CreateView):
    model = Direction
    success_url = reverse_lazy('list_direction')
    fields = '__all__'
    template_name = 'core/direction/direction_create_form.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(CreateDirection, self).dispatch(*args, **kwargs)

class DetailDirection(DetailView):
    model = Direction
    template_name = 'core/direction/direction_detail.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(DetailDirection, self).dispatch(*args, **kwargs)

class EditDirection(UpdateView):
    model = Direction
    success_url = reverse_lazy('list_direction')
    fields = '__all__'
    template_name = 'core/direction/direction_update_form.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(EditDirection, self).dispatch(*args, **kwargs)

class DeleteDirection(DeleteView):
    model = Direction
    success_url = reverse_lazy('list_direction')
    template_name = 'core/direction/direction_confirm_delete.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteDirection, self).dispatch(*args, **kwargs)

class ListActivity(ListView):
    model = Activity
    template_name = 'core/activity/activity_list.html'
    paginate_by = 5

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(ListActivity, self).dispatch(*args, **kwargs)

class CreateActivity(CreateView):
    model = Activity
    success_url = reverse_lazy('list_activity')
    fields = '__all__'
    template_name = 'core/activity/activity_create_form.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(CreateActivity, self).dispatch(*args, **kwargs)

class DetailActivity(DetailView):
    model = Activity
    template_name = 'core/activity/activity_detail.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(DetailActivity, self).dispatch(*args, **kwargs)

class EditActivity(UpdateView):
    model = Activity
    success_url = reverse_lazy('list_activity')
    fields = '__all__'
    template_name = 'core/activity/activity_update_form.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(EditActivity, self).dispatch(*args, **kwargs)

class DeleteActivity(DeleteView):
    model = Activity
    success_url = reverse_lazy('list_activity')
    template_name = 'core/activity/activity_confirm_delete.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteActivity, self).dispatch(*args, **kwargs)


class ListTask(ListView):
    model = Task
    template_name = 'core/task/task_list.html'
    paginate_by = 5

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(ListTask, self).dispatch(*args, **kwargs)

class CreateTask(CreateView):
    model = Task
    success_url = reverse_lazy('list_task')
    form_class = TaskForm
    fields = '__all__'
    template_name = 'core/task/task_create_form.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(CreateTask, self).dispatch(*args, **kwargs)

class DetailTask(DetailView):
    model = Task
    template_name = 'core/task/task_detail.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(DetailTask, self).dispatch(*args, **kwargs)

class EditTask(UpdateView):
    model = Task
    success_url = reverse_lazy('list_task')
    form_class = TaskForm
    fields = '__all__'
    template_name = 'core/task/task_update_form.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(EditTask, self).dispatch(*args, **kwargs)

class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy('list_task')
    template_name = 'core/task/task_confirm_delete.html'

    @method_decorator(login_required(login_url='/entrar/'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteTask, self).dispatch(*args, **kwargs)
