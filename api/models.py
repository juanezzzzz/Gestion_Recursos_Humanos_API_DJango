from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .managers import SoftDeleteManager
from .middleware import get_current_user


class Genero(models.Model):
    objects = SoftDeleteManager()

    id_generos     = models.AutoField     (primary_key=True)
    nombre         = models.CharField     (max_length=20)
    activo         = models.BooleanField  (default=True)
    creado_en      = models.DateTimeField (auto_now_add=True)
    actualizado_en = models.DateTimeField (auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'generos'


class EstadoCivil(models.Model):
    objects = SoftDeleteManager()

    id_estados_civiles = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'estados_civiles'


class TipoDocumento(models.Model):
    objects = SoftDeleteManager()

    id_tipos_documento = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipos_documento'


class NivelCargo(models.Model):
    objects = SoftDeleteManager()

    id_niveles_cargo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'niveles_cargo'


class TipoContrato(models.Model):
    objects = SoftDeleteManager()

    id_tipos_contrato = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipos_contrato'


class Estado(models.Model):
    objects = SoftDeleteManager()

    CONTEXTO_CHOICES = [
        ('CONTRATO', 'Contrato'),
        ('NOMINA', 'Nómina'),
        ('VACACIONES', 'Vacaciones'),
        ('CAPACITACION', 'Capacitación'),
    ]

    id_estados = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    contexto = models.CharField(max_length=15, choices=CONTEXTO_CHOICES)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return f"{self.nombre} ({self.get_contexto_display()})"

    class Meta:
        db_table = 'estados'
        unique_together = ('nombre', 'contexto')


class ModalidadCapacitacion(models.Model):
    objects = SoftDeleteManager()

    id_modalidades_capacitacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'modalidades_capacitacion'


class TipoEvaluacion(models.Model):
    objects = SoftDeleteManager()

    id_tipos_evaluacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipos_evaluacion'


class ResultadoEvaluacion(models.Model):
    objects = SoftDeleteManager()

    id_resultados_evaluacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'resultados_evaluacion'

class Departamentos(models.Model):
    objects = SoftDeleteManager()

    id_departamentos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'departamentos'


class Cargos(models.Model):
    objects = SoftDeleteManager()

    id_cargos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    id_niveles_cargo = models.ForeignKey(NivelCargo, on_delete=models.PROTECT, db_column='id_niveles_cargo')
    salario_base_minimo = models.DecimalField(max_digits=12, decimal_places=2)
    salario_base_maximo = models.DecimalField(max_digits=12, decimal_places=2)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cargos'


class Empleados(models.Model):
    objects = SoftDeleteManager()

    id_empleados = models.AutoField(primary_key=True)
    id_tipos_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT, db_column='id_tipos_documento')
    numero_documento = models.CharField(max_length=20, unique=True)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, null=True, blank=True)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, null=True, blank=True)
    fecha_nacimiento = models.DateField()
    id_generos = models.ForeignKey(Genero, on_delete=models.PROTECT, db_column='id_generos')
    id_estados_civiles = models.ForeignKey(EstadoCivil, on_delete=models.PROTECT, db_column='id_estados_civiles')
    email = models.EmailField(max_length=254, unique=True)
    email_corporativo = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    telefono = models.CharField(max_length=20)
    telefono_emergencia = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.TextField()
    ciudad = models.CharField(max_length=100)
    id_cargos = models.ForeignKey(Cargos, on_delete=models.PROTECT, db_column='id_cargos')
    id_departamentos = models.ForeignKey(Departamentos, on_delete=models.PROTECT, db_column='id_departamentos')
    fecha_ingreso = models.DateField()
    fecha_retiro = models.DateField(null=True, blank=True)
    foto = models.CharField(max_length=300, null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido} ({self.numero_documento})"

    class Meta:
        db_table = 'empleados'

class Contratos(models.Model):
    objects = SoftDeleteManager()

    id_contratos = models.AutoField(primary_key=True)
    id_empleados = models.ForeignKey(Empleados, on_delete=models.PROTECT, db_column='id_empleados')
    id_tipos_contrato = models.ForeignKey(TipoContrato, on_delete=models.PROTECT, db_column='id_tipos_contrato')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    salario = models.DecimalField(max_digits=12, decimal_places=2)
    jornada_horas = models.SmallIntegerField(default=8)
    id_estados = models.ForeignKey(Estado, on_delete=models.PROTECT, db_column='id_estados', limit_choices_to={'contexto': 'CONTRATO'})
    url_documento = models.CharField(max_length=300, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return f"Contrato {self.id_contratos} - {self.id_empleados}"

    class Meta:
        db_table = 'contratos'


class Nomina(models.Model):
    objects = SoftDeleteManager()

    id_nomina = models.AutoField(primary_key=True)
    id_empleados = models.ForeignKey(Empleados, on_delete=models.PROTECT, db_column='id_empleados')
    periodo_inicio = models.DateField()
    periodo_fin = models.DateField()
    salario_base = models.DecimalField(max_digits=12, decimal_places=2)
    horas_extras = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    bonificaciones = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    auxilio_transporte = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    otros_devengados = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_devengado = models.DecimalField(max_digits=12, decimal_places=2)
    salud = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    pension = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    retencion_fuente = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    otras_deducciones = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_deducciones = models.DecimalField(max_digits=12, decimal_places=2)
    neto_pagado = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_pago = models.DateField(null=True, blank=True)
    id_estados = models.ForeignKey(Estado, on_delete=models.PROTECT, db_column='id_estados', limit_choices_to={'contexto': 'NOMINA'})
    observaciones = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return f"Nómina {self.id_nomina} - {self.id_empleados}"

    class Meta:
        db_table = 'nomina'
        unique_together = ('id_empleados', 'periodo_inicio', 'periodo_fin')


class Vacaciones(models.Model):
    objects = SoftDeleteManager()

    id_vacaciones = models.AutoField(primary_key=True)
    id_empleados = models.ForeignKey(Empleados, on_delete=models.PROTECT, db_column='id_empleados', related_name='vacaciones')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    dias_solicitados = models.SmallIntegerField()
    dias_habiles = models.SmallIntegerField()
    id_estados = models.ForeignKey(Estado, on_delete=models.PROTECT, db_column='id_estados', limit_choices_to={'contexto': 'VACACIONES'})
    id_aprobado_por = models.ForeignKey(Empleados, on_delete=models.SET_NULL, db_column='id_aprobado_por', related_name='vacaciones_aprobadas', null=True, blank=True)
    fecha_aprobacion = models.DateTimeField(null=True, blank=True)
    motivo_rechazo = models.TextField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return f"Vacaciones {self.id_vacaciones} - {self.id_empleados}"

    class Meta:
        db_table = 'vacaciones'


class Capacitaciones(models.Model):
    objects = SoftDeleteManager()

    id_capacitaciones = models.AutoField(primary_key=True)
    id_empleados = models.ForeignKey(Empleados, on_delete=models.PROTECT, db_column='id_empleados')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    proveedor = models.CharField(max_length=150, null=True, blank=True)
    id_modalidades_capacitacion = models.ForeignKey(ModalidadCapacitacion, on_delete=models.PROTECT, db_column='id_modalidades_capacitacion')
    duracion_horas = models.SmallIntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    lugar = models.CharField(max_length=200, null=True, blank=True)
    costo = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    calificacion = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    aprobado = models.BooleanField(default=False)
    url_certificado = models.CharField(max_length=300, null=True, blank=True)
    id_estados = models.ForeignKey(Estado, on_delete=models.PROTECT, db_column='id_estados', limit_choices_to={'contexto': 'CAPACITACION'})
    observaciones = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return f"{self.nombre} - {self.id_empleados}"

    class Meta:
        db_table = 'capacitaciones'


class Evaluaciones(models.Model):
    objects = SoftDeleteManager()

    id_evaluaciones = models.AutoField(primary_key=True)
    id_empleados = models.ForeignKey(Empleados, on_delete=models.PROTECT, db_column='id_empleados', related_name='evaluaciones')
    id_evaluador = models.ForeignKey(Empleados, on_delete=models.PROTECT, db_column='id_evaluador', related_name='evaluaciones_realizadas')
    id_tipos_evaluacion = models.ForeignKey(TipoEvaluacion, on_delete=models.PROTECT, db_column='id_tipos_evaluacion')
    fecha_evaluacion = models.DateField()
    periodo_evaluado_inicio = models.DateField()
    periodo_evaluado_fin = models.DateField()
    puntualidad = models.SmallIntegerField()
    productividad = models.SmallIntegerField()
    trabajo_equipo = models.SmallIntegerField()
    calidad_trabajo = models.SmallIntegerField()
    liderazgo = models.SmallIntegerField(default=0)
    puntaje_total = models.DecimalField(max_digits=5, decimal_places=2)
    id_resultados_evaluacion = models.ForeignKey(ResultadoEvaluacion, on_delete=models.PROTECT, db_column='id_resultados_evaluacion')
    fortalezas = models.TextField(null=True, blank=True)
    areas_mejora = models.TextField(null=True, blank=True)
    plan_accion = models.TextField(null=True, blank=True)
    comentarios_empleado = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_creados')
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modificados')

    def __str__(self):
        return f"Evaluación {self.id_evaluaciones} - {self.id_empleados}"

    class Meta:
        db_table = 'evaluaciones'


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


@receiver(pre_save)
def auto_audit_user(sender, instance, **kwargs):
    current_user = get_current_user()
    if current_user and current_user.is_authenticated:
        if not instance.pk:
            instance.usuario_creacion = current_user
        instance.usuario_modificacion = current_user
