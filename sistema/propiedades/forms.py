from django import forms
from .models import Inmuebles

class InmueblesForm(forms.ModelForm):
    class Meta:
        model = Inmuebles
        fields = '__all__'