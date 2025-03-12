from django.shortcuts import render
from django.views.generic import TemplateView 
from django.views.generic.edit import CreateView 
from . import forms, models 


class IndexView(TemplateView):
    template_name = "index.html"


# creating
class CreatePageView(TemplateView): 
    template_name = "create.html"


class CreateClientView(CreateView):
    template_name = "create_client.html"
    model = models.Clientes 
    form_class = forms.CreateClientForm
    success_url = "#"


class CreateProductView(CreateView):
    template_name = "create_product.html"
    model = models.Produtos 
    form_class = forms.CreateProductForm
    success_url = "#"


class CreateOrderView(CreateView):
    template_name = "create_order.html"
    model = models.Pedidos 
    form_class = forms.CreateOrderForm
    success_url = "#"


# reading 
class ReadPageView(TemplateView):
    template_name = "read.html"


class ReadClientView(ListView):
    template_name = "read_client.html"
    model = models.Clientes 
    context_object_name = "clients"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        
        return context;
    





