from django.urls import path
from . import views
urlpatterns=[
   path('hellow', views.flight_reservation, name='flight_reservation'),
     
]