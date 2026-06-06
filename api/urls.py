from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GeneroViewSet, EstadoCivilViewSet, TipoDocumentoViewSet, NivelCargoViewSet,
    TipoContratoViewSet, EstadoViewSet, ModalidadCapacitacionViewSet,
    TipoEvaluacionViewSet, ResultadoEvaluacionViewSet, DepartamentosViewSet,
    CargosViewSet, EmpleadosViewSet, ContratosViewSet, NominaViewSet,
    VacacionesViewSet, CapacitacionesViewSet, EvaluacionesViewSet, AuditLogViewSet
)
from .auth_views import login, refresh_token

router = DefaultRouter()

router.register (r'generos', GeneroViewSet)
router.register (r'estados_civiles', EstadoCivilViewSet)
router.register (r'tipos_documento', TipoDocumentoViewSet)
router.register (r'niveles_cargo', NivelCargoViewSet)
router.register (r'tipos_contrato', TipoContratoViewSet)
router.register (r'estados', EstadoViewSet)
router.register (r'modalidades_capacitacion', ModalidadCapacitacionViewSet)
router.register (r'tipos_evaluacion', TipoEvaluacionViewSet)
router.register (r'resultados_evaluacion', ResultadoEvaluacionViewSet)
router.register (r'departamentos', DepartamentosViewSet)
router.register (r'cargos', CargosViewSet)
router.register (r'empleados', EmpleadosViewSet)
router.register (r'contratos', ContratosViewSet)
router.register (r'nomina', NominaViewSet)
router.register (r'vacaciones', VacacionesViewSet)
router.register (r'capacitaciones', CapacitacionesViewSet)
router.register (r'evaluaciones', EvaluacionesViewSet)
router.register (r'audit-logs', AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('auth/login/', login, name='login'),
    path('auth/refresh/', refresh_token, name='refresh-token'),
    path('', include(router.urls))
]
