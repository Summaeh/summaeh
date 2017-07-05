from django.shortcuts import render, redirect
from summaeh.videos.models import *

def home(request):
    video = Video.objects.last()
    num_likes = Like.objects.filter(video=video).count()
    user_already_like = Like.objects.filter(video=video, user=request.user).count()

    if user_already_like <= 0:
        user_already_like = False
    else:
        user_already_like = True

    information = {
        'video': video,
        'num_likes': num_likes,
        'user_already_like': user_already_like,
    }

    return render(request, 'pages/home.html', information)
