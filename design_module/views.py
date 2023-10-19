from django.shortcuts import render

# Create your views here.

def design_home_view(request):

  return render(request,'design_module/design_home.html')