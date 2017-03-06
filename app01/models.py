from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class userpro(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(u'姓名', max_length=30)

    def __unicode__(self):
        return self.name


class The_number_of_clicks(models.Model):
    province_name = models.CharField(max_length=100)
    number = models.FloatField()
    updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}-{}-{}".format(self.province_name, self.updatetime, self.number)


class source_ip(models.Model):
    province_name = models.CharField(max_length=100)
    number = models.FloatField()
    updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}-{}-{}".format(self.province_name, self.updatetime, self.number)


class Business_daily_traffic(models.Model):
    Business_name = models.CharField(max_length=100)
    traffic = models.FloatField()
    updatetime = models.DateTimeField(auto_now=True)
    date = models.CharField(max_length=100)

    def __str__(self):
        return "{}-{}-{}".format(self.Business_name, self.traffic, self.date)


class real(models.Model):
    rmb = models.FloatField()
    numner = models.IntegerField()
    time = models.CharField(max_length=100)
    updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.rmb, self.numner, self.time, self.updatetime)


class Commodity_categories(models.Model):
    categories_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    categoriesId = models.IntegerField(null=True)

    def __str__(self):
        return "{}-{}".format(self.categories_id, self.name)


class Commodity_subclass(models.Model):
    Commodity_categories = models.ForeignKey(Commodity_categories)
    name = models.CharField(max_length=100)
    total_rmb = models.FloatField()

    def __str__(self):
        return "{}-{}-{}".format(self.Commodity_categories, self.name, self.total_rmb)


class City_trading_volume(models.Model):
    city_name = models.CharField(max_length=100)
    city_rmb = models.FloatField()
    updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}-{}-()".format(self.city_name, self.city_rmb, self.updatetime)


class categories(models.Model):
    categoriesId = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    total_rmb = models.FloatField(null=True)

    def __str__(self):
        return self.name


class subclass(models.Model):
    total_rmb = models.FloatField(null=True)
    name = models.CharField(max_length=100, null=True)

    categoriesId = models.IntegerField(null=True)
    categoriesName = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class provinces_rmb(models.Model):
    name = models.CharField(max_length=100)
    rmb = models.FloatField()
    updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class business_real_time_access(models.Model):
    business_name=models.CharField(max_length=100)
    access_count=models.IntegerField()
    time=models.CharField(max_length=100)
    updatetime=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name


