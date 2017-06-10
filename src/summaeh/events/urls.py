from django.conf.urls import url
from . import views

app_name = 'events'
urlpatterns = [
    url(r'^$', views.list_events, name='list'),
    url(r'^detalhar_evento/(?P<id_event>[0-9]+)/$', views.detail_event, name='detail'),
]
