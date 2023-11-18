from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileModel(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  image = models.ImageField(default='profilepic.jpeg',upload_to='profile_pictures')
  city = models.CharField(max_length=150)
  date_of_joining = models.DateField()
  date_of_birth = models.DateField()

  def __str__(self):
    return self.user.username