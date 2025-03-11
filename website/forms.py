from django.forms import ModelForm 
from . import models 

class CreateClientForm(ModelForm):
    class Meta: 
        model = models.Clientes 
        fields = "__all__"
        
