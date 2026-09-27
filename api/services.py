from .models import Medico, Consulta


class MedicoService:

    @staticmethod
    def criar(nome, especialidade, crm):
        return Medico.objects.create(
            nome=nome,
            especialidade=especialidade,
            crm=crm
        )


class ConsultaService:

    @staticmethod
    def criar(paciente, data_consulta, valor, status, medico):
        return Consulta.objects.create(
            paciente=paciente,
            data_consulta=data_consulta,
            valor=valor,
            status=status,
            medico=medico
        )
