from django.conf.urls import include, url
from django.contrib import admin
from core.models import *
from core.views import *


urlpatterns = [
    # Examples:
    # url(r'^$', 'popmanager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.index', name='core_index'),

    # Peoples

    url(r'^pessoas/$', ListPeople.as_view(), name='list_people'),
    url(r'^pessoa/adicionar/$', CreatePeople.as_view(), name='create_people'),
    url(r'^pessoa/visualizar/(?P<pk>\d+)/$', DetailPeople.as_view(), name='view_people'),
    url(r'^pessoa/editar/(?P<pk>\d+)/$', EditPeople.as_view(), name='edit_people'),
    url(r'^pessoa/apagar/(?P<pk>\d+)/$', DeletePeople.as_view(), name='delete_people'),
]
