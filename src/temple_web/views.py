from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpRequest, JsonResponse
from django.db import connections
from django.db.utils import OperationalError


def health_check(request: HttpRequest):
    # Check database connection
    try:
        db_conn = connections['default']
        db_conn.cursor()
        db_status = True
    except OperationalError:
        db_status = False

    status = 200 if db_status else 503
    response_data = {
        'status': 'healthy' if db_status else 'unhealthy',
        'database': 'up' if db_status else 'down'
    }
    return JsonResponse(response_data, status=status)


def page_not_found_view(request: HttpRequest, exception):
    # print("hello", request.get_full_path())
    return render(request, "404.html", {}, status=404)
