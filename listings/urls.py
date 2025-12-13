from django.urls import path
from .views import create_room, room_list, room_detail, edit_room, delete_room, booking_list, approve_booking, reject_booking, dashboard

urlpatterns = [
    path('rooms/', room_list, name='room_list'),
    path('rooms/<int:room_id>/', room_detail, name='room_detail'),
    path('rooms/create/', create_room, name='create_room'),
    path('rooms/<int:room_id>/edit/', edit_room, name='edit_room'),
    path('rooms/<int:room_id>/delete/', delete_room, name='delete_room'),
    path('bookings/', booking_list, name='booking_list'),
    path('bookings/<int:booking_id>/approve/', approve_booking, name='approve_booking'),
    path('bookings/<int:booking_id>/reject/', reject_booking, name='reject_booking'),
    path('dashboard/', dashboard, name='dashboard'),

]