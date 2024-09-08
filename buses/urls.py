from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('search-bus', search_bus, name='search-bus'),
    path('buses-list', buses_list, name='buses-list'),
    path('add-bus', add_bus, name='add-bus'),
    path('add-route', add_routes, name='add-route'),
    path('add-schedule', add_schedule, name='add-schedule'),
    path('result', result, name='result')
]