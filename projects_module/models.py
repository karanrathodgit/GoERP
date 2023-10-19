from django.db import models

# Create your models here.

class RegistrationModel(models.Model):
  
  project_name = models.CharField(max_length=150,null=False,blank=False)
  project_date = models.DateField()
  PO_number = models.IntegerField()
  client_name = models.CharField(max_length=200,null=False,blank=False)
  wo_number = models.CharField(max_length=50,null=False,blank=False)
  projected_cost = models.IntegerField()
  cdd = models.DateField()

  def __str__(self):
    return self.project_name