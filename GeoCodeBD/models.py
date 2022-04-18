from django.db import models


# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=50)
    name_bn = models.CharField(max_length=50)
    url = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=50)
    name_bn = models.CharField(max_length=50)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    url = models.CharField(max_length=50, null=True, blank=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Upazila(models.Model):
    name = models.CharField(max_length=50)
    name_bn = models.CharField(max_length=50)
    url = models.CharField(max_length=50, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Union(models.Model):
    name = models.CharField(max_length=50)
    name_bn = models.CharField(max_length=50)
    code = models.CharField(max_length=10, blank=True, null=True)
    url = models.CharField(max_length=50, null=True, blank=True)
    upazila = models.ForeignKey(Upazila, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name
