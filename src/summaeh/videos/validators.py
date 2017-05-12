import re

from django.core.exceptions import ValidationError

youtube_regex = re.compile(
    r'(https?://)?(www\.)?'
    '(youtube|youtu|youtube-nocookie)\.(com|be)/'
    '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')


def youtube_url_normalizer(url):
    youtube_regex_match = re.match(youtube_regex, url)
    if youtube_regex_match:
        return "https://youtube.com/embed/" + youtube_regex_match.group(6)
    else:
        raise ValidationError('Digite um link dentro do youtube!')


def is_youtube_video(url):
    """
    Valida se "url" é do youtube
    """
    url = youtube_url_normalizer(url)

    return url
