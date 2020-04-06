from django.urls import path
from . import views


app_name = 'formularze'
urlpatterns = [
    path('', views.ListaPytan.as_view(), name='lista-pytan'),
    path('pytanie/glosuj/<int:pid>', views.pytanie_glosuj, name='pytanie-glosuj'),
    path('pytanie/<int:pk>', views.LiczbaGlosow.as_view(), name='liczba-glosow'),
]