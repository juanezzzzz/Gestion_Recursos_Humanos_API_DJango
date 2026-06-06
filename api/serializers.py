from rest_framework import serializers
from .models import (
    Genero, EstadoCivil, TipoDocumento, NivelCargo, TipoContrato, Estado,
    ModalidadCapacitacion, TipoEvaluacion, ResultadoEvaluacion,
    Departamentos, Cargos, Empleados, Contratos, Nomina, Vacaciones,
    Capacitaciones, Evaluaciones, AuditLog
)

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'


class EstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = '__all__'


class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'


class NivelCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelCargo
        fields = '__all__'


class TipoContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContrato
        fields = '__all__'


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'


class ModalidadCapacitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModalidadCapacitacion
        fields = '__all__'


class TipoEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEvaluacion
        fields = '__all__'


class ResultadoEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoEvaluacion
        fields = '__all__'

class DepartamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamentos
        fields = '__all__'


class CargosSerializer(serializers.ModelSerializer):
    id_niveles_cargo = NivelCargoSerializer(read_only=True)

    class Meta:
        model = Cargos
        fields = '__all__'


class EmpleadosSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = ['id_empleados', 'numero_documento', 'primer_nombre', 'primer_apellido', 'email']


class EmpleadosSerializer(serializers.ModelSerializer):
    id_tipos_documento = TipoDocumentoSerializer(read_only=True)
    id_generos = GeneroSerializer(read_only=True)
    id_estados_civiles = EstadoCivilSerializer(read_only=True)
    id_cargos = CargosSerializer(read_only=True)
    id_departamentos = DepartamentosSerializer(read_only=True)

    class Meta:
        model = Empleados
        fields = '__all__'


class ContratosSerializer(serializers.ModelSerializer):
    id_empleados = EmpleadosSerializer(read_only=True)
    id_tipos_contrato = TipoContratoSerializer(read_only=True)
    id_estados = EstadoSerializer(read_only=True)

    class Meta:
        model = Contratos
        fields = '__all__'


class NominaSerializer(serializers.ModelSerializer):
    id_empleados = EmpleadosSerializer(read_only=True)
    id_estados = EstadoSerializer(read_only=True)

    class Meta:
        model = Nomina
        fields = '__all__'


class VacacionesSerializer(serializers.ModelSerializer):
    id_empleados = EmpleadosSimpleSerializer(read_only=True)
    id_estados = EstadoSerializer(read_only=True)
    id_aprobado_por = EmpleadosSimpleSerializer(read_only=True)

    class Meta:
        model = Vacaciones
        fields = '__all__'


class CapacitacionesSerializer(serializers.ModelSerializer):
    id_empleados = EmpleadosSimpleSerializer(read_only=True)
    id_modalidades_capacitacion = ModalidadCapacitacionSerializer(read_only=True)
    id_estados = EstadoSerializer(read_only=True)

    class Meta:
        model = Capacitaciones
        fields = '__all__'


class EvaluacionesSerializer(serializers.ModelSerializer):
    id_empleados = EmpleadosSimpleSerializer(read_only=True)
    id_evaluador = EmpleadosSimpleSerializer(read_only=True)
    id_tipos_evaluacion = TipoEvaluacionSerializer(read_only=True)
    id_resultados_evaluacion = ResultadoEvaluacionSerializer(read_only=True)

    class Meta:
        model = Evaluaciones
        fields = '__all__'


class AuditLogSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = AuditLog
        fields = '__all__'
        read_only_fields = '__all__'


