from django.db import models


class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome


class Consulta(models.Model):
    STATUS_CHOICES = [
        ('AGENDADA', 'Agendada'),
        ('REALIZADA', 'Realizada'),
        ('CANCELADA', 'Cancelada'),
    ]

    paciente = models.CharField(max_length=150)
    data_consulta = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AGENDADA')

    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE,
        related_name="consultas"
    )

    def __str__(self):
        return f"{self.paciente} - {self.data_consulta}"
