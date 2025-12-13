from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import Room, Booking
from .forms import RoomForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.utils.dateparse import parse_datetime



def room_list(request):
    rooms = Room.objects.all()
    for room in rooms:
        room.is_reserved = room.booking_set.filter(status='approved').exists()


    q = request.GET.get('q')
    max_price = request.GET.get('max_price')
    available = request.GET.get('available')

    if q:
        rooms = rooms.filter(title__icontains=q)
    if max_price:
        rooms = rooms.filter(price_per_hour__lte=max_price)
    if available == 'true':
        rooms = rooms.filter(available=True)
    elif available == 'false':
        rooms = rooms.filter(available=False)

    return render(request, 'listings/room_list.html', {'rooms': rooms})


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    # Se o usuário clicar em reservar
    if request.method == 'POST' and request.user.is_authenticated:
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        booking = Booking.objects.create(
            client=request.user,
            room=room,
            start_date=parse_datetime(request.POST.get('start_date')),
            end_date=parse_datetime(request.POST.get('start_date' + timezone.timedelta(hours=1))),  # exemplo: 1h
            status='pending'
        )
        return redirect('room_list')  # ou uma página de confirmação

    return render(request, 'listings/room_detail.html', {'room': room})

@login_required
def create_room(request):
    if request.method == 'POST':

        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.owner = request.user  # atribui o dono automaticamente
            room.save()
            return redirect('room_list')  # redireciona para listagem de salas
    else:
        form = RoomForm()
    return render(request, 'listings/create_room.html', {'form': form})

@login_required
def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    # Verifica se o usuário logado é o dono
    if room.owner != request.user:
        return redirect('room_list')  # bloqueia acesso

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_detail', room_id=room.id)
    else:
        form = RoomForm(instance=room)

    return render(request, 'listings/edit_room.html', {'form': form, 'room': room})

@login_required
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    # Só o dono pode excluir
    if room.owner != request.user:
        return redirect('room_list')

    if request.method == 'POST':
        room.delete()
        return redirect('room_list')

    return render(request, 'listings/delete_room.html', {'room': room})

@login_required
def booking_list(request):
    # Reservas feitas pelo usuário
    my_bookings = Booking.objects.filter(client=request.user)

    # Reservas recebidas (salas que ele cadastrou)
    received_bookings = Booking.objects.filter(room__owner=request.user)

    return render(request, 'listings/booking_list.html', {
        'my_bookings': my_bookings,
        'received_bookings': received_bookings
    })


@login_required
def approve_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.room.owner == request.user:
        booking.status = 'approved'
        booking.save()
        messages.success(request, "Reserva aprovada com sucesso!")
    else:
        messages.error(request, "Você não tem permissão para aprovar esta reserva.")
    return redirect('booking_list')



@login_required
def reject_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Só o dono da sala pode rejeitar
    if booking.room.owner == request.user:
        booking.status = 'rejected'
        booking.save()
        messages.warning(request, "Reserva rejeitada.")
    else:
        messages.error(request, "Você não tem permissão para rejeitar esta reserva.")
    return redirect('booking_list')

@login_required
def dashboard(request):
    # Salas anunciadas pelo usuário
    my_rooms = Room.objects.filter(owner=request.user)

    # Reservas feitas pelo usuário
    my_bookings = Booking.objects.filter(client=request.user)

    # Reservas recebidas (nas salas que ele cadastrou)
    received_bookings = Booking.objects.filter(room__owner=request.user)

    return render(request, 'listings/dashboard.html', {
        'my_rooms': my_rooms,
        'my_bookings': my_bookings,
        'received_bookings': received_bookings,
        'is_dashboard': True,
    })