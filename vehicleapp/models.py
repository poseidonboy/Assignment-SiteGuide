import imp
import json
from django.db import models
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.utils.timezone import now

from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer


# Create your models here.
class vehicledetail(models.Model):
    name=models.CharField(max_length=100)
    vehicleno=models.CharField(max_length=100)
    speed= models.FloatField()
    avgspeed= models.FloatField()
    temperature= models.IntegerField()
    fuellevel= models.IntegerField()
    enginestatus= models.CharField(max_length=100)


class Notification(models.Model):
    notification=models.CharField(max_length=10000)
    is_seen=models.BooleanField(default=False)
    isdate=models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        channel_layer=get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'notifi', {
            'type':'send_notifi',
            'value':json.dumps(self.notification)
        }
        )
        super(Notification, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        notification_objs=Notification.objects.filter(is_seen=False).count()
        context={
            'count':notification_objs,
            'current_notif':self.notification
        }
        channel_layer=get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'notifi', {
            'type':'send_notifi',
            'value':json.dumps(context)
        }
        )
        super(Notification, self).delete(*args, **kwargs)
