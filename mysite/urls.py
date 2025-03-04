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

    path('api/', include(router.urls)),
    path('signup/', views.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('', include('bookings.urls')),  
]
