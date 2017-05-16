from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .validators import youtube_url_normalizer
from .models import Video
from .forms import VideoForm


@login_required
def add_video(request):
    ctx = {}

    if request.method == 'GET':
        ctx['form'] = VideoForm()
    else:
        ctx['form'] = form = VideoForm(request.POST)

        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.link = youtube_url_normalizer(video.link)
            video.save()
            return redirect('videos:list')

    return render(request, 'videos/add_video.html', ctx)


@login_required
def list_videos(request):
    return render(request, 'videos/list_videos.html')
