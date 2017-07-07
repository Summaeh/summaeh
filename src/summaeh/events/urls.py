from django.conf.urls import url
from . import views

app_name = 'events'
urlpatterns = [
    url(r'^$', views.list_events, name='list'),
    url(r'^detalhar_evento/(?P<id_event>[0-9]+)/$', views.detail_event, name='detail'),
    url(r'^criar_votacao/(?P<id_event>[0-9]+)/$', views.create_voting, name='create_voting'),
    url(r'^criar_votacao_com_senha/(?P<id_event>[0-9]+)/$', views.create_voting_with_password, name='create_voting_with_password'),
    url(r'^finalizar_votacao/(?P<id_event>[0-9]+)/$', views.finish_voting, name='finish_voting'),
    url(r'^reabrir_votacao/(?P<id_event>[0-9]+)/$', views.reopen_voting, name='reopen_voting'),
    url(r'^votar_video/(?P<id_event>[0-9]+)/$', views.vote_video, name='vote_video'),
    url(r'^votar_video_com_senha/(?P<id_event>[0-9]+)/$', views.validate_password, name='vote_video_with_password'),
    url(r'^segundo_turno/(?P<id_event>[0-9]+)/$', views.create_second_shift, name='create_second_shift'),
]
