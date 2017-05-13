from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Room

def show(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'rooms/show.html', {'room': room})

def new(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'rooms/show.html', {'room': room})


def index(request):
    room_list = Room.objects.all()
    template = loader.get_template('rooms/index.html')
    context = {
        'room_list': room_list
    }
    return render(request, 'rooms/index.html', context)
