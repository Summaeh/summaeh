from django.conf.urls import url
from . import views

app_name = 'videos'
urlpatterns = [
    url(r'^$', views.list_videos, name='list'),
    url(r'^adicionar_video/$', views.add_video, name='add'),
    url(r'^detalhar_video/(?P<id_video>[0-9]+)/$', views.detail_video, name='detail'),
    url(r'^like/$', views.like, name='like'),
]
