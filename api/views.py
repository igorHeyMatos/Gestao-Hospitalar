from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Medico, Consulta
from .serializers import MedicoSerializer, ConsultaSerializer
from .filters import ConsultaFilter
from .services import MedicoService, ConsultaService


class MedicoViewSet(viewsets.ModelViewSet):
    # order_by: a paginação precisa de uma ordem fixa
    # prefetch_related: busca as consultas de cada médico de uma vez só
    queryset = Medico.objects.prefetch_related("consultas").order_by("id")
    serializer_class = MedicoSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['especialidade']

    def perform_create(self, serializer):
        medico = MedicoService.criar(
            nome=serializer.validated_data["nome"],
            especialidade=serializer.validated_data["especialidade"],
            crm=serializer.validated_data["crm"]
        )
        serializer.instance = medico


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.select_related("medico").order_by("id")
    serializer_class = ConsultaSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = ConsultaFilter  # Usa o filtro avançado customizado

    def perform_create(self, serializer):
        consulta = ConsultaService.criar(
            paciente=serializer.validated_data["paciente"],
            data_consulta=serializer.validated_data["data_consulta"],
            valor=serializer.validated_data["valor"],
            status=serializer.validated_data.get("status", "AGENDADA"),
            medico=serializer.validated_data["medico"]
        )
        serializer.instance = consulta
