from django.http import JsonResponse

from core.models import Car


def cars(request):
    cars_list = Car.objects.all()

    response = []
    for car in cars_list:
        response.append({
            "id": car.id,
            "slug": car.slug,
            "name": car.name,
            "brand": car.brand,
            "address": car.address,
            "description": car.description,
            "status": car.status,
            "created": car.created,
        })

    return JsonResponse(response, safe=False)


def search(request):
    cars_list = Car.objects.all()

    search_text = request.GET.get("brand", None)
    if search_text:
        cars_list = cars_list.filter(brand=search_text)

    response = []
    for car in cars_list:
        response.append({
            "id": car.id,
            "name": car.name,
            "brand": car.brand,
            "status": car.status,
        })

    return JsonResponse(response, safe=False)


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
