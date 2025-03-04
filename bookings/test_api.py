from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking

class MovieAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.movie = Movie.objects.create(title='Test Movie')

    def test_movie_list(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  
        self.assertEqual(response.data[0]['title'], 'Test Movie')



class SeatAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.movie = Movie.objects.create(title='Test Movie')
        self.seat = Seat.objects.create(movie=self.movie, seat_number=1, is_booked=False)

    def test_seat_list(self):
        response = self.client.get('/api/seats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 
        self.assertEqual(response.data[0]['seat_number'], 1)

    def test_seat_create(self):
        data = {'movie': self.movie.id, 'seat_number': 2, 'is_booked': False}
        response = self.client.post('/api/seats/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['seat_number'], 2)

class BookingAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.movie = Movie.objects.create(title='Test Movie')
        self.seat = Seat.objects.create(movie=self.movie, seat_number=1, is_booked=False)
        self.booking = Booking.objects.create(user=self.user, movie=self.movie, seat=self.seat)


    def test_booking_invalid_create(self):
        data = {
            'user': self.user.id,
            'movie': self.movie.id,
            'seat': 999 
        }
        response = self.client.post('/api/bookings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
