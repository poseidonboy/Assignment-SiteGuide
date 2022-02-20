from django.urls import path
from . import consumers

ws_patterns=[
    path('vehicle/', consumers.vehicleadd.as_asgi()),
    path('vehiclelist/', consumers.vehicleddelete.as_asgi()),
    path('vehicleupdate/', consumers.vehicleupdate.as_asgi()),
    path('notifications/', consumers.notify.as_asgi()),
    path('clearnotifications/', consumers.clearnotify.as_asgi()),
]