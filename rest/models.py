from django.db import models


class RestCat(models.Model):
    title = models.CharField(max_length=100)
