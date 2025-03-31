from django.http import JsonResponse

from lostfound.models import *

def android(request):
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
    
    for item in Item.objects.all():
        data["items"].append({
            "name": f"{item.itemName}",
            "description": f"{item.description}",
            "date": f"{item.dateReported}",
            "category": f"{item.category}",
            "photo": f"{item.photo}",
        })

    return JsonResponse(data)

def androidUpload(request):
    return HttpResponse()
