from  django import forms
from .models import *




class PersonalizadoForm(forms.ModelForm):
    class Meta:
        model= Personalizado
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model= Producto
        fields = "__all__"



class ClienteForm(forms.ModelForm):

    class Meta: 
        model = Cliente
        fields = "__all__"

        widgets = {
            'usuario': forms.HiddenInput(),
           
        }
