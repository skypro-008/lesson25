from django.http import JsonResponse
from django.shortcuts import render

from course.models import Course


def courses(request):
    courses_list = Course.objects.all()

    response = []
    for course in courses_list:
        response.append({
            "id": course.id,
            "slug": course.slug,
            "author": course.author,
            "description": course.description,
            "start_day": course.start_day,
            "status": course.status,
            "created": course.created,
        })

    return JsonResponse(response, safe=False)


def new_courses(request):
    courses_list = Course.objects.filter(status="new")

    response = []
    for course in courses_list:
        response.append({
            "id": course.id,
            "slug": course.slug,
            "author": course.author
        })

    return JsonResponse(response, safe=False)


def get_course(request, course_slug):
    try:
        course = Course.objects.get(slug=course_slug)
    except Course.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)

    return JsonResponse({
        "id": course.id,
        "slug": course.slug,
        "author": course.author,
        "description": course.description,
        "start_day": course.start_day,
        "status": course.status,
        "created": course.created,
    })


def search(request):
    courses = Course.objects.all()

    search_text = request.GET.get("author", None)
    if search_text:
        courses = courses.filter(author=search_text)

    response = []
    for course in courses:
        response.append({
            "id": course.id,
            "text": course.text,
        })

    return JsonResponse(response, safe=False)
