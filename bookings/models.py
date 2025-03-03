from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    available_seats = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def available_seats(self):
        # Count the number of unbooked seats for this movie
        return Seat.objects.filter(movie=self, is_booked=False).count()

    def create_seats(self, num_seats=100):
        """Create 100 seats for the movie."""
        for i in range(1, num_seats + 1):
            Seat.objects.create(movie=self, seat_number=f"S{i}", is_booked=False)

class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # Add movie field to relate with Movie
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)  # Indicates if the seat is booked

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

