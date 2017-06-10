from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_events(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def detail_event(request, id_event):
#     return HttpResponse("Hello, world. You're at the polls index.")