from django.shortcuts import render
from .forms import ResourceForm
from .models import Resource_Model
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def resource_view(request):
  
  if request.method == 'POST':
    plates = request.POST['plates']
    pipes = request.POST['pipes']
    rod = request.POST['rod']

    data = Resource_Model(plates=plates,pipes=pipes,rod=rod)
    data.save()

  form = ResourceForm()
  return render(request,'inventory_module/resource_view.html',context={'form':form})