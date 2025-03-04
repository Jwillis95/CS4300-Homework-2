from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    available_seats = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return self.title

    def update_available_seats(self):
        """Recalculate available seats based on unbooked seats."""
        self.available_seats = Seat.objects.filter(movie=self, is_booked=False).count()
        self.save() 

    def create_seats(self, num_seats=100):
        """Create seats for the movie."""
        for i in range(1, num_seats + 1):
            Seat.objects.create(movie=self, seat_number=f"S{i}", is_booked=False)
        self.update_available_seats() 

    @property
    def available_seats(self):
        return Seat.objects.filter(movie=self, is_booked=False).count()

    def update_available_seats(self):

        pass

class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) 
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False) 

    def __str__(self):
        return f"seat {self.seat_number} - {'Booked' if self.is_booked else 'Available'}"


from django.db import models

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserved seat for: {self.movie.title} (Seat: {self.seat.id})"