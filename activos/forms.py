from django import forms
from .models import TipoActivo, Software,Hardware


class TipoActivoForm(forms.ModelForm):
    class Meta:
        model = TipoActivo
        fields = '__all__'
        
        
class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = '__all__'
        
class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = '__all__'