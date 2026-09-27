import django_filters
from .models import Consulta


class ConsultaFilter(django_filters.FilterSet):
    # Filtro de valor mínimo e máximo da consulta
    valor_min = django_filters.NumberFilter(field_name="valor", lookup_expr="gte")
    valor_max = django_filters.NumberFilter(field_name="valor", lookup_expr="lte")

    # Busca por parte do nome do paciente (case-insensitive)
    paciente = django_filters.CharFilter(field_name="paciente", lookup_expr="icontains")

    class Meta:
        model = Consulta
        fields = ['status', 'medico', 'valor_min', 'valor_max', 'paciente']
