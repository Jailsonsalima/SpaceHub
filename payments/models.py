from django.db import models

# Create your models here.

from django.db import models
from listings.models import Booking

class PagSeguroPayment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)