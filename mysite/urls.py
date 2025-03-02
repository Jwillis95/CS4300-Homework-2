from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookings.viewsets import MovieViewSet, SeatViewSet, BookingViewSet
from bookings import views


router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    # API Routes using viewsets (for REST API)
    path('', include('bookings.urls')),
    path('api/', include(router.urls)),

    # Traditional Views Routes (for frontend)
    path('', views.movie_list, name='movie_list'),  # This will use the `movie_list` function from `views.py`
    path('movie/<int:movie_id>/book/', views.seat_booking, name='seat_booking'),
    path('movie/<int:movie_id>/seats/', views.seat_availability, name='seat-availability'),
    path('booking/history/', views.booking_history, name='booking_history'),
]
