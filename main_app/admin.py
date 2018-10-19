from django.contrib import admin
from .models import Hiker, Trail, Trip

# Register your models here.

admin.site.register(Hiker)
admin.site.register(Trail)
admin.site.register(Trip)
