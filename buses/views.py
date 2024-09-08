from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def buses_list(request):
    source = request.GET.get('source')
    destination = request.GET.get('destination')
    route = Route.objects.get(source=source.lower(), destination=destination.lower())
    routes = Schedule.objects.filter(route=route)
    return render(request, 'buses_list.html', {'routes': routes, 'route': route})

def search_bus(request):
    return render(request, 'search_bus.html')

def home(request):
    return render(request, 'home.html')
def add_bus(request):
    if request.method == 'POST':
        bus_name = request.POST.getlist('bus_name[]')
        bus_type = request.POST.getlist('bus_type[]')
        for name, type in zip(bus_name, bus_type):
            Buses.objects.create(name=name, type=type)
        return redirect('add-route')
    return render(request, 'add_bus.html')

def add_routes(request):
    if request.method == 'POST':
        source_list = request.POST.getlist('source[]')
        destination_list = request.POST.getlist('destination[]')
        for source, destination in zip(source_list, destination_list):
            Route.objects.create(source=source, destination=destination)
        return redirect('add-schedule')
    return render(request, 'add_route.html')

def add_schedule(request):
    bus = Buses.objects.all()
    route = Route.objects.all()
    if request.method == 'POST':
        bus_list = request.POST.getlist('bus[]')
        route_list = request.POST.getlist('route[]')
        departure_time_list = request.POST.getlist('departure_time[]')
        via_list = request.POST.getlist('via[]')
        price_list = request.POST.getlist('price[]')
        for buses, routes, departure_time, via, price in zip(bus_list, route_list, departure_time_list, via_list, price_list):
            bus =Buses.objects.get(id=int(buses))
            route =Route.objects.get(id=int(routes))
            Schedule.objects.create(
                bus=bus,
                route=route,
                departure_time=departure_time,
                via=via,
                price=price
            )
        return redirect('search-bus')
    return render(request, 'add_schedule.html', {'bus': bus, 'route': route}),

def result(request):
    source = request.GET.get('source')
    destination = request.GET.get('destination')
    route = Route.objects.get(source=source.lower(), destination=destination.lower())
    routes = Schedule.objects.filter(route=route)
    return render(request, 'result.html', {'routes': routes, 'route': route, 'source': source, 'destination': destination})
