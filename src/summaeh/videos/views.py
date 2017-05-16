from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    AMOUNT_PER_PAGE = 3

    videos_list = Video.objects.all()

    paginator = Paginator(videos_list, AMOUNT_PER_PAGE)  # Quantidade de vídeo por página

    page = request.GET.get('page')
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não for um inteiro, vai para a primeira página
        videos = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do alcance
        # mostra o número de páginas como resultado
        videos = paginator.page(paginator.num_pages)

    return render(request, 'videos/list_videos.html', {'videos_list': videos})
