from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from .views import (
    SeatAvailabilityView,
    MovieListCreateView,
    MovieDetailView,
    SeatListCreateView,
    BookingListCreateView,  # Ensure this is imported correctly
    BookingHistoryView
)
from .views import signup


urlpatterns = [
    # Traditional Views Routes (for the frontend)
    path('', views.movie_list, name='movie_list'),  # Frontpage with movie list
    path('movies/', views.movie_list, name='movie_list'),  # Optional, if you want a separate movie list page
    path('reserve_seat/<int:movie_id>/', views.reserve_seat, name='reserve_seat'),
    path('booking/history/', views.booking_history, name='booking_history'),

    # Authentication Routes
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # API Routes using CBVs (Class-based Views)
    path('api/movies/', MovieListCreateView.as_view(), name='movie-list'),
    path('api/movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('api/seats/', SeatListCreateView.as_view(), name='seat-list'),
    path('api/seats/available/', SeatAvailabilityView.as_view(), name='seat-availability'),
    path('api/bookings/', BookingListCreateView.as_view(), name='booking-list'),
    path('api/bookings/history/', BookingHistoryView.as_view(), name='booking-history'),
]
