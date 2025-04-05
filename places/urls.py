from django.urls import path

from places import views

urlpatterns = [
    path('', views.index, name='index'),
    path('places/<int:place_id>', views.get_place_details, name='place_details'),
]
