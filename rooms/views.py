from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from .models import Room
from .forms import ŔoomForm

def show(request, room_id):
    model = Room
    template_name = 'rooms/show.html'

    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'rooms/show.html' , {'room':room})

def new(request):
    if request.method == "POST":
        form = ŔoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.author = request.user
            room.pub_date = timezone.now()
            room.save()
            return render(request, 'rooms/show.html' , {'room':room})
    else:
        form = ŔoomForm()
    return render(request, 'rooms/edit.html', {'form': form})


def index(request):
    room_list = Room.objects.all()
    template = loader.get_template('rooms/index.html')
    context = {
        'room_list': room_list
    }
    return render(request, 'rooms/index.html', context)
