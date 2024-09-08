from django.db import models
import datetime
from datetime import timedelta
class Buses(models.Model):
    name = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Route(models.Model):
    source = models.CharField(max_length=100, null=True)
    destination = models.CharField(max_length=100, null=True)
    distance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    duration = models.DurationField(null=True, blank=True)
    def __str__(self):
        return (self.source + '-' + self.destination)

class Stop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class RouteStop(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    order = models.IntegerField()
    def __str__(self):
        return (self.route.source + "-" + self.stop.location)

class Schedule(models.Model):
    bus = models.ForeignKey(Buses, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.TimeField()
    arrival_time = models.TimeField(null=True, blank=True)
    via = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    def __str__(self):
        return (self.route.source + '-' + self.route.destination)
# Create your models here.
