from django.http import JsonResponse

from lostfound.models import *

def android(request):
    data = {
        "items": [
            {
                "name": "shirt",
                "description": "just a shirt",
                "date": "1/1/2020",
                "category": "apparel",
            },
            {
                "name": "credit card",
                "description": "a black card",
                "date": "2/2/2020",
                "category": "finance",
            },
        ]
    }
    
    for item in Item.objects.all():
        data["items"].append({
            "name": f"{item.itemName}",
            "description": f"{item.description}",
            "date": f"{item.dateReported}",
            "category": f"{item.category}"
        })
        print(f"{item}")

    return JsonResponse(data)
