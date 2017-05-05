from django.core.exceptions import ValidationError


def is_youtube_video(url):
    """
    Valida se "url" é do youtube
    """

    if url.startswith('https://youtube.com'):
        raise ValidationError('Digite um link dentro do youtube!')