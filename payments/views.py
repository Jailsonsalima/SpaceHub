from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, get_object_or_404
from django_pagseguro.models import Checkout
from listings.models import Booking

def create_checkout(booking):
    checkout = Checkout()
    checkout.add_item(
        id=str(booking.id),
        description=booking.room.title,
        amount=str(booking.room.price_per_hour),
        quantity=1
    )
    return checkout

def start_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    checkout = create_checkout(booking)
    # redireciona o cliente para o PagSeguro
    return redirect(checkout.get_redirect_url())