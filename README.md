# Movie Theater Booking System

This application is designed to allow users to do the following:

1. View the list of available movies at a given theater
2. Create an account, as well as log in
3. Reserve a seat for a given movie on their account
4. View their seat booking history

## Getting Started

To launch the application, navigate to the project directory, at CS4300/Homework 2/movie_theater_booking. Once you are in the proper directory, you can run the server using the following command: python3 manage.py runserver. From here, you should be able to utilize the movie theater booking web application. NOTE: This application is expicitly designed to run on port 8000. Since this is the default port selected by the runserver command, this should require no user intervention.

## Common Issues and Dependencies

A common issue may be that Django and the Django Rest Framework are not installed upon loading this into your own environment.
You can run "pip apt update" to update your environment with a list of the newest package versions, and then use "pip apt install [package name] to obtain the latest versions of Django and the Django Rest Framework.

## Managing Movies

First, run the Django development server using python3 maange.py runserver. Launch the server in your web browser.
From here, you can enter the admin panel at http://127.0.0.1:8000/admin/. Note that this will require you to have admin credentials. If you do not have an admin account, you can create one by running "python3 manage.py createsuperuser".
Once logged in to the admin panel, you can use the interface to add and remove movies. Simply navigate to the "Movies" section.
