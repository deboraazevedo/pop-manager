from django.conf.urls import include, url
from django.contrib import admin
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

    url(r'^pessoas/$', ListPeople.as_view(), name='list_people'),
    url(r'^pessoa/adicionar/$', CreatePeople.as_view(), name='create_people'),
    url(r'^pessoa/visualizar/(?P<pk>\d+)/$', DetailPeople.as_view(), name='view_people'),
    url(r'^pessoa/editar/(?P<pk>\d+)/$', EditPeople.as_view(), name='edit_people'),
    url(r'^pessoa/apagar/(?P<pk>\d+)/$', DeletePeople.as_view(), name='delete_people'),

    # Managements

    url(r'^gerencias/$', ListManagement.as_view(), name='list_management'),
    url(r'^gerencia/adicionar/$', CreateManagement.as_view(), name='create_management'),
    url(r'^gerencia/visualizar/(?P<pk>\d+)/$', DetailManagement.as_view(), name='view_management'),
    url(r'^gerencia/editar/(?P<pk>\d+)/$', EditManagement.as_view(), name='edit_management'),
    url(r'^gerencia/apagar/(?P<pk>\d+)/$', DeleteManagement.as_view(), name='delete_management'),

    # Directions

    url(r'^diretorias/$', ListDirection.as_view(), name='list_direction'),
    url(r'^diretoria/adicionar/$', CreateDirection.as_view(), name='create_direction'),
    url(r'^diretoria/visualizar/(?P<pk>\d+)/$', DetailDirection.as_view(), name='view_direction'),
    url(r'^diretoria/editar/(?P<pk>\d+)/$', EditDirection.as_view(), name='edit_direction'),
    url(r'^diretoria/apagar/(?P<pk>\d+)/$', DeleteDirection.as_view(), name='delete_direction'),

    # Activitys

    url(r'^atividades/$', ListActivity.as_view(), name='list_activity'),
    url(r'^atividade/adicionar/$', CreateActivity.as_view(), name='create_activity'),
    url(r'^atividade/visualizar/(?P<pk>\d+)/$', DetailActivity.as_view(), name='view_activity'),
    url(r'^atividade/editar/(?P<pk>\d+)/$', EditActivity.as_view(), name='edit_activity'),
    url(r'^atividade/apagar/(?P<pk>\d+)/$', DeleteActivity.as_view(), name='delete_activity'),

    # Tasks

    url(r'^tarefas/$', ListTask.as_view(), name='list_task'),
    url(r'^tarefa/adicionar/$', CreateTask.as_view(), name='create_task'),
    url(r'^tarefa/visualizar/(?P<pk>\d+)/$', DetailTask.as_view(), name='view_task'),
    url(r'^tarefa/editar/(?P<pk>\d+)/$', EditTask.as_view(), name='edit_task'),
    url(r'^tarefa/apagar/(?P<pk>\d+)/$', DeleteTask.as_view(), name='delete_task'),
]
