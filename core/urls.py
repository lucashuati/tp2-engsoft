from django.conf.urls import url
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='index', permanent=True)),
    url(r'^index/$', index, name='index'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^new/$', createUser, name='newuser'),
    url(r'^new/caderno/$', criarCaderno.as_view(), name='criarcaderno'),
    url(r'^cadernos/$', lista_cadernos, name='cadernos'),


]
