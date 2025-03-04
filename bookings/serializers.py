from rest_framework import serializers
from .models import Movie, Seat, Booking

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    movie = serializers.CharField(source='movie.title')  # Get the title directly from the movie

    class Meta:
        model = Booking
        fields = ['id', 'reserved_at', 'user', 'movie', 'seat']