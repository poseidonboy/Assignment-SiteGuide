from django.contrib import admin
from .models import Notification, vehicledetail
# Register your models here.
@admin.register(vehicledetail)
class vehicledetailadmin(admin.ModelAdmin):
    list_display=('name', 'vehicleno', 'speed', 'avgspeed', 'temperature', 'fuellevel','enginestatus')


@admin.register(Notification)
class vehicledetailadmin(admin.ModelAdmin):
    list_display=('notification', 'is_seen','isdate')