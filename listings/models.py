from django.db import models

# Create your models here.

from accounts.models import User

class Room(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # dono da sala
    title = models.CharField(max_length=100)
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, default='pending')  # pending, approved, paid