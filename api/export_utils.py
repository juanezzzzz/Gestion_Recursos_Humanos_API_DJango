import csv
from io import BytesIO, StringIO
from django.http import HttpResponse, StreamingHttpResponse
from openpyxl import Workbook


def export_queryset_to_csv(queryset, model_name):
    output = StringIO()
    writer = csv.writer(output)

    if not queryset.exists():
        return None

    model = queryset.model
    fields = [f.name for f in model._meta.get_fields() if not f.many_to_one or f.many_to_one]

    writer.writerow(fields)

    for obj in queryset:
        row = [getattr(obj, field, '') for field in fields]
        writer.writerow(row)

    response = HttpResponse(output.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{model_name}.csv"'
    return response


def export_queryset_to_excel(queryset, model_name):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = model_name[:31]

    if not queryset.exists():
        return None

    model = queryset.model
    fields = [f.name for f in model._meta.get_fields() if not f.many_to_one or f.many_to_one]

    worksheet.append(fields)

    for obj in queryset:
        row = [str(getattr(obj, field, '')) for field in fields]
        worksheet.append(row)

    output = BytesIO()
    workbook.save(output)
    output.seek(0)

    response = HttpResponse(
        output.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename="{model_name}.xlsx"'
    return response
