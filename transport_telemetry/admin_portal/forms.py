# admin_portal/forms.py
from django import forms
from .models import Route, ThirdPartyLogistics, Checkpoint, Driver

# admin_portal/forms.py
class CheckpointForm(forms.ModelForm):
    class Meta:
        model = Checkpoint
        fields = ['name', 'load_location', 'unload_location', 'load_tonnes']

class RouteForm(forms.ModelForm):
    checkpoint_count = forms.IntegerField(min_value=1, required=True, label="Number of Checkpoints")

    class Meta:
        model = Route
        fields = ['route_name', 'origin', 'destination', 'assigned_driver']

class ThirdPartyLogisticsForm(forms.ModelForm):
    class Meta:
        model = ThirdPartyLogistics
        fields = ['company_name', 'request_load', 'route']


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'contact_number', 'is_available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter driver name'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
