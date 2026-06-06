from django.db import models
from django.contrib.auth.models import User


class AuditLog(models.Model):
    OPERACIONES = [
        ('CREATE', 'Creación'),
        ('UPDATE', 'Actualización'),
        ('DELETE', 'Eliminación'),
    ]

    id_audit_log = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    operacion = models.CharField(max_length=10, choices=OPERACIONES)
    modelo = models.CharField(max_length=100)
    objeto_id = models.CharField(max_length=100)
    objeto_str = models.CharField(max_length=255, null=True, blank=True)
    cambios = models.JSONField(null=True, blank=True)
    ip_address = models.CharField(max_length=45, null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'audit_logs'
        ordering = ['-creado_en']

    def __str__(self):
        return f"{self.usuario} - {self.operacion} {self.modelo} ({self.creado_en})"
