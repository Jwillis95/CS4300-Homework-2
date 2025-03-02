from django.shortcuts import render
from .models import Movie, Seat, Booking  # Added Booking model import
from rest_framework import generics
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

def seat_booking(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    seats = Seat.objects.filter(movie=movie)
    
    if request.method == 'POST':
        # Handle booking logic here
        pass

    return render(request, 'seat_booking.html', {'movie': movie, 'seats': seats})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def booking_history(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_history.html', {'bookings': bookings})

def seat_availability(request):
    available_seats = Seat.objects.filter(is_booked=False)
    return render(request, 'seat_availability.html', {'seats': available_seats})


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatListCreateView(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class SeatAvailabilityView(generics.ListAPIView):
    queryset = Seat.objects.filter(is_booked=False)  # Correct field filtering
    serializer_class = SeatSerializer

# Define Booking-related views
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingHistoryView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
