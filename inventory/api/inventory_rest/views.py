import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from common.json import ModelEncoder

from .models import Pellets


class PelletsEncoder(ModelEncoder):
    model = Pellets
    properties = [
        "item_number",
        "name",
        "unit_price",
        "stock",
    ]


@require_http_methods(["GET", "POST"])
def api_list_pellets(request):
    if request.method == "GET":
        pellets = Pellets.objects.all()
        return JsonResponse(
            {"pellets": pellets},
            encoder=PelletsEncoder,
        )
    else:
        content = json.loads(request.body)
        pellet = Pellets.objects.create(**content)
        return JsonResponse(
            pellet,
            encoder=PelletsEncoder,
            safe=False,
        )


@require_http_methods(["GET", "DELETE", "PUT"])
def api_show_pellet(request, pk):
    if request.method == "GET":
        try:
            pellet = Pellets.objects.get(item_number=pk)
            return JsonResponse(
                pellet,
                encoder=PelletsEncoder,
                safe=False
            )
        except Pellets.DoesNotExist:
            response = JsonResponse(
                {"message": "Product does not exist"}
            )
            response.status_code = 404
            return response

    if request.method == "DELETE":
        try:
            pellet = Pellets.objects.get(item_number=pk)
            pellet.delete()
            return JsonResponse(
                pellet,
                encoder=PelletsEncoder,
                safe=False,
            )
        except Pellets.DoesNotExist:
            response = JsonResponse(
                {"message": "Product does not exist"}
            )
            response.status_code = 404
            return response

    else:
        try:
            content = json.loads(request.body)
            pellet = Pellets.objects.get(item_number=pk)

            props = [
                "unit_price",
                "stock",
            ]
            for prop in props:
                if prop in content:
                    setattr(pellet, prop, content[prop])
            pellet.save()

            return JsonResponse(
                pellet,
                encoder=PelletsEncoder,
                safe=False,
            )
        except Pellets.DoesNotExist:
            response = JsonResponse(
                {"message": "Product does not exist"}
            )
            response.status_code = 404
            return response
