from django.db import models
from django.utils.translation import gettext_lazy as _

class Documents(models.Model):
    name=models.CharField(max_length=120,verbose_name=_('name'))
    notes=models.TextField(max_length=1500)

    def __str__(self):
        return self.name

class Sectors(models.Model):
    name=models.CharField(max_length=120)
    code=models.CharField(max_length=75,default='')

    def __str__(self):
        return self.name