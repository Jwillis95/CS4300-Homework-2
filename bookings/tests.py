from django.test import TestCase
from .models import Movie, Seat, Booking
from django.contrib.auth.models import User

class MovieTestCase(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(title='Test Movie')

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, 'Test Movie')

    def test_movie_str(self):
        self.assertEqual(str(self.movie), 'Test Movie')

class SeatTestCase(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(title='Test Movie')
        self.seat = Seat.objects.create(movie=self.movie, seat_number=1, is_booked=False)

    def test_seat_creation(self):
        self.assertEqual(self.seat.seat_number, 1)
        self.assertEqual(self.seat.is_booked, False)

    def test_seat_str(self):
        self.assertEqual(str(self.seat), 'Seat 1')

class BookingTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.movie = Movie.objects.create(title='Test Movie')
        self.seat = Seat.objects.create(movie=self.movie, seat_number=1, is_booked=False)
        self.booking = Booking.objects.create(user=self.user, movie=self.movie, seat=self.seat)

    def test_booking_creation(self):
        self.assertEqual(self.booking.user.username, 'testuser')
        self.assertEqual(self.booking.movie.title, 'Test Movie')
        self.assertEqual(self.booking.seat.seat_number, 1)

    def test_booking_str(self):
        self.assertEqual(str(self.booking), f'{self.user.username} booked seat {self.seat.seat_number} for {self.movie.title}')
