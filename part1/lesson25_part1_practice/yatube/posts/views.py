from django.http import JsonResponse

from .models import Post


def index(request):
    post_list = Post.objects.all()

    response = []
    for post in post_list:
        response.append({
            "id": post.id,
            "slug": post.slug,
            "text": post.text,
            "pub_date": post.pub_date,
            "author": post.author,
            "group": post.group,
        })

    return JsonResponse(response, safe=False)


def get_post(request, slug):
    post = Post.objects.get(slug=slug)

    return JsonResponse({
        "id": post.id,
        "slug": post.slug,
        "text": post.text,
        "pub_date": post.pub_date,
        "author": post.author,
        "group": post.group,
    })


def posts(request):
    if request.method == "GET":
        posts = Post.objects.all()

        search_text = request.GET.get("search_text", None)
        if search_text:
            posts = posts.filter(author=search_text)

        response = []
        for post in posts:
            response.append({
                "id": post.id,
                "slug": post.slug,
                "text": post.text,
                "pub_date": post.pub_date,
                "author": post.author,
                "group": post.group,
            })

        return JsonResponse(response, safe=False)
