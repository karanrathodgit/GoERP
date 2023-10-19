from django.shortcuts import render
from projects_module.models import RegistrationModel

# Create your views here.

def dashboard_view(request):

  project_number = RegistrationModel.objects.all().count()

  context = {'project_number':project_number}
  
  return render(request,'home/dashboard.html',context)