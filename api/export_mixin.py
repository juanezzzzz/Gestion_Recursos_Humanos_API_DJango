from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .export_utils import export_queryset_to_csv, export_queryset_to_excel


class ExportMixin:
    @action(detail=False, methods=['get'], url_path='export')
    def export(self, request):
        format_type = request.query_params.get('format', 'csv').lower()

        queryset = self.filter_queryset(self.get_queryset())
        model_name = self.queryset.model.__name__

        if format_type == 'excel':
            return export_queryset_to_excel(queryset, model_name)
        elif format_type == 'csv':
            return export_queryset_to_csv(queryset, model_name)
        else:
            return Response(
                {
                    'success': False,
                    'message': 'Formato no válido. Use ?format=csv o ?format=excel',
                    'data': None
                },
                status=status.HTTP_400_BAD_REQUEST
            )
