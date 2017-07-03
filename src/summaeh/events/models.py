from django.db import models
from django.conf import settings


class Event(models.Model):

    name = models.CharField('Nome', max_length=200)

    date_start = models.DateTimeField('Data de Início')

    date_end = models.DateTimeField('Data de Término')

    estimated_public = models.IntegerField('Público Estimado')

    description = models.CharField('Descrição', max_length=600)

    other_informations = models.CharField('Demais Informações', max_length=400)

    name_institute = models.CharField('Local', max_length=200)

    institute_address = models.CharField('Endereço', max_length=200)

    def __str__(self):
        return self.name


class Voting(models.Model):

    event = models.ForeignKey(
        Event,
        related_name='events',
        verbose_name='Evento',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Usuário',
        related_name='events',
        on_delete=models.PROTECT,
        help_text='Usuário responsável pelo evento.',
    )
    video = models.ManyToManyField(
        'videos.Video',
        related_name='events',
    )
    is_open = models.BooleanField(
        default=False,
    )