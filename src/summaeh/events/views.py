from django.http import HttpResponse
from .models import Event
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from summaeh.videos.models import Video
from django.shortcuts import render, redirect

@login_required
def list_events(request):
    event_list = Event.objects.all()
    context = {
        'event_list': event_list
    }

    return render(request, 'events/list_events.html', context)

@login_required
def detail_event(request, id_event):
    event = Event.objects.get(id=id_event)

    AMOUNT_PER_PAGE = 3

    videos_list = Video.objects.filter(event=event)

    paginator = Paginator(videos_list, AMOUNT_PER_PAGE)  # Quantidade de vídeo por página

    page = request.GET.get('page')
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não for um inteiro, vai para a primeira página
        videos = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do alcance vai para a última página existente
        videos = paginator.page(paginator.num_pages)

    context = {
        'event': event,
        'videos_list': videos,
    }

    return render(request, 'events/detail_event.html', context)

@login_required
def create_voting(request, id_event):

    event = Event.objects.get(id=id_event)

    videos_list = Video.objects.filter(event=event)

    if request.method == 'GET':
        context = {
            'event': event,
            'videos_list': videos_list,
        }
    else:
        form = request.POST.getlist('checkvoting')
        print(form)

        return redirect('videos/list_videos.html')

    return render(request, 'events/voting_videos.html', context)