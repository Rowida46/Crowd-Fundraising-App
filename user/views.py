from django.shortcuts import render,redirect,reverse,get_object_or_404
# Create your views here.
from django.contrib.auth.models import User
from user.models import User
from django.shortcuts import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from user.forms import RegistraionForm
from projects.models import Project

from user.forms import UpdateUserForm

    
    
def showprofile(request,id):
        user=get_object_or_404(User,id=id)
        if user:
            if request.method=='GET':
                # user=RegistraionForm(instance=request.user)
                return render(request,"profile.html",context={'user':user})
            
        
        
        
def user_project(request,id):
    user=User.objects.get(id=id)
    project=Project.objects.filter(user=user)
    context={
        "user":user,
        "project":project
    }
    return render(request,'viewProject.html',context)
    
     



def delete_profile(request,id):
    user=User.objects.get(id=id)
    if request.method=='POST':
        user.delete()
        return redirect('donation')
    elif request.method=='GET':
        user.delete()
        return redirect('donation')
    
    



     
     
     
     
        
# def user_donation(request,id):
#     user=User.objects.get(id=id)
#     project=Donation.objects.filter(user=user)
#     context={
#         "user":user,
#         "project":project
#     }
#     return render(request,'viewProject.html',context)

        
                

    
def editprofile(request,id):
    user=get_object_or_404(User,id=id)
    print(user)
    form = UpdateUserForm(request.POST, request.FILES, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            # print("photo from form is :", form.cleaned_data["photo"])
            # request.user.photo = form.cleaned_data["photo"]
            form.save()
            return redirect("viewprofile")
        else:
            form = UpdateUserForm(
                initial={
                    "first_name": request.user.first_name,
                    "last_name": request.user.last_name,
                    "phone": request.user.phone,
                    "date_birth": request.user.date_birth,
                    "facebook_link": request.user.facebook_link,
                    "country": request.user.country,

                }
            )
        # context={"form": form}
        form.save()
    return render(request, "editprofile.html", {"form": form})





