from rest_framework import serializers
from .models import Medico, Consulta


class ConsultaResumoSerializer(serializers.ModelSerializer):
    # Versão resumida da consulta, SEM o campo "medico",
    # usada dentro do médico para não criar um ciclo (médico -> consulta -> médico...)
    class Meta:
        model = Consulta
        fields = [
            "id",
            "paciente",
            "data_consulta",
            "valor",
            "status",
        ]


class MedicoSerializer(serializers.ModelSerializer):
    # Lista as consultas do médico (somente leitura), usando o related_name="consultas"
    consultas = ConsultaResumoSerializer(many=True, read_only=True)

    class Meta:
        model = Medico
        fields = [
            "id",
            "nome",
            "especialidade",
            "crm",
            "consultas",
        ]


class MedicoSimplesSerializer(serializers.ModelSerializer):
    # Dados básicos do médico, usados dentro da consulta
    class Meta:
        model = Medico
        fields = [
            "id",
            "nome",
            "especialidade",
            "crm",
        ]


class ConsultaSerializer(serializers.ModelSerializer):
    medico = MedicoSimplesSerializer(read_only=True)
    medico_id = serializers.PrimaryKeyRelatedField(
        source="medico",
        queryset=Medico.objects.all(),
        write_only=True
    )

    class Meta:
        model = Consulta
        fields = [
            "id",
            "paciente",
            "data_consulta",
            "valor",
            "status",
            "medico",
            "medico_id",
        ]
