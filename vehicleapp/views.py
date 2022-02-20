from typing import Counter
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import addvehicles
from django.template.loader import render_to_string
from .models import vehicledetail, Notification
from django.views import View



# Create your views here.
class vehicleview(TemplateView):
    template_name= 'addvehicles.html'
    def get_context_data(self,*args, **kwargs):
        context=super().get_context_data(**kwargs)
        fm=addvehicles()
        context={'form':fm}
        return context

class update_vehicle(TemplateView):
    template_name= 'vehicleupdate.html'
    def get_context_data(self,*args, **kwargs):
        context=super().get_context_data(**kwargs)
        fm=addvehicles()
        context={'form':fm}
        return context



class vehiclelist(TemplateView):
    template_name= 'vehiclelist.html'
    def get_context_data(self,*args, **kwargs):
        context=super().get_context_data(**kwargs)
        fm=vehicledetail.objects.all()
        context={'data':fm}
        return context


class vehicleupdate(View):
    def get(self, request, *args, **kwargs):
        vehicleobj=vehicledetail.objects.get(pk=self.kwargs['pk'])
        fm=addvehicles(instance=vehicleobj)
        context={
            'fm':fm,
            'id':self.kwargs['pk']
        }
        return render(request, 'vehicleupdate.html', context)


class notifications(View):
    def get(self, request, *args, **kwargs):
        noti=Notification.objects.filter(is_seen=False).order_by('isdate').reverse()
        count=noti.count()
        context={
            'notifications':noti,
            'count':count,
        }
        return render(request, 'notifications.html', context)


class vehdetails(View):
    def get(self, request, *args, **kwargs):
        vehicleobj=vehicledetail.objects.get(pk=self.kwargs['pk'])
        return render(request, 'vehicledetails.html', {'data':vehicleobj})
