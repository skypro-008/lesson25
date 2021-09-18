from django.db import models


class Destination(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    to_name = models.CharField(max_length=100, null=True, blank=True)
    flag = models.CharField(max_length=10, null=True, blank=True)
    visa_id = models.PositiveSmallIntegerField(null=True, blank=True)
    covid_status = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name