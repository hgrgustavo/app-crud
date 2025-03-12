from django.urls import path
from website import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="indexpage"),
    path("criar/", views.CreatePageView.as_view(), name="createpage"),
    path("criar/cliente/", views.CreateClientView.as_view(), name="createclientpage"),
    path("criar/produto/", views.CreateProductView.as_view(), name="createproductpage"),
    path("criar/pedido/", views.CreateOrderView.as_view(), name="createorderpage"),

    path("listar/", views.ReadPageView.as_view(), name="readpage"),
    path("listar/cliente/", views.ReadClientView.as_view(), name="readclientpage"),




]
