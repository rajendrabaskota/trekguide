from django.urls import path
from .views import AllDestinations, GetDestination, DestinationSeason, RoutePackages, RouteInfo, CityInfo, DestinationTitle

urlpatterns = [
    path('all/', AllDestinations.as_view()),
    path('destination/', GetDestination.as_view()),
    path('destination-season/', DestinationSeason.as_view()),
    path('route-packages/', RoutePackages.as_view()),
    path('route-info/', RouteInfo.as_view()),
    path('city-info/', CityInfo.as_view()),
    path('destination-title/', DestinationTitle.as_view()),
]
