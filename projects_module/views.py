from django.shortcuts import render,redirect
from .models import RegistrationModel
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def registration_view(request):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        project_date = request.POST['project_date']
        PO_number = request.POST['PO_number']
        client_name = request.POST['client_name']
        wo_number = request.POST['wo_number']
        projected_cost = request.POST['projected_cost']
        cdd = request.POST['cdd']

        new_project = RegistrationModel(project_name=project_name,project_date=project_date,PO_number=PO_number,client_name=client_name,wo_number=wo_number,projected_cost=projected_cost,cdd=cdd)

        new_project.save()

    context = {}
    return render(request,'projects_module/registration.html',context)

@login_required
def editanddelete_view(request):
    project_list = RegistrationModel.objects.all()
    context = {'project_list':project_list}
    return render(request,'projects_module/editanddelete.html',context)

@login_required
def edit_view(request,id):
    edit = RegistrationModel.objects.get(pk=id)
    if request.method=='POST':
        form = RegistrationForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
        project_list = RegistrationModel.objects.all()
        context = {'project_list':project_list}
        return render(request,'projects_module/editanddelete.html',context)
    else:
        edit = RegistrationModel.objects.get(pk=id)
        form = RegistrationForm(instance=edit)
    return render(request,'projects_module/edit.html',context={'form':form})

        

    return redirect(request,'editanddelete.html')

@login_required
def delete_view(request,id):

    del_object = RegistrationModel.objects.get(pk=id)

    del_object.delete()

    project_list = RegistrationModel.objects.all()
    context = {'project_list':project_list}
    return render(request,'projects_module/editanddelete.html',context)

    
