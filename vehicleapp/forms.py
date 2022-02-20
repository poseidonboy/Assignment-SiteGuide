from django import forms
from .models import vehicledetail


class addvehicles(forms.ModelForm):
    class Meta:
        model=vehicledetail
        fields='__all__'
        # labels={ 'roomname': 'Enter room name', 'type': 'Privacy open'}
        widgets={'name':forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
        'vehicleno':forms.TextInput(attrs={'class':'form-control', 'id':'vnoid'}),
        'speed':forms.TextInput(attrs={'class':'form-control', 'id':'speedid'}),
        'avgspeed':forms.TextInput(attrs={'class':'form-control', 'id':'avgspeedid'}),
        'temperature':forms.TextInput(attrs={'class':'form-control', 'id':'tempid'}),
        'fuellevel':forms.TextInput(attrs={'class':'form-control', 'id':'fuelid'}),
        'enginestatus':forms.TextInput(attrs={'class':'form-control', 'id':'engstatusid'})}



