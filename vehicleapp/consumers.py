from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from .models import vehicledetail, Notification
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import sync_to_async, async_to_sync
from channels.db import database_sync_to_async
import json
from django.http import JsonResponse


class clearnotify(SyncConsumer):
    def websocket_connect(self, event):
        print('consumer connected')
        self.send({
            'type':'websocket.accept',
        })
    def websocket_receive(self, event):
        print('websocket noti recieve')
        data= json.loads(event['text'])
        upobj=Notification.objects.filter(pk=data['id'])
        upobj.update(is_seen=True)

    def websocket_disconnect(self, event):
        print('websocket disconnected')
        raise StopConsumer()

class notify(WebsocketConsumer):
    def connect(self):
        self.rmname='notify'
        self.group_name='notifi'
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()
        noti=str(Notification.objects.filter(is_seen=False).count())
        data1=json.loads(noti)
        self.send(text_data=json.dumps({'msg':0, 'data':data1}))
        
    def receive(self):
        print('websocket noti recieve')

    def disconnect(self, close_code):
        print('websocket disconnected')
        raise StopConsumer()

    def send_notifi(self, event):
        noti=str(Notification.objects.filter(is_seen=False).count())
        data=json.loads(event['value'])
        self.send(text_data=json.dumps({'msg':1, 'data':data, 'count':noti}))

class vehicleupdate(SyncConsumer):
    def websocket_connect(self, event):
        print('consumer connected')
        self.send({
            'type':'websocket.accept',
        })
    def websocket_receive(self, event):
        print('websocket recieve')
        data= json.loads(event['text'])
        vehicledetail.objects.filter(pk=data['vid']).update(name=data['name'], vehicleno=data['vno'], speed=data['speed'], avgspeed=data['avgspeed'], temperature=data['temp'], fuellevel=data['fuel'], enginestatus=data['engine'])
        newnot="Vehicle no " +data['vno']+ " has been updated."
        newnotific=Notification(notification=newnot)
        newnotific.save()

        
    def websocket_disconnect(self, event):
        print('websocket disconnected')
        raise StopConsumer()

class vehicleddelete(SyncConsumer):
    def websocket_connect(self, event):
        print('consumer connected')
        self.send({
            'type':'websocket.accept',
        })
    def websocket_receive(self, event):
        print('websocket recieve')
        data= json.loads(event['text'])
        pi=vehicledetail.objects.get(pk=data['id'])
        pi.delete()
        newnot="Deleted successfully."
        newnotific=Notification(notification=newnot)
        newnotific.save()

    def websocket_disconnect(self, event):
        print('websocket disconnected')
        raise StopConsumer()
    
    
class vehicleadd(SyncConsumer):
    def websocket_connect(self, event):
        print('consumer connected')
        self.send({
            'type':'websocket.accept',
        })
    def websocket_receive(self, event):
        print('websocket add recieve')
        data= json.loads(event['text'])
        vehicleinfo=vehicledetail(name=data['name'], vehicleno=data['vno'], speed=data['speed'], avgspeed=data['avgspeed'], temperature=data['temp'], fuellevel=data['fuel'], enginestatus=data['engine'])
        vehicleinfo.save()
        newnot="Vehicle no " +data['vno']+ " has been added."
        newnotific=Notification(notification=newnot)
        newnotific.save()


    def websocket_disconnect(self, event):
        print('websocket disconnected')
        raise StopConsumer()

    
