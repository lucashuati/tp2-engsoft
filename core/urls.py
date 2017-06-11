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
    url(r'^excluir/caderno/$', excluir_cadernos, name='excluircadernos'),
    url(r'^editar/caderno/$', editar_cadernos, name='editarcadernos'),
    url(r'^excluir/caderno/(?P<pk>\d+)$', deletar_caderno.as_view(), name='deletarcaderno'),
    url(r'^editar/caderno/(?P<pk>\d+)$', editar_caderno.as_view(), name = 'editarcaderno'),
]
