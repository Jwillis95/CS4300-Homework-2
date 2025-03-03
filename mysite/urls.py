from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookings.viewsets import MovieViewSet, SeatViewSet, BookingViewSet
from bookings import views
from django.contrib import admin

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    # API Routes using viewsets (for REST API)
    path('api/', include(router.urls)),

    # Traditional Views Routes (for frontend)
    path('signup/', views.signup, name='signup'),  # Added signup route
    path('admin/', admin.site.urls),
    path('', include('bookings.urls')),  
]
