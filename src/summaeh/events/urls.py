from django.conf.urls import url
from . import views

app_name = 'events'
urlpatterns = [
    url(r'^$', views.list_events, name='list'),
    url(r'^detalhar_evento/(?P<id_event>[0-9]+)/$', views.detail_event, name='detail'),
    url(r'^criar_votacao/(?P<id_event>[0-9]+)/$', views.create_voting, name='create_voting'),
]
