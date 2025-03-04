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

def custom_404(request, exception):
    return render(request, '404.html')  # You can create a simple 404 page


@login_required
def reserve_seat(request, movie_id):
    print(f"Reserving seat for movie ID: {movie_id}")
    movie = get_object_or_404(Movie, pk=movie_id)
    print(f"Movie found: {movie.title}")

    available_seats = Seat.objects.filter(movie=movie, is_booked=False)
    print(f"Available seats: {len(available_seats)}")

    if request.method == 'POST':
        if available_seats.exists():
            seat = available_seats.first()
            seat.is_booked = True
            seat.save()
            
            # Use request.user directly instead of request.user.username
            Booking.objects.create(movie=movie, seat=seat, user=request.user)
            movie.update_available_seats()
            
            print("Seat reserved successfully!")
            return redirect('/')  # Redirect to home page
        else:
            print("No available seats.")
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
    bookings = Booking.objects.filter(user=request.user)  # Get all bookings for the logged-in user
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
    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(user=request.user)  # Get all bookings for the logged-in user
        serializer = BookingSerializer(bookings, many=True)
        
        # Instead of returning the API response, render the template with the serialized data
        return render(request, 'booking_history.html', {'bookings': serializer.data})