from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.DurationField()

    def __str__(self):
        return self.title

class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False) 

    def __str__(self):
        return f"seat {self.seat_number} - {'Booked' if self.is_booked else 'Available'}"

# bookings/models.py
from django.db import models

class Booking(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    seat = models.ForeignKey('Seat', on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking {self.id} - {self.movie.title} - {self.seat.number}'

