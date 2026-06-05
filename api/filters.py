import django_filters
from .models import (
    Genero, EstadoCivil, TipoDocumento, NivelCargo, TipoContrato, Estado,
    ModalidadCapacitacion, TipoEvaluacion, ResultadoEvaluacion,
    Departamentos, Cargos, Empleados, Contratos, Nomina, Vacaciones,
    Capacitaciones, Evaluaciones, AuditLog
)


class GeneroFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()
    class Meta:
        model = Genero
        fields = ['nombre', 'activo']


class EstadoCivilFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()
    class Meta:
        model = EstadoCivil
        fields = ['nombre', 'activo']


class TipoDocumentoFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains')
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()
    class Meta:
        model = TipoDocumento
        fields = ['codigo', 'nombre', 'activo']


class NivelCargoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()
    class Meta:
        model = NivelCargo
        fields = ['nombre', 'activo']


class TipoContratoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()
    class Meta:
        model = TipoContrato
        fields = ['nombre', 'activo']


class EstadoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    contexto = django_filters.ChoiceFilter(choices=Estado.CONTEXTO_CHOICES)
    activo = django_filters.BooleanFilter()
    class Meta:
        model = Estado
        fields = ['nombre', 'contexto', 'activo']


class ModalidadCapacitacionFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()
    class Meta:
        model = ModalidadCapacitacion
        fields = ['nombre', 'activo']


class TipoEvaluacionFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()
    class Meta:
        model = TipoEvaluacion
        fields = ['nombre', 'activo']


class ResultadoEvaluacionFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()
    class Meta:
        model = ResultadoEvaluacion
        fields = ['nombre', 'activo']


class DepartamentosFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter()
    class Meta:
        model = Departamentos
        fields = ['nombre', 'descripcion', 'activo']


class CargosFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')
    id_niveles_cargo = django_filters.NumberFilter()
    salario_base_minimo_min = django_filters.NumberFilter(field_name='salario_base_minimo', lookup_expr='gte')
    salario_base_minimo_max = django_filters.NumberFilter(field_name='salario_base_minimo', lookup_expr='lte')
    salario_base_maximo_min = django_filters.NumberFilter(field_name='salario_base_maximo', lookup_expr='gte')
    salario_base_maximo_max = django_filters.NumberFilter(field_name='salario_base_maximo', lookup_expr='lte')
    activo = django_filters.BooleanFilter()
    class Meta:
        model = Cargos
        fields = ['nombre', 'id_niveles_cargo', 'activo']


class EmpleadosFilter(django_filters.FilterSet):
    numero_documento = django_filters.CharFilter(lookup_expr='icontains')
    primer_nombre = django_filters.CharFilter(lookup_expr='icontains')
    primer_apellido = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    id_tipos_documento = django_filters.NumberFilter()
    id_generos = django_filters.NumberFilter()
    id_estados_civiles = django_filters.NumberFilter()
    id_cargos = django_filters.NumberFilter()
    id_departamentos = django_filters.NumberFilter()
    ciudad = django_filters.CharFilter(lookup_expr='icontains')
    fecha_ingreso = django_filters.DateFilter()
    fecha_ingreso_min = django_filters.DateFilter(field_name='fecha_ingreso', lookup_expr='gte')
    fecha_ingreso_max = django_filters.DateFilter(field_name='fecha_ingreso', lookup_expr='lte')
    fecha_retiro = django_filters.DateFilter()
    activo = django_filters.BooleanFilter()
    class Meta:
        model = Empleados
        fields = [
            'numero_documento', 'primer_nombre', 'primer_apellido', 'email',
            'id_tipos_documento', 'id_generos', 'id_estados_civiles',
            'id_cargos', 'id_departamentos', 'ciudad', 'activo'
        ]


class ContratosFilter(django_filters.FilterSet):
    id_empleados = django_filters.NumberFilter()
    id_tipos_contrato = django_filters.NumberFilter()
    fecha_inicio = django_filters.DateFilter()
    fecha_inicio_min = django_filters.DateFilter(field_name='fecha_inicio', lookup_expr='gte')
    fecha_inicio_max = django_filters.DateFilter(field_name='fecha_inicio', lookup_expr='lte')
    fecha_fin = django_filters.DateFilter()
    salario_min = django_filters.NumberFilter(field_name='salario', lookup_expr='gte')
    salario_max = django_filters.NumberFilter(field_name='salario', lookup_expr='lte')
    id_estados = django_filters.NumberFilter()
    activo = django_filters.BooleanFilter()
    class Meta:
        model = Contratos
        fields = ['id_empleados', 'id_tipos_contrato', 'id_estados', 'activo']


class NominaFilter(django_filters.FilterSet):
    id_empleados = django_filters.NumberFilter()
    periodo_inicio = django_filters.DateFilter()
    periodo_inicio_min = django_filters.DateFilter(field_name='periodo_inicio', lookup_expr='gte')
    periodo_inicio_max = django_filters.DateFilter(field_name='periodo_inicio', lookup_expr='lte')
    periodo_fin = django_filters.DateFilter()
    salario_base_min = django_filters.NumberFilter(field_name='salario_base', lookup_expr='gte')
    salario_base_max = django_filters.NumberFilter(field_name='salario_base', lookup_expr='lte')
    neto_pagado_min = django_filters.NumberFilter(field_name='neto_pagado', lookup_expr='gte')
    neto_pagado_max = django_filters.NumberFilter(field_name='neto_pagado', lookup_expr='lte')
    id_estados = django_filters.NumberFilter()
    fecha_pago = django_filters.DateFilter()
    activo = django_filters.BooleanFilter()
    class Meta:
        model = Nomina
        fields = ['id_empleados', 'id_estados', 'activo']


class VacacionesFilter(django_filters.FilterSet):
    id_empleados = django_filters.NumberFilter()
    fecha_inicio = django_filters.DateFilter()
    fecha_inicio_min = django_filters.DateFilter(field_name='fecha_inicio', lookup_expr='gte')
    fecha_inicio_max = django_filters.DateFilter(field_name='fecha_inicio', lookup_expr='lte')
    dias_solicitados_min = django_filters.NumberFilter(field_name='dias_solicitados', lookup_expr='gte')
    dias_solicitados_max = django_filters.NumberFilter(field_name='dias_solicitados', lookup_expr='lte')
    id_estados = django_filters.NumberFilter()
    id_aprobado_por = django_filters.NumberFilter()
    activo = django_filters.BooleanFilter()
    class Meta:
        model = Vacaciones
        fields = ['id_empleados', 'id_estados', 'id_aprobado_por', 'activo']


class CapacitacionesFilter(django_filters.FilterSet):
    id_empleados = django_filters.NumberFilter()
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    proveedor = django_filters.CharFilter(lookup_expr='icontains')
    id_modalidades_capacitacion = django_filters.NumberFilter()
    duracion_horas_min = django_filters.NumberFilter(field_name='duracion_horas', lookup_expr='gte')
    duracion_horas_max = django_filters.NumberFilter(field_name='duracion_horas', lookup_expr='lte')
    fecha_inicio = django_filters.DateFilter()
    fecha_inicio_min = django_filters.DateFilter(field_name='fecha_inicio', lookup_expr='gte')
    fecha_inicio_max = django_filters.DateFilter(field_name='fecha_inicio', lookup_expr='lte')
    costo_min = django_filters.NumberFilter(field_name='costo', lookup_expr='gte')
    costo_max = django_filters.NumberFilter(field_name='costo', lookup_expr='lte')
    calificacion_min = django_filters.NumberFilter(field_name='calificacion', lookup_expr='gte')
    calificacion_max = django_filters.NumberFilter(field_name='calificacion', lookup_expr='lte')
    aprobado = django_filters.BooleanFilter()
    id_estados = django_filters.NumberFilter()
    activo = django_filters.BooleanFilter()
    class Meta:
        model = Capacitaciones
        fields = [
            'id_empleados', 'nombre', 'id_modalidades_capacitacion',
            'aprobado', 'id_estados', 'activo'
        ]


class EvaluacionesFilter(django_filters.FilterSet):
    id_empleados = django_filters.NumberFilter()
    id_evaluador = django_filters.NumberFilter()
    id_tipos_evaluacion = django_filters.NumberFilter()
    fecha_evaluacion = django_filters.DateFilter()
    fecha_evaluacion_min = django_filters.DateFilter(field_name='fecha_evaluacion', lookup_expr='gte')
    fecha_evaluacion_max = django_filters.DateFilter(field_name='fecha_evaluacion', lookup_expr='lte')
    puntaje_total_min = django_filters.NumberFilter(field_name='puntaje_total', lookup_expr='gte')
    puntaje_total_max = django_filters.NumberFilter(field_name='puntaje_total', lookup_expr='lte')
    id_resultados_evaluacion = django_filters.NumberFilter()
    activo = django_filters.BooleanFilter()
    class Meta:
        model = Evaluaciones
        fields = [
            'id_empleados', 'id_evaluador', 'id_tipos_evaluacion',
            'id_resultados_evaluacion', 'activo'
        ]


class AuditLogFilter(django_filters.FilterSet):
    usuario = django_filters.CharFilter(field_name='usuario__username', lookup_expr='icontains')
    operacion = django_filters.CharFilter(lookup_expr='icontains')
    modelo = django_filters.CharFilter(lookup_expr='icontains')
    creado_en = django_filters.DateFilter()
    creado_en_min = django_filters.DateFilter(field_name='creado_en', lookup_expr='gte')
    creado_en_max = django_filters.DateFilter(field_name='creado_en', lookup_expr='lte')

    class Meta:
        model = AuditLog
        fields = ['usuario', 'operacion', 'modelo', 'creado_en']

