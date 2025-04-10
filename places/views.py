from django.urls import reverse

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from places.models import Place

def index(request):
    places = Place.objects.all()
    geo = {
        "type": "FeatureCollection",
        "features": []
    }
    for place in places:
        geo["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('place_details', kwargs={'place_id': place.id})
            }
        }
        )
    context = {
        "geo_json": geo,
    }
    return render(request, 'index.html', context=context)

def get_place_details(request,place_id):
    place = get_object_or_404(Place,pk=place_id)
    place_details = {
        "title" : place.title,
        "imgs" : [image.image.url for image in place.images.all()],
        "description_short" : place.description_short,
        "description_long" : place.description_long,
        "coordinates" : {
            "lng": place.lng,
            "lat" : place.lat,
        }
    }
    return JsonResponse(place_details,json_dumps_params={'ensure_ascii': False, 'indent': 4})
