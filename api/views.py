from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Genero, EstadoCivil, TipoDocumento, NivelCargo, TipoContrato, Estado,
    ModalidadCapacitacion, TipoEvaluacion, ResultadoEvaluacion,
    Departamentos, Cargos, Empleados, Contratos, Nomina, Vacaciones,
    Capacitaciones, Evaluaciones, AuditLog
)
from .serializers import (
    GeneroSerializer, EstadoCivilSerializer, TipoDocumentoSerializer,
    NivelCargoSerializer, TipoContratoSerializer, EstadoSerializer,
    ModalidadCapacitacionSerializer, TipoEvaluacionSerializer,
    ResultadoEvaluacionSerializer, DepartamentosSerializer, CargosSerializer,
    EmpleadosSerializer, ContratosSerializer, NominaSerializer,
    VacacionesSerializer, CapacitacionesSerializer, EvaluacionesSerializer, AuditLogSerializer
)
from .filters import (
    GeneroFilter, EstadoCivilFilter, TipoDocumentoFilter, NivelCargoFilter,
    TipoContratoFilter, EstadoFilter, ModalidadCapacitacionFilter,
    TipoEvaluacionFilter, ResultadoEvaluacionFilter, DepartamentosFilter,
    CargosFilter, EmpleadosFilter, ContratosFilter, NominaFilter,
    VacacionesFilter, CapacitacionesFilter, EvaluacionesFilter
)
from .export_mixin import ExportMixin

class GeneroViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GeneroFilter
    ordering_fields = '__all__'


class EstadoCivilViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = EstadoCivil.objects.all()
    serializer_class = EstadoCivilSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EstadoCivilFilter
    ordering_fields = '__all__'


class TipoDocumentoViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TipoDocumentoFilter
    ordering_fields = '__all__'


class NivelCargoViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = NivelCargo.objects.all()
    serializer_class = NivelCargoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NivelCargoFilter
    ordering_fields = '__all__'


class TipoContratoViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = TipoContrato.objects.all()
    serializer_class = TipoContratoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TipoContratoFilter
    ordering_fields = '__all__'


class EstadoViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EstadoFilter
    ordering_fields = '__all__'


class ModalidadCapacitacionViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = ModalidadCapacitacion.objects.all()
    serializer_class = ModalidadCapacitacionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ModalidadCapacitacionFilter
    ordering_fields = '__all__'


class TipoEvaluacionViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = TipoEvaluacion.objects.all()
    serializer_class = TipoEvaluacionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TipoEvaluacionFilter
    ordering_fields = '__all__'


class ResultadoEvaluacionViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = ResultadoEvaluacion.objects.all()
    serializer_class = ResultadoEvaluacionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ResultadoEvaluacionFilter
    ordering_fields = '__all__'

class DepartamentosViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = Departamentos.objects.all()
    serializer_class = DepartamentosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DepartamentosFilter
    ordering_fields = '__all__'


class CargosViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = Cargos.objects.all()
    serializer_class = CargosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CargosFilter
    ordering_fields = '__all__'


class EmpleadosViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmpleadosFilter
    ordering_fields = '__all__'


class ContratosViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = Contratos.objects.all()
    serializer_class = ContratosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContratosFilter
    ordering_fields = '__all__'


class NominaViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = Nomina.objects.all()
    serializer_class = NominaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NominaFilter
    ordering_fields = '__all__'


class VacacionesViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = Vacaciones.objects.all()
    serializer_class = VacacionesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = VacacionesFilter
    ordering_fields = '__all__'


class CapacitacionesViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = Capacitaciones.objects.all()
    serializer_class = CapacitacionesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CapacitacionesFilter
    ordering_fields = '__all__'


class EvaluacionesViewSet(ExportMixin, viewsets.ModelViewSet):
    queryset = Evaluaciones.objects.all()
    serializer_class = EvaluacionesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EvaluacionesFilter
    ordering_fields = '__all__'


class AuditLogViewSet(ExportMixin, viewsets.ReadOnlyModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = '__all__'

    def get_queryset(self):
        return AuditLog.objects.filter(usuario=self.request.user).order_by('-creado_en')

