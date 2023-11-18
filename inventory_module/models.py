from django.db import models

# Create your models here.

class Resource_Model(models.Model):
  plates = models.IntegerField()
  pipes = models.IntegerField()
  rod = models.IntegerField()
  
  