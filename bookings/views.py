from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Booking


# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

@login_required
def seat_booking(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    seats = Seat.objects.filter(movie=movie)

    if request.method == 'POST':
        selected_seat_id = request.POST.get('seat')
        selected_seat = Seat.objects.get(id=selected_seat_id)
        selected_seat_booked = True
        selected_seat.save()

        Booking.objects.create(
            movie=movie,
            seat=selected_seat,
            user=request.user,
            booking_date=request.POST.get('booking_date')
        )
        return render(request, 'seat_booking.html', { 'movie': movie, 'seats': seats, 'message': 'Booking Successful'})

    return render(request, 'seat_booking.html', {'movie': movie, 'seats': seats})

    @login_required
    def booking_history(request):
        bookings = Bookings.objects.filter(user=request.user)
        return render(request, 'booking_history.html', { 'bookings': bookings})
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_history.html', {'bookings': bookings})