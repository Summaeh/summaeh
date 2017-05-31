from django.conf import settings
from django.db import models

from model_utils.models import TimeStampedModel
from .validators import is_youtube_video


class Video(TimeStampedModel):
    """
    Representa um vídeo do youtube.
    """

    # event = models.ForeingKey('events.Event', related_name='videos')
    link = models.URLField(
        'Link',
        max_length=200,
        help_text='Link do vídeo no Youtube (ex.: https://youtube.com/...)',
        validators=[is_youtube_video],
    )
    name = models.CharField(
        'Nome',
        max_length=200,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Usuário',
        related_name='videos',
        on_delete=models.PROTECT,
        help_text='Usuário responsável pelo vídeo.',
    )

    def __str__(self):
        return self.name

    def new_comment(self, user, comment):
        """
        Cria um comentário no vídeo para o usuário dado.
        """
        self.comments.create(user=user, comment=comment)

    def like(self, user, type):
        """
        Registra um like (ou dislike) de um usuário.
        
        Args:
            user: usuário que faz a requisição
            type (str): 'like' ou 'dislike'
        """
        type = LIKE_TYPES[type]
        self.likes.create_or_update(user=user, type=type)

    @property
    def num_likes(self):
        return self.likes.filter(type=Like.TYPE_LIKE).count()

    @property
    def num_dislikes(self):
        return self.likes.filter(type=Like.TYPE_DISLIKE).count()


class Comment(TimeStampedModel):
    """
    Comentário em um vídeo.
    """

    video = models.ForeignKey(
        Video,
        related_name='comments',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Usuário',
        related_name='comments',
    )
    comment = models.TextField()


class Like(TimeStampedModel):
    """
    Um like (ou dislike) para um vídeo.
    """

    TYPE_LIKE = 0
    TYPE_DISLIKE = 1

    video = models.ForeignKey(
        Video,
        related_name='likes',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='likes',
        on_delete=models.PROTECT,
    )
    type = models.IntegerField(
        choices=[
            (TYPE_LIKE, 'like'),
            (TYPE_DISLIKE, 'dislike'),
        ],
    )

    class Meta:
        unique_together = [
            ('user', 'video', 'type'),
        ]


LIKE_TYPES = {'like': Like.TYPE_LIKE, 'dislike': Like.TYPE_DISLIKE}