from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .validators import youtube_url_normalizer
from .models import Video


@login_required
def add_video(request):
    return render(request, 'videos/add_video.html')


@login_required
def save_video(request):
    if request.method == 'POST':
        url = request.POST.get('linkvideo', '')
        name_video = request.POST.get('namevideo', '')

        url_parse = youtube_url_normalizer(url)

        video = Video.objects.create(link=url_parse,name=name_video,user=request.user)
        Video.save(video)

        video_info = {
            'urlVideo': url_parse,
            'nameVideo': name_video
        }

        return render(request, 'videos/save_video.html', video_info)
    else:
        return render(request, 'videos/add_video.html')
