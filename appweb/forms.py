from  django import forms
from .models import *




class PersonalizadoForm(forms.ModelForm):
    class Meta:
        model= Personalizado
        fields = "__all__"