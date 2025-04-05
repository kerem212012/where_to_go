from audioop import reverse

from django.http import HttpResponse
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
                "detailsUrl": "" #reverse('place_details', kwargs={'place_id': place.id})
            }
        }
        )
    context = {
        "geo_json": geo,
    }
    return render(request, 'index.html', context=context)

def get_place_details(request,place_id):
    place = get_object_or_404(Place,pk=place_id)
    return HttpResponse(place.title)
