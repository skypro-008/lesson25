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
    statistic_list = Statistic.objects.all()

    response = []
    for statistic in statistic_list:
        response.append({
            "id": statistic.id,
            "day": statistic.day,
            "store": statistic.store,
            "reason": statistic.reason,
            "status": statistic.status,
        })

    return JsonResponse(response, safe=False)
