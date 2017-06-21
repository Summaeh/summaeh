'''Test models dependencies'''
from django.contrib.auth.models import User
from django.test import TestCase
import factory
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


class VideoCreateMethodTests(TestCase):


    def test_suit(self):
        self.assertTrue(True)

    def test_Video_create(self):
        video_1 = VideoFactory()




