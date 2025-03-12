from django.forms import ModelForm 
from . import models 

class CreateClientForm(ModelForm):
    class Meta: 
        model = models.Clientes 
        fields = "__all__"


class CreateProductForm(ModelForm):
    class Meta:
        model = models.Produtos 
        fields = "__all__" 


class CreateOrderForm(ModelForm):
    class Meta: 
        model = models.Pedidos 
        fields = "__all__" 

