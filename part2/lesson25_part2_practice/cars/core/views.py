from django.http import JsonResponse

from core.models import Car


# TODO: перепиши меня
def car(request, id):
    try:
        car = Car.objects.get(id=id)
    except Car.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)

    return JsonResponse({
        "id": car.id,
        "slug": car.slug,
        "name": car.name,
        "brand": car.brand,
        "address": car.address,
        "description": car.description,
        "status": car.status,
        "created": car.created,
    })
