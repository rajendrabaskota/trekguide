from rest_framework import serializers
from .models import *


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class DSerializer(serializers.ModelSerializer):
    class Meta:
        model = D
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class DestinationRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationRoute
        fields = '__all__'


class CityViewpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityViewpoint
        fields = '__all__'


class AccomodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accomodation
        fields = '__all__'


# class TransportMediumSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TransportMedium
#         fields = '__all__'


# class TransportationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transportation
#         fields = '__all__'


class MonthsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Months
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'


class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = '__all__'
