from django.http import JsonResponse

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
    # TODO: эта вью отвечает по GET /course/new и возвравщает список курсов со status=new, но только поля id, slug, author


def get_course(request, course_slug):
    # TODO: эта вью отвечаает по GET /course/:slug и возвращает карточку курса (все поля) по переданному ей slug


def search(request):
    # TODO: эта вью отвечает по GET /course/search и принимает QUERY параметр author. По этому параметру она ищет курсы и возвращает список подошедших (все поля)

