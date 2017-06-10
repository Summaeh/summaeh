from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# Create your views here.
def list_events(request):
    event_list = Event.objects.all()
    context = {
        'event_list': event_list
    }

    return render(request, 'events/list_events.html', context)

def detail_event(request, id_event):
    event = Event.objects.get(id=id_event)

    return render(request, 'events/detail_event.html', {'event': event})


