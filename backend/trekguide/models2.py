# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accomodation(models.Model):
    acc_id = models.AutoField(primary_key=True)
    city_id = models.IntegerField()
    hotel_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accomodation'


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=30)
    city_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class CityViewpoint(models.Model):
    cvp_id = models.AutoField(primary_key=True)
    viewpoint_name = models.CharField(max_length=30)
    city = models.ForeignKey(City, models.DO_NOTHING)
    viewpoint_details = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city_viewpoint'


class Destination(models.Model):
    dest_id = models.AutoField(primary_key=True)
    dest_name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True, null=True)
    image_link = models.CharField(max_length=255, blank=True, null=True)
    max_elevation = models.CharField(max_length=255, blank=True, null=True)
    min_duration = models.CharField(max_length=30, blank=True, null=True)
    difficulty = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'destination'


class DestinationRoute(models.Model):
    dest = models.ForeignKey(Destination, models.DO_NOTHING)
    route = models.OneToOneField('Route', models.DO_NOTHING, primary_key=True)
    route_name = models.CharField(max_length=30, blank=True, null=True)
    route_description = models.CharField(max_length=255, blank=True, null=True)
    route_pic = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'destination_route'
        unique_together = (('route', 'dest'),)


class Guide(models.Model):
    guide_id = models.AutoField(primary_key=True)
    guide_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guide'


class Months(models.Model):
    month_id = models.AutoField(primary_key=True)
    month_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'months'


class PackageDetails(models.Model):
    package = models.OneToOneField('Packages', models.DO_NOTHING, primary_key=True)
    package_description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'package_details'
        unique_together = (('package', 'package_description'),)


class Packages(models.Model):
    package_id = models.AutoField(primary_key=True)
    price = models.FloatField(blank=True, null=True)
    days = models.IntegerField()
    guide = models.ForeignKey(Guide, models.DO_NOTHING)
    route = models.ForeignKey('Route', models.DO_NOTHING)
    package_name = models.CharField(max_length=30, blank=True, null=True)
    package_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packages'


class Route(models.Model):
    route_id = models.IntegerField(primary_key=True)
    city = models.ForeignKey(City, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'route'
        unique_together = (('route_id', 'city'),)


class Season(models.Model):
    dest = models.OneToOneField(Destination, models.DO_NOTHING, primary_key=True)
    month = models.ForeignKey(Months, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'season'
        unique_together = (('dest', 'month'),)


class TransportMedium(models.Model):
    transport_medium_id = models.AutoField(primary_key=True)
    transport_medium_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'transport_medium'


class Transportation(models.Model):
    transport_medium = models.ForeignKey(TransportMedium, models.DO_NOTHING)
    city_id_origin = models.ForeignKey(City, models.DO_NOTHING, db_column='city_id_origin')
    city_id_destination = models.ForeignKey(City, models.DO_NOTHING, db_column='city_id_destination')
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transportation'
