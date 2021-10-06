from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import JVDjangoDBModel

from app_api_jv.problem_domain import databaseMapper

def get_current_state(request, id_user):
    register, _ = JVDjangoDBModel.objects.get_or_create(pk=id_user)
    mapper = databaseMapper.DatabaseMapper(register)
    if request.method == "GET":
        response_data = mapper.getState()
    elif request.method == "POST":
        a_line = int(request.POST["line"])
        a_column = int(request.POST["column"])
        response_data = mapper.click_position(a_line, a_column)
    return JsonResponse(response_data, safe=False)
    