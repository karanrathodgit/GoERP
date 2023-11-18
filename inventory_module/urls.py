from django.urls import path
from . import views

app_name = 'inventory_module'

urlpatterns = [
  path('resource_view/',views.resource_view,name='resource_view'),
]