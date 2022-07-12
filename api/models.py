from operator import mod
from django.db import models

class Recipes(models.Model):
    name = models.CharField(max_length = 100)
    ingredients= models.CharField(max_length = 1000)
    directions = models.CharField(max_length = 1000)
    last_modified = models.DateField(auto_now=True)

    def __str___(self):
        return self.name