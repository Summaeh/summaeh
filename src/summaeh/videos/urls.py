from django.conf.urls import url
from . import views

app_name = 'videos'
urlpatterns = [
    url(r'^adicionar_video/', views.add_video, name='add_video'),
    url(r'^salvar_video/', views.save_video, name='save_video'),
]

