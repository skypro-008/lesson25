from django.http import JsonResponse

from core.models import Issue, Statistic


def issues(request):
    issues_list = Issue.objects.all()

    response = []
    for issue in issues_list:
        response.append({
            "uid": issue.uid,
            "author": issue.author,
            "timestamp": issue.timestamp,
            "text": issue.text,
            "photos": issue.photos,
        })

    return JsonResponse(response, safe=False)


def statistics(request):
    # TODO: допиши здесь ручку, которая отдает нужные значения
    pass