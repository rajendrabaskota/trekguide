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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True, null=True)

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


class D(models.Model):
    did = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=20, blank=True, null=True)
    tempfield = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd'


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Guide(models.Model):
    guide_id = models.AutoField(primary_key=True)
    guide_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guide'


class M(models.Model):
    mid = models.IntegerField(primary_key=True)
    mname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm'


class Months(models.Model):
    month_id = models.AutoField(primary_key=True)
    month_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'months'


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


class PackageDetails(models.Model):
    package = models.OneToOneField('Packages', models.DO_NOTHING, primary_key=True)
    package_description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'package_details'
        unique_together = (('package', 'package_description'),)


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
    city_id_origin = models.ForeignKey(City, models.DO_NOTHING, db_column='city_id_origin', related_name='city_origin')
    city_id_destination = models.ForeignKey(City, models.DO_NOTHING, db_column='city_id_destination')
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transportation'
