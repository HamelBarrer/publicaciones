from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'phone', 'direction', 'image'
        )
        labels = {
            'phone': 'Telefono',
            'direction': 'Direccion',
            'image': 'Imagen',
        }
