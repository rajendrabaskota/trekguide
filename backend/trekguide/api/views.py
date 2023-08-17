from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


class AllDestinations(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestinationTitle(APIView):
    serializer_class = DestinationSerializer

    def get(self, request, format=None):
        destinations = Destination.objects.all()
        titles = []
        for destination in destinations:
            titles.append(destination.dest_name)
        return JsonResponse(titles, safe=False, status=status.HTTP_200_OK)

class GetDestination(APIView):
    serializer_class = DestinationSerializer
    lookup_url_kwarg = 'dest_name'

    def get(self, request, format=None):
        dest_name = request.GET.get(self.lookup_url_kwarg)
        if dest_name != None:
            destination = Destination.objects.filter(dest_name=dest_name)
            data = DestinationSerializer(destination[0]).data

            return Response(data, status=status.HTTP_200_OK)
        return Response({'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


#OLD AND WORKING
# class RouteInfo(APIView):
#     lookup_url_kwarg = 'dest_id'

#     def get(self, request, format=None):
#         dest_id = request.GET.get(self.lookup_url_kwarg)
#         if dest_id != None:
#             routes = DestinationRoute.objects.filter(dest=dest_id)
#             data = []
            
#             for route in routes:
#                 route_id = route.route_id
#                 route_name = route.route_name
#                 route_description = route.route_description
#                 route_pic = route.route_pic

#                 objects_cities = Route.objects.raw('''
#                     select route_id, city_name
#                     from destination_route natural join destination natural join route natural join city
#                     where dest_id='%s' and route_id='%s'
#                 ''' %(dest_id, route_id))

#                 cities = [object.city_name for object in objects_cities]

#                 objects_packages = Route.objects.raw('''
#                     select route_id, guide_name, phone_number, price, days, package_name, package_description
#                     from guide natural join packages
#                     where route_id='%s'
#                 ''' %(route_id))

#                 packages = []
#                 for object in objects_packages:
#                     package_info = {
#                         'package_name': object.package_name,
#                         'package_description': object.package_description,
#                         'price': object.price,
#                         'days': object.days,
#                         'guide_name': object.guide_name,
#                         'phone_number': object.phone_number,
#                     }
#                     packages.append(package_info)

#                 temp = {
#                     'route_name': route_name,
#                     'route_description': route_description,
#                     'route_pic': route_pic,
#                     'cities': cities,
#                     'packages': packages
#                 }

#                 data.append(temp)

#             return JsonResponse(data, safe=False, status=status.HTTP_200_OK)




class RouteInfo(APIView):
    lookup_url_kwarg = 'dest_name'

    def get(self, request, format=None):
        dest_name = request.GET.get(self.lookup_url_kwarg)
        if dest_name != None:
            queryset = Destination.objects.filter(dest_name=dest_name)[0]
            dest_id = queryset.dest_id
        if dest_id != None:
            routes = DestinationRoute.objects.filter(dest=dest_id)
            data = []
            
            for route in routes:
                route_id = route.route_id
                route_name = route.route_name
                route_description = route.route_description
                route_pic = route.route_pic

                objects_cities = Route.objects.raw('''
                    select route_id, city_name, city_description
                    from destination_route natural join destination natural join route natural join city
                    where dest_id='%s' and route_id='%s'
                ''' %(dest_id, route_id))

                cities = []

                for city_obj in objects_cities:
                    city_info = {}
                    city = city_obj.city_name
                    city_description = city_obj.city_description

                    objects_viewpoint = City.objects.raw('''
                        select city_id, city_name, viewpoint_name, viewpoint_details
                        from city natural join city_viewpoint
                        where city_name='%s'
                    ''' %(city))

                    city_viewpoint = []
                    for object in objects_viewpoint:
                        temp = {
                            "viewpoint_name": object.viewpoint_name,
                            "viewpoint_description": object.viewpoint_details,
                        }
                        city_viewpoint.append(temp)

                    objects_accomodation = City.objects.raw('''
                        select city_id, city_name, hotel_name, phone_number, email, price
                        from city natural join accomodation
                        where city_name='%s'
                    ''' %(city))

                    city_accomodation = []
                    for object in objects_accomodation:
                        temp = {
                            "hotel_name": object.hotel_name,
                            "phone_number": object.phone_number,
                            "email": object.email,
                            "price": object.price
                        }
                        city_accomodation.append(temp)

                    city_info = {
                        "city_name": city,
                        "city_description": city_description,
                        "city_viewpoint": city_viewpoint,
                        "accomodation": city_accomodation
                    }

                    cities.append(city_info)


                objects_packages = Route.objects.raw('''
                    select route_id, guide_name, phone_number, price, days, package_id, package_name, package_description
                    from guide natural join packages
                    where route_id='%s'
                ''' %(route_id))

                packages = []
                for object in objects_packages:
                    package_info = {
                        'package_name': object.package_name,
                        'price': object.price,
                        'days': object.days,
                        'guide_name': object.guide_name,
                        'phone_number': object.phone_number,
                    }

                    package_details = PackageDetails.objects.raw('''
                        select package_id, package_description
                        from package_details
                        where package_id='%s'
                    ''' %(object.package_id))

                    description_temp = [package_detail.package_description for package_detail in package_details]
                    package_info['package_description'] = description_temp
                    packages.append(package_info)

                temp = {
                    'route_name': route_name,
                    'route_description': route_description,
                    'route_pic': route_pic,
                    'city': cities,
                    'packages': packages
                }

                data.append(temp)

            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)



# class RouteCities(APIView):
#     lookup_url_kwarg = 'dest_id'

#     def get(self, request, format=None):
#         dest_id = request.GET.get(self.lookup_url_kwarg)
#         if dest_id != None:
#             routes = DestinationRoute.objects.filter(dest=dest_id)
#             data = []
            
#             for route in routes:
#                 route_id = route.route_id
#                 route_name = route.route_name
#                 route_description = route.route_description
#                 route_pic = route.route_pic

#                 objects_cities = Route.objects.raw('''
#                     select route_id, city_name, city_description
#                     from destination_route natural join destination natural join route natural join city
#                     where dest_id='%s' and route_id='%s'
#                 ''' %(dest_id, route_id))

#                 for object in objects_cities:
#                     city_name = object.city_name
#                     city_description = object.city_description
                    





#                 print("cities")
#                 print(cities)

#                 objects_packages = Route.objects.raw('''
#                     select route_id, guide_name, phone_number, price, days, package_name, package_description
#                     from guide natural join packages
#                     where route_id='%s'
#                 ''' %(route_id))

#                 packages = []
#                 for object in objects_packages:
#                     package_info = {
#                         'package_name': object.package_name,
#                         'package_description': object.package_description,
#                         'price': object.price,
#                         'days': object.days,
#                         'guide_name': object.guide_name,
#                         'phone_number': object.phone_number,
#                     }
#                     packages.append(package_info)

#                 temp = {
#                     'route_name': route_name,
#                     'route_description': route_description,
#                     'route_pic': route_pic,
#                     'cities': cities,
#                     'packages': packages
#                 }

#                 data.append(temp)

#             return JsonResponse(data, safe=False, status=status.HTTP_200_OK)












# class RoutePackages(APIView):
#     lookup_url_kwarg = 'route_id'

#     def get(self, request , format=None):
#         route_id = request.GET.get(self.lookup_url_kwarg)
#         if route_id != None:
#             objects = Route.objects.raw('''
#                 select route_id, guide_name, phone_number, price, days
#                 from guide natural join packages
#                 where route_id='%s'
#             ''' %(route_id))
#             data = {}
#             data['packages'] = []

#             for object in objects:
#                 temp = [object.days, object.price, object.guide_name, object.phone_number]
#                 data['packages'].append(temp)

#             return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
#         return Response({'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class RoutePackages(APIView):
    lookup_url_kwarg = 'route_id'

    def get(self, request , format=None):
        route_id = request.GET.get(self.lookup_url_kwarg)
        if route_id != None:
            objects = Route.objects.raw('''
                select route_id, guide_name, phone_number, price, days, package_name, package_description
                from guide natural join packages
                where route_id='%s'
            ''' %(route_id))
            data = []
            # data['packages'] = []

            for object in objects:
                temp = {
                    'package_name': object.package_name,
                    'package_description': object.package_description,
                    'price': object.price,
                    'days': object.days,
                    'guide_name': object.guide_name,
                    'phone_number': object.phone_number,
                }
                data.append(temp)

            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
        return Response({'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

# OLD AND RUNNING
# class ViewpointAccomodation(APIView):
#     lookup_url_kwarg = 'dest_id'

#     def get(self, request, format=None):
#         dest_id = request.GET.get(self.lookup_url_kwarg)
#         if dest_id != None:
#             cities = City.objects.raw('''
#                 select distinct city_id, city_name from
#                 destination_route natural join route natural join city
#                 where dest_id='%s'
#             ''' %(dest_id))
#             data = {}

#             for city_obj in cities:
#                 city = city_obj.city_name

#                 objects_viewpoint = City.objects.raw('''
#                     select city_id, city_name, viewpoint_name
#                     from city natural join city_viewpoint
#                     where city_name='%s'
#                 ''' %(city))
#                 temp_viewpoint = [object.viewpoint_name for object in objects_viewpoint]

#                 objects_accomodation = City.objects.raw('''
#                     select city_id, city_name, hotel_name, phone_number, email, price
#                     from city natural join accomodation
#                     where city_name='%s'
#                 ''' %(city))
#                 temp_accomodation = [[object.hotel_name, object.phone_number, object.email, object.price] for object in objects_accomodation]

#                 data[city] = {
#                     "viewpoint": temp_viewpoint,
#                     "accomodation": temp_accomodation,
#                 }

#             return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

#         return Response({'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class CityInfo(APIView):
    lookup_url_kwarg = 'dest_id'

    def get(self, request, format=None):
        dest_id = request.GET.get(self.lookup_url_kwarg)
        if dest_id != None:
            cities = City.objects.raw('''
                select distinct city_id, city_name, city_description from
                destination_route natural join route natural join city
                where dest_id='%s'
            ''' %(dest_id))
            data = {}

            for city_obj in cities:
                city_info = {}
                city = city_obj.city_name
                city_description = city_obj.city_description

                objects_viewpoint = City.objects.raw('''
                    select city_id, city_name, viewpoint_name, viewpoint_details
                    from city natural join city_viewpoint
                    where city_name='%s'
                ''' %(city))

                city_viewpoint = []
                for object in objects_viewpoint:
                    temp = {
                        "viewpoint_name": object.viewpoint_name,
                        "viewpoint_description": object.viewpoint_details,
                    }
                    city_viewpoint.append(temp)

                objects_accomodation = City.objects.raw('''
                    select city_id, city_name, hotel_name, phone_number, email, price
                    from city natural join accomodation
                    where city_name='%s'
                ''' %(city))

                city_accomodation = []
                for object in objects_accomodation:
                    temp = {
                        "hotel_name": object.hotel_name,
                        "phone_number": object.phone_number,
                        "email": object.email,
                        "price": object.price
                    }
                    city_accomodation.append(temp)

                city_info = {
                    "city_name": city,
                    "city_description": city_description,
                    "city_viewpoint": city_viewpoint,
                    "accomodation": city_accomodation
                }

                data[city] = city_info

            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

        return Response({'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)



class DestinationSeason(APIView):
    lookup_url_kwarg = 'dest_name'

    def get(self, request, format=None):
        dest_name = request.GET.get(self.lookup_url_kwarg)
        if dest_name != None:
            objects = Season.objects.raw('''
                select dest_id, dest_name, month_name
                from season natural join months
                natural join destination
                where dest_name='%s'
            ''' %(dest_name))
            data = {}
            data['months'] = []

            for object in objects:
                data['months'].append(object.month_name)

            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

        return Response({'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


# class Transportation(APIView):
#     lookup_url_kwarg = 'dest_name'

#     def get(self, request, format=None):
#         dest_name = request.GET.get(self.lookup_url_kwarg)
#         if dest_name != None:
            

        