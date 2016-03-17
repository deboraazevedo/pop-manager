from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import permission_required
from core.models import *
from core.views import *


urlpatterns = [
    # Examples:
    # url(r'^$', 'popmanager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Authenticate

    url(r'^entrar/$', 'accounts.views.view_login', name='accounts_view_login'),
    url(r'^sair/$', 'accounts.views.view_logout', name='accounts_view_logout'),


    url(r'^$', 'core.views.index', name='core_index'),

    # Peoples

    url(r'^pessoas/$', permission_required('core.add_people', 'core.change_people', 'core.delete_people')(ListPeople.as_view()), name='list_people'),
    url(r'^pessoa/adicionar/$', permission_required('core.add_people')(CreatePeople.as_view()), name='create_people'),
    url(r'^pessoa/visualizar/(?P<pk>\d+)/$', permission_required('core.add_people', 'core.change_people', 'core.delete_people')(DetailPeople.as_view()), name='view_people'),
    url(r'^pessoa/editar/(?P<pk>\d+)/$', permission_required('core.change_people')(EditPeople.as_view()), name='edit_people'),
    url(r'^pessoa/apagar/(?P<pk>\d+)/$', permission_required('core.delete_people')(DeletePeople.as_view()), name='delete_people'),

    # Managements

    url(r'^gerencias/$', permission_required('core.add_management', 'core.change_management', 'core.delete_management')(ListManagement.as_view()), name='list_management'),
    url(r'^gerencia/adicionar/$', permission_required('core.add_management')(CreateManagement.as_view()), name='create_management'),
    url(r'^gerencia/visualizar/(?P<pk>\d+)/$', permission_required('core.add_management', 'core.change_management', 'core.delete_management')(DetailManagement.as_view()), name='view_management'),
    url(r'^gerencia/editar/(?P<pk>\d+)/$', permission_required('core.change_management')(EditManagement.as_view()), name='edit_management'),
    url(r'^gerencia/apagar/(?P<pk>\d+)/$', permission_required('core.delete_management')(DeleteManagement.as_view()), name='delete_management'),

    # Directions

    url(r'^diretorias/$', permission_required('core.add_direction', 'core.change_direction', 'core.delete_direction')(ListDirection.as_view()), name='list_direction'),
    url(r'^diretoria/adicionar/$', permission_required('core.add_direction')(CreateDirection.as_view()), name='create_direction'),
    url(r'^diretoria/visualizar/(?P<pk>\d+)/$', permission_required('core.add_direction', 'core.change_direction', 'core.delete_direction')(DetailDirection.as_view()), name='view_direction'),
    url(r'^diretoria/editar/(?P<pk>\d+)/$', permission_required('core.change_direction')(EditDirection.as_view()), name='edit_direction'),
    url(r'^diretoria/apagar/(?P<pk>\d+)/$', permission_required('core.delete_direction')(DeleteDirection.as_view()), name='delete_direction'),

    # Activitys

    url(r'^atividades/$', permission_required('core.add_activity', 'core.change_activity', 'core.delete_activity')(ListActivity.as_view()), name='list_activity'),
    url(r'^atividade/adicionar/$', permission_required('core.add_activity')(CreateActivity.as_view()), name='create_activity'),
    url(r'^atividade/visualizar/(?P<pk>\d+)/$', permission_required('core.add_activity', 'core.change_activity', 'core.delete_activity')(DetailActivity.as_view()), name='view_activity'),
    url(r'^atividade/editar/(?P<pk>\d+)/$', permission_required('core.change_activity')(EditActivity.as_view()), name='edit_activity'),
    url(r'^atividade/apagar/(?P<pk>\d+)/$', permission_required('core.delete_activity')(DeleteActivity.as_view()), name='delete_activity'),

    # Tasks

    url(r'^tarefas/$', permission_required('core.add_task', 'core.change_task', 'core.delete_task')(ListTask.as_view()), name='list_task'),
    url(r'^tarefa/adicionar/$', permission_required('core.add_task')(CreateTask.as_view()), name='create_task'),
    url(r'^tarefa/visualizar/(?P<pk>\d+)/$', permission_required('core.add_task', 'core.change_task', 'core.delete_task')(DetailTask.as_view()), name='view_task'),
    url(r'^tarefa/editar/(?P<pk>\d+)/$', permission_required('core.change_task')(EditTask.as_view()), name='edit_task'),
    url(r'^tarefa/apagar/(?P<pk>\d+)/$', permission_required('core.delete_task')(DeleteTask.as_view()), name='delete_task'),
]
