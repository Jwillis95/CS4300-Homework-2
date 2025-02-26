from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet
from . import views

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/book/', views.seat_booking, name='seat_booking'),
    path('booking/history/', views.booking_history, name='booking_history'),
]

