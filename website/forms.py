from django.forms import ModelForm, Select
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


class UpdateClientForm(ModelForm):
    class Meta: 
        model = models.Clientes 
        fields = "__all__" 
        widgets = {
            "id": Select(attrs={"autofocus": "autofocus", "disabled": "disabled"})
        }

        
class UpdateProductForm(ModelForm):
    class Meta: 
        model = models.Produtos 
        fields = "__all__" 
        widgets = {
            "id": Select(attrs={"autofocus": "autofocus", "disabled": "disabled"})
        }


class UpdateOrderForm(ModelForm):
    class Meta: 
        model = models.Pedidos 
        fields = "__all__" 
        widgets = {
            "id": Select(attrs={"autofocus": "autofocus", "disabled": "disabled"})
        }

