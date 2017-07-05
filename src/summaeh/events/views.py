from django.http import HttpResponse
from .models import Event, Voting
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from summaeh.videos.models import Video, Vote
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
    videos_list = Video.objects.filter(event=event)
    user_already_vote = Vote.objects.filter(user=request.user, event=event).exists()

    AMOUNT_PER_PAGE = 3

    try:
        voting = Voting.objects.get(event=event)
    except Voting.DoesNotExist:
        voting = None

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

    if voting is not None:
        context = {
            'event': event,
            'voting_open': voting.is_open,
            'voting_already_close': voting.already_closed,
            'user_already_vote': user_already_vote,
            'videos_list': videos,
        }
    else:
        context = {
            'event': event,
            'voting_open': False,
            'voting_already_close': False,
            'user_already_vote': False,
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
        list_selected_videos = request.POST.getlist('checkvoting')

        voting = Voting()
        voting.event = Event.objects.get(id=id_event)
        voting.user = request.user
        voting.is_open = True
        voting.already_closed = False
        voting.save()

        for video_id in list_selected_videos:
            voting.video.add(Video.objects.get(id=video_id))

        return redirect('events:detail', id_event)

    return render(request, 'events/voting_videos.html', context)


@login_required
def finish_voting(request, id_event):
    event = Event.objects.get(id=id_event)
    voting = Voting.objects.get(event=event)

    voting.already_closed = True
    voting.save()

    return redirect('events:detail', id_event)


@login_required
def reopen_voting(request, id_event):
    event = Event.objects.get(id=id_event)
    voting = Voting.objects.get(event=event)

    voting.already_closed = False
    voting.save()

    return redirect('events:detail', id_event)


@login_required
def vote_video(request, id_event):
    event = Event.objects.get(id=id_event)
    voting = Voting.objects.get(event=event)
    videos_list = voting.video.all()

    try:
        vote = Vote.objects.get(event=event, user=request.user)
    except Vote.DoesNotExist:
        vote = None

    if request.method == 'GET':
        if vote is not None:
            context = {
                'videos_list': videos_list,
                'event': event,
                'user_video_voted': vote.video
            }
        else:
            context = {
                'videos_list': videos_list,
                'event': event,
                'user_video_voted': None
            }
    else :
        video_id = int(request.POST.get('radiovoting', None))
        if vote is not None:
            vote.video = Video.objects.get(id=video_id)
            vote.save()
        else:

            vote = Vote()
            vote.event = event
            vote.user = request.user
            vote.video = Video.objects.get(id=video_id)
            vote.save()

        return redirect('events:detail', id_event)

    return render(request, 'events/vote_video.html', context)