import django_filters
from django_filters import CharFilter
from .models import *

class FiltroEmpresa(django_filters.FilterSet):
    razon_social = CharFilter(field_name='razon_social', lookup_expr='icontains')
    class Meta:
        model = Empresa
        fields = '__all__'
        exclude = [
            'id_empleador',
            'celular',
            'telefono',
            'email',
            'direccion',
            'fecha_ultima_actualizacion',
            'nombre_contacto'
        ]