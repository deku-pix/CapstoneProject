from django import forms
from .models import Compra
from django.forms import ModelForm


class CompraForm(ModelForm):
    class Meta:
        required_css_class = 'required'
        model = Compra
        fields = ('id_agencia', 'metodo', 'objeto', 'fecha_reporte', 'fecha_recibo', 'num_licitador',
                  'comentarios', 'comprador', 'num_compra', 'concepto', 'cantidad', 'fondos', 'descripcion', 
                  'id_comprador', 'asignacion', 'procedencia', 'proveedor', 'cuenta')

        labels = {
            'id_agencia': 'id_agencia',
            'metodo': 'metodo',
            'objeto': 'objeto',
            'num_licitador': 'num_licitador:',
            'comentarios': 'comentarios',
            'fecha_reporte': 'fecha_reporte',
            #'fecha_adjudicacion': 'Fecha Final',
            'num_compra': 'Numero de Compra',
            'cantidad': 'Cantidad Total de Gastos $',
            'fondos': 'fondos',
            'descripcion': 'descripcion',
            'id_comprador': 'Comprador',
            #'num_reporte': 'num_reporte',
            'asignacion': 'asignacion',
            'procedencia': 'procedencia',
            'proveedor': 'proveedor',
            'cuenta': 'cuenta',
            'comprador': 'comprador',
            #'alerta': 'Estatal',
            #'alerta': 'Federal',
            'fecha_recibo': 'Fecha Recibo'
        }
        
        widgets = {
            'num_licitador' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Inserte numero Licitador', 'style': 'margin-top:10px'}),
            'metodo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Inserte metodo de compra.', 'style': 'margin-top:10px'}),
            'id_agencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte acrónimo de la agencia.', 'width': '10px', 'style': 'margin-top:10px'}),
            'objeto': forms.Select(attrs={'class': 'form-control', 'placeholder': 'De ser delegada mencione el tipo.', 'style': 'margin-top:10px'}),
            'comentarios': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte comentarios.', 'style': 'margin-top:10px'}),
            'comprador': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte comprador.', 'style': 'margin-top:10px'}),
            'num_compra': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte numero de compra.', 'style': 'margin-top:10px'}),
            'concepto': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Concepto de compra.', 'style': 'margin-top:10px'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total de Gastos', 'style': 'margin-top:10px'}),
            'fondos': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tipo de fondo.', 'style': 'margin-top:10px'}),
            'descripcion': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ofrezca una descripcion.', 'style': 'margin-top:10px'}),
            'id_comprador': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte  ID Comprador', 'style': 'margin-top:10px'}),
            #'num_reporte': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Oficial a cargo.', 'style': 'margin-top:10px'}),
            'asignacion': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Inserte tipo de asignacion.', 'style': 'margin-top:10px'}),
            'procedencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte Procedencia.', 'style': 'margin-top:10px'}),
            'proveedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte nombre proveedor.', 'style': 'margin-top:10px'}),
            'cuenta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte cifra de cuenta.', 'style': 'margin-top:10px'}),
            #'alerta':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte propósito.', 'style': 'margin-top:10px'}),


            'fecha_reporte': forms.SelectDateWidget(years=range(2015, 2030), attrs={'class': 'form-control', 'placeholder': 'Escoja una fecha', 'style': 'margin-top:10px'}),
            #'fecha_adjudicacion': forms.SelectDateWidget(years=range(2015, 2030), attrs={'class': 'form-control', 'placeholder': 'Escoja una fecha', 'style': 'margin-top:10px'}),
            'fecha_recibo': forms.SelectDateWidget(years=range(2015, 2030), attrs={'class': 'form-control', 'placeholder': 'Escoja una fecha', 'style': 'margin-top:10px'}),


        }



#autodate
#duplicate compras 