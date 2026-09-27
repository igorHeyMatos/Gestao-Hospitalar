from rest_framework import serializers
from .models import Medico, Consulta


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = [
            "id",
            "nome",
            "especialidade",
            "crm",
        ]


class ConsultaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer(read_only=True)
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
