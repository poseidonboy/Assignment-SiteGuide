from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .import views

urlpatterns = [
    path('', views.vehicleview.as_view(), name='vehicle'),
    path('vehiclelist/', views.vehiclelist.as_view(), name='vehiclelist'),
    path('vehicleupdate/<int:pk>/', views.vehicleupdate.as_view(), name='updateveh'),
    path('notifications/', views.notifications.as_view(), name='notifications'),
    path('vehicledetails/<int:pk>/', views.vehdetails.as_view(), name='vehicledetails'),
]