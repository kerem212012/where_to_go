from audioop import reverse

from django.shortcuts import render

from places.models import Place

def start_page(request):
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
