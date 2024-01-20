from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    content = models.CharField(max_length=255)
