from django.urls import path
from . import views

app_name = 'design_module'

urlpatterns = [
  path('design_home/',views.design_home_view,name='design_home')
]