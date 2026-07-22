from django.db import models


class Estudiante(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    curso = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Docente(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Falta(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    fecha = models.DateField()

    TIPO_FALTA = [
        ("hora", "Por hora"),
        ("dia", "Todo el día"),
    ]

    tipo = models.CharField(max_length=10, choices=TIPO_FALTA)

    materia = models.CharField(max_length=100, blank=True)
    hora = models.CharField(max_length=20, blank=True)

    motivo = models.TextField()

    justificada = models.BooleanField(default=False)

    ESTADOS = [
        ("Pendiente", "Pendiente"),
        ("Aprobada", "Aprobada"),
        ("Rechazada", "Rechazada"),
    ]

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="Pendiente"
    )

    fecha_justificacion = models.DateField(
        null=True,
        blank=True
    )

    observaciones = models.TextField(
        blank=True
    )

    documento = models.FileField(
        upload_to="justificaciones/",
        null=True,
        blank=True
    )

    fecha_revision = models.DateField(
        null=True,
        blank=True
    )

    observaciones_coordinador = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.estudiante} - {self.fecha}"