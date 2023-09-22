from django.db import models

# Create your models here.

class store_status(models.Model):
    store_id = models.IntegerField()
    timestamp_utc = models.TextField()
    status = models.CharField(max_length=10)

class business_hours(models.Model):
    store_id = models.IntegerField()
    day_of_week = models.IntegerField()
    start_time_local = models.DateTimeField()
    end_time_local = models.DateTimeField()

class store_timezone(models.Model):
    store_id = models.IntegerField()
    timezone_str = models.CharField(max_length=100)

