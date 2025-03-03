from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Seat, Booking  # Added Booking model import
from rest_framework import generics
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from .forms import UserSignupForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def reserve_seat(request, movie_id):
    # Ensure this is correctly fetching the movie by its ID
    movie = get_object_or_404(Movie, pk=movie_id)

    # Fetch available seats
    available_seats = Seat.objects.filter(movie=movie, is_booked=False)

    if request.method == 'POST':
        if available_seats.exists():
            seat = available_seats.first()  # Reserve the first available seat
            seat.is_booked = True
            seat.reserved_by = request.user
            seat.save()

            # Redirect back to the movie list page after reserving a seat
            return redirect('movie_list')  # This will reload the movie list page

    return render(request, 'reserve_seat.html', {'movie': movie, 'available_seats': available_seats})


def movie_list(request):
    movies = Movie.objects.all()
    
    movie_data = [
        {'movie': movie, 'available_seats': movie.available_seats}
        for movie in movies
    ]  # Create a list to hold movie info and available seats
    
    return render(request, 'movie_list.html', {'movie_data': movie_data})


@login_required
def booking_history(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_history.html', {'bookings': bookings})

@login_required
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
