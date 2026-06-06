from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from .models import (
    Genero, EstadoCivil, TipoDocumento, NivelCargo, TipoContrato, Estado,
    ModalidadCapacitacion, TipoEvaluacion, ResultadoEvaluacion,
    Departamentos, Cargos, Empleados, Contratos, Nomina, Vacaciones,
    Capacitaciones, Evaluaciones, AuditLog
)
from .middleware import get_current_user


MODELOS_A_AUDITAR = [
    Genero, EstadoCivil, TipoDocumento, NivelCargo, TipoContrato, Estado,
    ModalidadCapacitacion, TipoEvaluacion, ResultadoEvaluacion,
    Departamentos, Cargos, Empleados, Contratos, Nomina, Vacaciones,
    Capacitaciones, Evaluaciones
]


def registrar_auditoria(sender, instance, operacion, cambios=None, **kwargs):
    usuario = get_current_user()
    if not usuario or not usuario.is_authenticated:
        return

    AuditLog.objects.create(
        usuario=usuario,
        operacion=operacion,
        modelo=sender.__name__,
        objeto_id=str(instance.pk),
        objeto_str=str(instance),
        cambios=cambios or {},
        ip_address=kwargs.get('ip_address'),
    )


@receiver(post_save)
def log_creacion_actualizacion(sender, instance, created, **kwargs):
    if sender not in MODELOS_A_AUDITAR:
        return

    operacion = 'CREATE' if created else 'UPDATE'
    registrar_auditoria(sender, instance, operacion, **kwargs)


@receiver(pre_delete)
def log_eliminacion(sender, instance, **kwargs):
    if sender not in MODELOS_A_AUDITAR:
        return

    registrar_auditoria(sender, instance, 'DELETE', **kwargs)
