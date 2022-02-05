from django.db import models


class Category(models.Model):
    """
    name: str - required
    description: str
    """
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=10000, null=True)
