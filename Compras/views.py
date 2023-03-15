from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Compra
from .forms import CompraForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from datetime import date
# Create your views here.

Compras = []


def AddCompra(request):

    submitted = False
    if request.method == "POST":
        form = CompraForm(request.POST, request.FILES)
        usuario = request.user.username

        if form.is_valid():

            f = form.save(commit=False)
            f.usuario = usuario
            f.save()

        messages.success(request, "Se añadió un nuevo comunicado.")
        return HttpResponseRedirect('comprasAddCompra?submitted=True')

    else:
        form = CompraForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/AddCompra.html', {'form': form, 'submitted': submitted})


def ComprasView(request):
    compras = Compra.objects.order_by('id_agencia')
    context = {'compras': compras}

    return render(request, 'home/Compras.html', context)


def EditarCompra(request, compra_id):
    submitted = False
    if request.method == "POST":

        form = CompraForm(request.POST)

        id_agencia = request.POST['id_agencia']
        metodo = request.POST['metodo']
        objeto = request.POST['objeto']
        num_licitador = request.POST['num_licitador']
        comprador = request.POST['comprador']
        num_compra = request.POST['num_compra']
        comentarios = request.POST['comentarios']
        concepto = request.POST['concepto']
        cantidad = request.POST['cantidad']
        fondos = request.POST['fondos']
        descripcion = request.POST['descripcion']
        id_comprador = request.POST['id_comprador']
        #num_reporte = request.POST['num_reporte']
        asignacion = request.POST['asignacion']
        procedencia = request.POST['procedencia']
        proveedor = request.POST['proveedor']
        cuenta = request.POST['cuenta']
        alerta = request.POST['alerta']

        # Fecha de reporte
        
        fecha_reporte_year = request.POST.get('fecha_reporte_year')
        fecha_reporte_month = request.POST.get('fecha_reporte_month')
        fecha_reporte_day = request.POST.get('fecha_reporte_day')

        # Fecha adjudicacion
        fecha_adjudicacion_day = request.POST.get('fecha_adjudicacion_day')
        fecha_adjudicacion_month = request.POST.get('fecha_adjudicacion_month')
        fecha_adjudicacion_year = request.POST.get('fecha_adjudicacion_year')

        # Fecha reporte
        fecha_reporte_day = request.POST.get('fecha_reporte_day')
        fecha_reporte_month = request.POST.get('fecha_reporte_month')
        fecha_reporte_year = request.POST.get('fecha_reporte_year')

        compra = Compra.objects.get(compra_id=compra_id)

        compra.id_agencia = id_agencia
        compra.metodo = metodo
        compra.objeto = objeto
        compra.num_licitador = num_licitador
        compra.comentarios = comentarios
        compra.asignacion = asignacion
        compra.comprador = comprador
        compra.num_compra = num_compra
        compra.concepto = concepto
        compra.cantidad = cantidad
        compra.fondos = fondos
        compra.descripcion = descripcion
        compra.id_comprador = id_comprador
        #compra.num_reporte = num_reporte
        compra.procedencia = procedencia
        compra.proveedor = proveedor
        compra.cuenta = cuenta
        compra.alerta = alerta

        compra.fecha_reporte = compra.fecha_reporte.replace(day=int(
            fecha_reporte_day), month=int(fecha_reporte_month), year=int(fecha_reporte_year))

        compra.fecha_adjudicacion = compra.fecha_adjudicacion.replace(day=int(
            fecha_adjudicacion_day), month=int(fecha_adjudicacion_month), year=int(fecha_adjudicacion_year))

        compra.fecha_reporte = compra.fecha_reporte.replace(day=int(
            fecha_reporte_day), month=int(fecha_reporte_month), year=int(fecha_reporte_year))

        compra.save()
        message = ('La compra se enmendó ')
        messages.success(request, message)
        submitted = True
        return render(request, 'home/ComprasEdit.html', {'compra': compra, 'submitted': submitted})

    else:
        compra = Compra.objects.get(compra_id=compra_id)
        form = CompraForm(request.POST or None, instance=compra)

        return render(request, 'home/ComprasEdit.html', {'form': form, 'compra': compra, 'submitted': submitted})


def EliminarCompra(request, compra_id=None):

    compra = Compra.objects.get(compra_id=compra_id)
    if request.method == 'POST':

        compra.delete()

        return redirect('/compras')

    return render(request, 'templates/home/ComprasDelete.html', {'compra': compra})
