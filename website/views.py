from django.shortcuts import render
from django.views.generic import TemplateView 
from django.views.generic.edit import CreateView 
from . import forms 

from . import models 
class IndexView(TemplateView):
    template_name = "index.html"


class CreatePageView(TemplateView): 
    template_name = "create.html"


class CreateClientView(CreateView):
    template_name = "create_client.html"
    model = models.Clientes 
    form_class = forms.CreateClientForm 


