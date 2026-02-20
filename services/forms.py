from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):
    """
    A form that automatically creates fields
    based on the Service model
    """

    class Meta:
        model = Service
        fields = '__all__'
        labels = {
            'service_type': 'Service Type',
            'session_count': 'Number of Sessions',
            'duration': 'Duration (minutes)',
            'featured_image': 'Service Image',
        }
