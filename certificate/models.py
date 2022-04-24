from django.db import models


# Create your models here.

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    name_bn = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
