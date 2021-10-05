from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import JVDjangoDBModel

from app_api_jv.problem_domain import databaseMapper

def refresh(request, id_user):
    register = JVDjangoDBModel(id_user)

    if request.method == "GET":
        try:
            register = JVDjangoDBModel.objects.get(pk=id_user)
        except:
            register.save()
        finally:
            mapper = databaseMapper.DatabaseMapper(register)
            response_data = mapper.getState()
            return JsonResponse(response_data, safe=False)
    elif request.method == "POST":
        print(request.POST)
        col = request.POST["col"]
        line = request.POST["line"]
        return JsonResponse(request.POST, safe=False)


def click(request, id_user, line, column):
    register = JVDjangoDBModel(id_user)
    try:
        register = JVDjangoDBModel.objects.get(pk=id_user)
    except:
        register.save()
    finally:
        mapper = databaseMapper.DatabaseMapper(register)
        response_data = mapper.click_position(line, column)
        return JsonResponse(response_data, safe=False)
