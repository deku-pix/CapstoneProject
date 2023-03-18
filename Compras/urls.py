from django.urls import path

from .views import (ComprasView, AddCompra, EliminarCompra, EditarCompra)

app_name = 'Compras'
urlpatterns = [

    path('', ComprasView, name='compra'),
    path('AddCompra', AddCompra, name='addcompra'),
    path('eliminarcompra/<compra_id>',EliminarCompra, name='eliminarcompra'),
    path('EditarCompra/<compra_id>', EditarCompra, name='editarcompra'),



]
