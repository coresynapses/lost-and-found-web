from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from lostfound.models import *

data = {
    "items": [
        {
            "name": "shirt",
            "status": "lost",
            "description": "just a shirt",
            "date": "1/1/1010",
            "category": "Apparel",
            "photo": "photo1",
        },
        {
            "name": "credit card",
            "status": "found",
            "description": "a black card",
            "date": "2/2/2020",
            "category": "Finance",
            "photo": "photo2",
        },
    ]
}

def android(request):
    for item in Item.objects.all():
        data["items"].append({
            "name": f"{item.itemName}",
            "description": f"{item.description}",
            "date": f"{item.dateReported}",
            "category": f"{item.category}",
            "photo": f"{item.photo}",
        })

    return JsonResponse(data)

@csrf_exempt # Remove from production
def androidUpload(request):
    if request.method == "POST":
        body = request.body.decode("utf-8").split("$")
        print(body)
        data["items"].append({
            "name": body[0],
            "date": body[1],
            "category": body[2],
        })
        return HttpResponse(body)
    else:
        return HttpResponse("nihao")


@csrf_exempt # Remove from production
def androidClaim(request):
    if request.method == "POST":
        body = request.body.decode("utf-8").split("$")
        print(body)
        # data["items"].append({
        #     "name": body[0],
        #     "date": body[1],
        #     "category": body[2],
        # })
        return HttpResponse(body)
    else:
        return HttpResponse("nihao")


@csrf_exempt # Remove from production
def androidReport(request):
    if request.method == "POST":
        body = request.body.decode("utf-8").split("$")
        print(body)
        # data["items"].append({
        #     "name": body[0],
        #     "date": body[1],
        #     "category": body[2],
        # })
        return HttpResponse(body)
    else:
        return HttpResponse("nihao")
