from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Room

def room_list(request):
    rooms = Room.objects.filter(available=True)
    return render(request, 'listings/room_list.html', {'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'listings/room_detail.html', {'room': room})