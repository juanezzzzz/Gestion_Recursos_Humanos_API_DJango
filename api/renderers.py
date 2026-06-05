from rest_framework.renderers import JSONRenderer


class StandardJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context['response']

        success = response.status_code < 400
        message = ""

        if success:
            if response.status_code == 201:
                message = "Recurso creado exitosamente"
            elif response.status_code == 204:
                message = "Recurso eliminado exitosamente"
            else:
                message = "Solicitud exitosa"
        else:
            if isinstance(data, dict):
                message = str(data.get('detail', 'Error en la solicitud'))
            else:
                message = "Error en la solicitud"

        formatted_data = {
            "success": success,
            "message": message,
            "data": data if success else None
        }

        return super().render(formatted_data, accepted_media_type, renderer_context)
