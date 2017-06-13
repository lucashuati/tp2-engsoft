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
    url(r'^cadernos/(?P<pk>\d+)$', mostrar_caderno.as_view(), name='mostrarcaderno'),

    url(r'^new/listaCaderno/$', criarListaCaderno.as_view(), name='criarListaCaderno'),
    url(r'^listaCadernos/$', lista_lista_cadernos, name='listaCadernos'),
    url(r'^excluir/listaCaderno/$', excluir_lista_cadernos, name='excluirListaCadernos'),
    url(r'^editar/listaCaderno/$', editar_lista_cadernos, name='editarListaCadernos'),
    url(r'^excluir/listaCaderno/(?P<pk>\d+)$', deletar_lista_caderno.as_view(), name='deletarListaCaderno'),
    url(r'^editar/listaCaderno/(?P<pk>\d+)$', editar_lista_caderno.as_view(), name = 'editarListaCaderno'),
    url(r'^listaCadernos/(?P<pk>\d+)$', mostrar_lista_caderno.as_view(), name='mostrarListaCaderno'),
]
