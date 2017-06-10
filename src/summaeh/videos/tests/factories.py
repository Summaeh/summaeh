import factory
from django.contrib.auth.models import User

from src.summaeh.videos.models import Video


class UserFactory(factory.Factory):
    class Meta:
        model = User
    username = 'nicacio'
    email = 'nicacionetobsb@gmail.com'
    password = 'admin'



class VideoFactory(factory.Factory):
    class Meta:
        model = Video
    link = "https://www.youtube.com/watch?v=v0NSeysrDYw",
    name = "Bob Sinclar - Love Generation",
