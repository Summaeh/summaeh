from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .validators import youtube_url_normalizer
from .models import *
from summaeh.events.models import Event
from .forms import VideoForm
from django.http import JsonResponse

@login_required
def add_video(request, id_event):
    event = Event.objects.get(id=id_event)
    ctx = {}

    if request.method == 'GET':
        ctx['form'] = VideoForm()
    else:
        ctx['form'] = form = VideoForm(request.POST)

        if form.is_valid():
            video = form.save(commit=False)
            video.event = event
            video.user = request.user
            video.link = youtube_url_normalizer(video.link)
            video.save()
            return redirect('events:detail', id_event)

    return render(request, 'videos/add_video.html', ctx)


def list_videos(request):
    AMOUNT_PER_PAGE = 5

    videos_list = Video.objects.all()

    paginator = Paginator(videos_list, AMOUNT_PER_PAGE)  # Show AMOUNT_PER_PAGE contacts per page

    page = request.GET.get('page')
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        videos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        videos = paginator.page(paginator.num_pages)

    return render(request, 'videos/list_videos.html', {'videos_list': videos})


@login_required
def detail_video(request, id_video):
    video = Video.objects.get(id=id_video)
    comments = Comment.objects.filter(video=id_video,user=request.user)
    num_likes = Like.objects.filter(video=video).count()
    user_already_like = Like.objects.filter(video=video, user=request.user).count()

    if user_already_like <= 0:
        user_already_like = False
    else:
        user_already_like = True

    information = {
        'video': video,
        'comments_list': comments,
        'num_likes': num_likes,
        'user_already_like': user_already_like,
    }

    return render(request, 'videos/detail_video.html', information)


@login_required
@require_POST
def like(request):
    user = request.user
    video_id = int(request.POST.get('video_id', None))
    video = Video.objects.get(id=video_id);

    if Like.objects.filter(user=user, video=video).exists():
        # User already like this video
        # remove like/user
        Like.objects.filter(user=user, video=video).delete()
        like = False
    else:
        # Add a like to the video
        Like.objects.create(user=user, video=video)
        like = True

    num_likes = Like.objects.filter(video=video).count()

    ctx = {'likes_count': num_likes, 'like': like}

    return JsonResponse(ctx)