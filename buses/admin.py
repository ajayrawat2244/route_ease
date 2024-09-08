from django.contrib import admin
from .models import *

admin.site.register(Buses)
admin.site.register(Route)
admin.site.register(Stop)
admin.site.register(RouteStop)
admin.site.register(Schedule)
# Register your models here.
