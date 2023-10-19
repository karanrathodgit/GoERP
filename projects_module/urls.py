from django.urls import path 
from . import views

app_name = 'projects_module'

urlpatterns = [
  path('registration/',views.registration_view,name='registration'),
  path('editanddelete/',views.editanddelete_view,name='editanddelete'),
  path('edit_view/<int:id>',views.edit_view,name='edit_view'),
  path('delete_view/<int:id>',views.delete_view,name='delete_view'),
  
]