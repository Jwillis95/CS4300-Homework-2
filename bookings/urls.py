from django.urls import path
from bookings import views
from .views import (
    SeatAvailabilityView,
    MovieListCreateView,
    MovieDetailView,
    SeatListCreateView,
    BookingListCreateView,  # Ensure this is imported correctly
    BookingHistoryView
)

urlpatterns = [
    # API Routes using CBVs
    path('api/movies/', MovieListCreateView.as_view(), name='movie-list'),
    path('api/movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('api/seats/', SeatListCreateView.as_view(), name='seat-list'),
    path('api/seats/available/', SeatAvailabilityView.as_view(), name='seat-availability'),
    path('api/bookings/', BookingListCreateView.as_view(), name='booking-list'),
    path('api/bookings/history/', BookingHistoryView.as_view(), name='booking-history'),

    # Traditional Views Routes (if needed for the frontend)
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/book/', views.seat_booking, name='seat_booking'),
    path('booking/history/', views.booking_history, name='booking_history'),
]
